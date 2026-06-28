# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 00035009-b5d0-31d3-a13c-9423eda4d512 | -12.20226 | -52.9092 | 2026-06-28 00:41:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 91bb72e6-06b1-3fb9-b610-708c448a8043 | -14.05833 | -58.22652 | 2026-06-28 00:41:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 17.0 |
| f8a583ea-a1a4-3a68-a79e-5480f095051d | -11.91302 | -57.10988 | 2026-06-28 00:41:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 396ff444-dc6f-3998-b603-06038d24d4fd | -10.81121 | -56.61117 | 2026-06-28 00:41:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b9577e87-61a9-3060-bf12-7962d1426340 | -11.21425 | -54.32637 | 2026-06-28 00:41:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| f6deeb30-543d-306a-88d6-85f19591e246 | -13.65224 | -60.62215 | 2026-06-28 00:41:00 | TERRA_M-M | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| e98bd533-2860-34ec-9cc2-150dc5544dbf | -12.19646 | -52.87077 | 2026-06-28 00:41:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 314.0 |
| 7e3f8b8b-1e13-3781-b603-d337841be34a | -11.90566 | -57.13527 | 2026-06-28 00:41:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 3c83fc24-5a93-392a-b611-541c4ec2ec01 | -14.63398 | -54.45747 | 2026-06-28 00:41:00 | TERRA_M-M | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 47542778-3fee-3251-bf10-0e10c482a02a | -11.91547 | -57.12787 | 2026-06-28 00:41:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| e76b057d-abc4-32e3-92ce-91893a8bbeab | -11.91867 | -58.66082 | 2026-06-28 00:41:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 5dde064a-88af-307c-9e92-f36336859472 | -12.17506 | -57.15177 | 2026-06-28 00:41:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 27.1 |
| dff0efc2-39ac-37a7-b096-75d9e45d510c | -11.90443 | -57.12627 | 2026-06-28 00:41:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| f7fb86dc-aef4-367b-9a13-f0929cd7fd0e | -12.09078 | -52.02799 | 2026-06-28 00:41:00 | TERRA_M-M | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 125.7 |
| 926ca277-6934-39d1-bcb6-a33defe54f55 | -9.59501 | -56.93116 | 2026-06-28 00:41:00 | TERRA_M-M | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 3ef1b348-5894-3842-8952-f5913fb237c3 | -12.18146 | -52.91258 | 2026-06-28 00:41:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 0fba4258-2eb2-3510-b11e-5a4f04bf1fec | -9.08931 | -59.38992 | 2026-06-28 00:41:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 17.7 |
| a4317f54-568e-3471-8587-5c7dcc6a2206 | -9.19013 | -58.07214 | 2026-06-28 00:41:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 7804957a-fbd4-350e-a6e9-8f0c0657e1a1 | -12.18992 | -52.89813 | 2026-06-28 00:41:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 184.2 |
| 6642dc91-91fa-3473-9fd5-baf918268253 | -12.60501 | -57.87768 | 2026-06-28 00:41:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 200634f6-bc90-3ce8-8de4-41be35ec7141 | -14.05703 | -58.21664 | 2026-06-28 00:41:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 91615842-41d6-3f6a-b3e2-be65c6d1a31e | -12.16621 | -57.15305 | 2026-06-28 00:41:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 1e06ed5f-4a1f-3990-87b9-3a118ede6f09 | -10.9014 | -56.85715 | 2026-06-28 00:41:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 7bcd3980-6bd9-3563-8f69-b36678932f0f | -9.03418 | -61.33463 | 2026-06-28 00:41:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 74205490-9998-3f89-8a88-c65b83a6d979 | -12.46507 | -58.49288 | 2026-06-28 00:41:00 | TERRA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 82.8 |
| c83aeacb-769a-347f-8d0e-37eec239bcd3 | -11.52018 | -54.79251 | 2026-06-28 00:41:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 49d970be-b660-370e-8825-6243306cd7cb | -12.98738 | -57.77996 | 2026-06-28 00:41:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 44230bfa-cea6-3ab6-bb77-08a86d1dc53d | -9.61592 | -56.29472 | 2026-06-28 00:41:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| ecc9cf0e-ea20-3739-96c9-09c3da113424 | -11.9292 | -58.66943 | 2026-06-28 00:41:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 1284d841-1425-38c7-ba27-456815c33cca | -12.07966 | -52.02989 | 2026-06-28 00:41:00 | TERRA_M-M | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| d1885bcd-bdcc-38d2-854e-d1fe1f4362ee | -12.19452 | -52.8579 | 2026-06-28 00:41:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 8bd3f033-0f85-3aa9-9410-ef438ee56c69 | -11.91998 | -58.67065 | 2026-06-28 00:41:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e3990299-9d43-331f-a84e-294a6d0b5151 | -12.62551 | -57.89383 | 2026-06-28 00:41:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 14.8 |
| eb4a80ce-890a-3b99-ab1c-d2ecb7696f1a | -10.63731 | -50.52901 | 2026-06-28 00:41:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 191f739f-334b-3f0f-b28b-95be0d2b6158 | -10.93799 | -56.86095 | 2026-06-28 00:41:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c74d1f12-5c0f-3f91-ba9b-afab369d249d | -9.09317 | -59.41944 | 2026-06-28 00:41:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 2ec2f38e-7a9c-341b-b013-493ca0628fcd | -11.65692 | -57.25671 | 2026-06-28 00:41:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 34.3 |
| 5e0a96eb-adf1-3a17-b1c5-627204527115 | -11.88428 | -57.11085 | 2026-06-28 00:41:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| b632cc92-8468-3b7d-b382-8964a6d4d981 | -12.23174 | -56.5532 | 2026-06-28 00:41:00 | TERRA_M-M | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 3cd2b49b-fa4f-3098-8b48-2ceeff6f6caa | -12.17629 | -57.16079 | 2026-06-28 00:41:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 3aa76158-0e8a-338d-91e0-2ef685320a10 | -12.59601 | -57.87896 | 2026-06-28 00:41:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 74.9 |
| ec463391-abaa-3390-b212-bfbf8eed7c52 | -11.21217 | -53.82122 | 2026-06-28 00:41:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 6abedbeb-3bfb-375e-b470-32a038ce0350 | -12.1984 | -52.88365 | 2026-06-28 00:41:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 233.8 |
| 91dfcda1-23af-342a-9b25-9b747c80dfc2 | -11.91606 | -57.40973 | 2026-06-28 00:41:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 85956351-4f5b-3cab-a381-4177deb7e2be | -10.93675 | -56.85201 | 2026-06-28 00:41:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 769f8e43-a71a-300a-8be1-2eda094f823f | -12.16497 | -57.14404 | 2026-06-28 00:41:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| f60455fe-5912-3852-a3e5-f5dce3e13136 | -12.60626 | -57.88703 | 2026-06-28 00:41:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 8ac1770e-a806-336e-9e99-aebfb544beb5 | -10.30246 | -57.12357 | 2026-06-28 00:41:00 | TERRA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 156.6 |
| 02efd9c4-d25c-385c-90b5-6ef936576145 | -11.53098 | -54.80111 | 2026-06-28 00:41:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 9a7f9051-3494-30e9-83d2-d2de54a4ab27 | -11.90196 | -57.10829 | 2026-06-28 00:41:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 96c440ee-bdaf-3383-933f-e476362a3029 | -9.17041 | -58.07205 | 2026-06-28 00:41:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| a5ce9df4-1f4f-3963-afcf-0a828b120e6e | -10.29486 | -57.13376 | 2026-06-28 00:41:00 | TERRA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 38.9 |
| c708c0e5-61de-340a-884a-78bdbea65e62 | -12.28577 | -57.5551 | 2026-06-28 00:41:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 4e3a7fad-9c5f-329c-a1c3-415a96905387 | -9.60262 | -56.92094 | 2026-06-28 00:41:00 | TERRA_M-M | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| baa4619b-2a08-3395-91d8-89782d060c67 | -12.17259 | -57.13373 | 2026-06-28 00:41:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 49.2 |
| e9b432f3-9f99-3eea-9f0e-7a235810d9a9 | -11.52951 | -54.79104 | 2026-06-28 00:41:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 2e36ef70-89e5-30c5-8daa-37e0a09cd027 | -12.17382 | -57.14275 | 2026-06-28 00:41:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 36.0 |
| ce92d0ba-9a2f-354b-896a-0628b86ff240 | -12.16251 | -57.126 | 2026-06-28 00:41:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 7fc16c54-5503-3674-8ee8-7a3f3608a2fa | -14.04782 | -58.21793 | 2026-06-28 00:41:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 22.3 |
| dacfb814-8cf4-3fdf-ad3f-b9d13ec21cdc | -11.9279 | -58.65964 | 2026-06-28 00:41:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 5225148d-367f-387e-b733-7ecac601beea | -10.39257 | -56.76994 | 2026-06-28 00:41:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 80a586f3-7d12-3e00-8611-176435180f61 | -12.20882 | -52.88195 | 2026-06-28 00:41:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 50.6 |
| cc42a02f-d7d2-36a1-b14e-a67ed8be5c3b | -11.31342 | -53.95075 | 2026-06-28 00:41:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 2bd7cf47-5e59-36e4-8561-41e3ecee1b11 | -12.23049 | -56.5442 | 2026-06-28 00:41:00 | TERRA_M-M | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 4f65be55-2100-3bbd-9899-b032e0e28560 | -12.58731 | -57.81366 | 2026-06-28 00:41:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ecca3f14-270b-301c-9397-1d987cd8268b | -9.09188 | -59.40955 | 2026-06-28 00:41:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.0 |
| e25860a1-fe50-37a5-bb88-a3ee9eb012a4 | -14.63541 | -54.4673 | 2026-06-28 00:41:00 | TERRA_M-M | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 552af4ca-b930-3fe3-80f3-75c799923fd0 | -11.93859 | -58.61249 | 2026-06-28 00:41:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2b94349e-5de1-34b4-bea4-9c3c6c75542c | -11.21388 | -53.83273 | 2026-06-28 00:41:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 14.3 |
| ed22e07a-4285-367c-b3dd-1c953e033af5 | -12.08855 | -52.01329 | 2026-06-28 00:41:00 | TERRA_M-M | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 308.1 |
| da877720-9956-3cbc-9d0c-a33e63bce028 | -14.04911 | -58.22782 | 2026-06-28 00:41:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 09bc79d5-08e1-3a49-a5a7-8381a135f80f | -12.17755 | -52.88695 | 2026-06-28 00:41:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 27.3 |
| df48f4ae-7494-3164-8cc1-b8e379db5b11 | -11.9167 | -57.13687 | 2026-06-28 00:41:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| aa103a93-06d4-3293-acae-bce20fff5cfb | -12.17951 | -52.89981 | 2026-06-28 00:41:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 137.6 |
| 491a4d4f-a96c-332b-89f0-ad2818f8effa | -12.61525 | -57.88573 | 2026-06-28 00:41:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8fdfdcd2-22c1-35bd-a0e7-3a8ef6527347 | -10.30492 | -57.14141 | 2026-06-28 00:41:00 | TERRA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| d01a8aac-d1ed-3ff3-b6aa-496f5ced3c29 | -11.2221 | -53.81969 | 2026-06-28 00:41:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 51382ae3-d12a-326c-ab2e-ffce2229554e | -12.19186 | -52.91088 | 2026-06-28 00:41:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 116.6 |
| 95dc9707-af20-3d8d-a45b-1c372f10cbeb | -11.65815 | -57.26571 | 2026-06-28 00:41:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 9d7dd4aa-e6ea-3a9e-a454-0e2db11cdc28 | -12.17136 | -57.12472 | 2026-06-28 00:41:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 927e8283-3132-328a-aaf9-13bf5d035966 | -11.9032 | -57.11728 | 2026-06-28 00:41:00 | TERRA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 9f64c843-a627-346d-919c-81bba8d8d01a | -12.42831 | -58.41466 | 2026-06-28 00:41:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 39d7137d-d9c9-3893-93c0-f9264a0b7abc | -12.09062 | -52.02227 | 2026-06-28 00:41:00 | TERRA_M-M | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 398.6 |
| 0a0b173d-0ac1-35d9-a619-7ab2237e20e3 | -12.08827 | -52.00756 | 2026-06-28 00:41:00 | TERRA_M-M | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 285.2 |
| c7372626-541c-3485-8d88-13a85fd5ad24 | -11.72504 | -59.35506 | 2026-06-28 00:41:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| ab08afc4-9fde-37be-8d44-1c21973cdc09 | -12.6075 | -57.8964 | 2026-06-28 00:41:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| d3a34739-f78e-3852-a9a2-86a2a6615c76 | -12.16374 | -57.13502 | 2026-06-28 00:41:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 36.7 |
| d50b86b6-9b8a-39ca-bfa0-da3d6bec0eba | -12.18798 | -52.88531 | 2026-06-28 00:41:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 189.0 |
| 3d73dc1d-32a9-3af6-8fb3-d2200eef7b8a | -9.59377 | -56.92222 | 2026-06-28 00:41:00 | TERRA_M-M | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| afc986a5-3ad4-3981-8d1a-a158311f8c29 | -11.87971 | -57.82128 | 2026-06-28 00:41:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ac7268e5-584f-3d86-8294-9cad0f42839f | -12.04958 | -55.45768 | 2026-06-28 00:41:00 | TERRA_M-M | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| b903272d-00e9-3075-9314-31b5242b7b05 | -13.22559 | -54.41213 | 2026-06-28 00:41:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 91ef48e5-f8ec-37a4-a067-7cdca8152b1f | -12.23299 | -56.56221 | 2026-06-28 00:41:00 | TERRA_M-M | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 18.5 |
| b85f0857-46e2-3a75-8446-e13f9d29920b | -9.08458 | -59.40643 | 2026-06-28 00:41:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| d7bfec60-a386-350e-83c9-9fe5205afbde | -9.18892 | -58.06313 | 2026-06-28 00:41:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d00551e1-c461-36ea-9b5a-08c89b52d203 | -9.08591 | -59.41629 | 2026-06-28 00:41:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 6ae44c90-71f9-39ca-9d46-7dd4d0e2b320 | -10.30369 | -57.13249 | 2026-06-28 00:41:00 | TERRA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 186.4 |
| 97d400c4-8785-3d49-a4cf-fb16e8cb7dcf | -10.29363 | -57.12484 | 2026-06-28 00:41:00 | TERRA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 45.2 |
| afc14e0b-0131-3672-a3b4-1a09c3aa1c44 | -12.45833 | -58.49974 | 2026-06-28 00:41:00 | TERRA_M-M | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 85.0 |
| d39f7916-6175-3d5e-bc5f-0191545276ce | -9.0906 | -59.39973 | 2026-06-28 00:41:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 27.1 |


[Clique aqui para ver as próximas entradas](README5.md)
