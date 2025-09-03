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

## Dados Diários - Página 113

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 99693bc4-306c-3689-b243-4c9e53ea3259 | -7.7224 | -48.7572 | 2025-09-03 12:40:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 265.3 |
| 7a4babba-b18f-3f59-bc03-9ea72ef87c07 | -15.1771 | -52.356 | 2025-09-03 12:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 27ce0c65-1705-3ba7-88ee-e41af0e36d9a | -8.0197 | -44.1072 | 2025-09-03 12:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 141.3 |
| ed710a9d-76fe-317d-a044-b2acdf7ac5a6 | -5.9264 | -57.7303 | 2025-09-03 12:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 45cc1db3-00b1-3746-83a8-2a542de63a5e | -10.0932 | -54.7667 | 2025-09-03 12:50:00 | GOES-19 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 142.0 |
| 4a7a0e53-bd5a-3e0d-af3e-e18d42bb7a86 | -9.6229 | -47.0638 | 2025-09-03 12:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 104.1 |
| ea9c3452-e79c-3dab-aa32-1b81b7f17ac7 | -5.9265 | -57.7108 | 2025-09-03 12:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| c464f176-ce76-3848-be3b-7312f0f5ffd9 | -12.7926 | -47.6638 | 2025-09-03 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 72712b7a-8974-3c75-8e07-cf776f9188db | -8.0796 | -45.3617 | 2025-09-03 12:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 92.2 |
| ca93f958-d4c8-3b22-853a-4bb41eed8c00 | -9.6232 | -47.0416 | 2025-09-03 12:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 85.0 |
| e421e164-69c2-3e45-a82f-cb808c8634f6 | -7.5157 | -45.3478 | 2025-09-03 12:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 131.4 |
| e662db31-5949-3fd8-af1e-0bf52d42ab86 | -13.5162 | -47.0393 | 2025-09-03 12:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 70.0 |
| e991a61d-38a9-3d72-af4d-a3cb3ef8c732 | -7.4966 | -45.3722 | 2025-09-03 12:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 5842edcd-32d0-311b-b03f-dbd96322a7e8 | -5.7343 | -45.5375 | 2025-09-03 12:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 98.8 |
| c8cefe53-63ad-3ec3-a066-2ad6e2adb4f5 | -6.0597 | -44.6976 | 2025-09-03 12:50:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| f3929ba5-2294-3767-81e1-d930d2a6b814 | -12.824 | -48.06 | 2025-09-03 12:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |
| dd462f29-c892-3094-9327-11369d88f819 | -6.9942 | -43.2308 | 2025-09-03 12:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 121.0 |
| f88a3f17-7b42-3416-a785-c72f9c91962e | -11.8533 | -51.4318 | 2025-09-03 12:50:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 79.0 |
| fbf90b5b-80fa-323f-a58b-9d3277a62b14 | -10.4853 | -50.346 | 2025-09-03 12:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 140.5 |
| a21d27f8-0f9e-305b-92f7-35f28f493d39 | -6.797 | -44.0859 | 2025-09-03 12:50:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| a60c00f1-c324-3784-8ab1-41ad4bad5b69 | -7.0131 | -43.2291 | 2025-09-03 12:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 126.4 |
| 5dd73992-dcf4-335c-961d-fb3f6d5259bc | -7.5302 | -47.4443 | 2025-09-03 12:50:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 221.1 |
| 88dc9482-b7e8-3b72-adeb-a1e3bcce63b1 | -7.0128 | -43.2525 | 2025-09-03 12:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 181.8 |
| 1d1ee3fd-6c89-3fc9-ba95-68023b9f3179 | -9.7615 | -49.4121 | 2025-09-03 12:50:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| e118528b-d742-3bae-8d3d-1e89662c73d7 | -7.4969 | -45.3495 | 2025-09-03 12:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 136.2 |
| 5564b138-37e1-3a0c-b127-bd9961392297 | -10.5045 | -50.3226 | 2025-09-03 12:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 0e4721fb-7594-3cc7-82b0-47a7335f12b8 | -8.2006 | -49.5559 | 2025-09-03 12:50:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| de2ca55a-154b-305a-9589-9407efda9c58 | -9.7613 | -49.4337 | 2025-09-03 12:50:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 4653c94d-aedb-37c0-ac40-978c60b43659 | -11.0181 | -51.5001 | 2025-09-03 12:50:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 161.6 |
| 2fcf0695-d368-3fe6-8f7d-aa2a065d110b | -11.9606 | -50.6108 | 2025-09-03 12:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 0c2bc8c8-9bbe-37f5-adc4-9c38704a89cc | -5.9079 | -57.7506 | 2025-09-03 12:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 134.4 |
| 8f75e9e7-1a3c-3237-9afb-818d05bba9ca | -9.402 | -48.0585 | 2025-09-03 12:50:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 150.1 |
| 452bcfe4-b564-3d82-b6a3-d7ad4677e720 | -7.4842 | -44.8043 | 2025-09-03 12:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 84.8 |
| f33d3dd4-ebc9-31ca-bc3b-6796730c9d8e | -6.1234 | -45.9139 | 2025-09-03 12:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 100.3 |
| f74b2d36-2d23-3ef7-8700-05a95cdd8472 | -9.96 | -51.6244 | 2025-09-03 12:50:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 114.3 |
| 318d0cc0-3ec8-3796-859b-da936ff07da3 | -8.8653 | -45.824 | 2025-09-03 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 5a265786-11de-3525-b239-1099c63a7d2e | -11.3901 | -43.5602 | 2025-09-03 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 137.1 |
| b20fa686-e7ce-3a33-96b7-707b39ba5848 | -8.0608 | -45.3636 | 2025-09-03 12:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 265.2 |
| aa94e251-19f3-3c98-adab-e810b9d5492d | -6.4648 | -49.5151 | 2025-09-03 12:50:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 880785f6-9dbe-3af7-84bc-e4df4a6203d5 | -5.8895 | -57.7513 | 2025-09-03 12:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 06fb88f8-ad4f-3622-ace9-591a30f1e52a | -6.994 | -43.2543 | 2025-09-03 12:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 179.3 |
| e76e0e0a-af3a-3a16-86c5-494c2603954c | -5.8455 | -45.6421 | 2025-09-03 12:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 286.5 |
| 0bf404d3-c5ed-3338-894b-2e1f89d92520 | -5.8896 | -57.7318 | 2025-09-03 12:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 081328a3-c8d9-36f2-9f7f-bca833f74121 | -11.3709 | -43.5631 | 2025-09-03 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 93d226a3-9f89-320b-9eb3-5b0d551a8762 | -6.6982 | -48.4035 | 2025-09-03 12:50:00 | GOES-19 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 894304f2-89c2-338e-9642-1c94a2f663f6 | -10.4856 | -50.3246 | 2025-09-03 12:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 1aa17aef-3840-39b2-990d-567d656ab596 | -9.4023 | -48.0365 | 2025-09-03 12:50:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 908e3963-1735-323a-a102-9ef0bd0ac8c9 | -9.7427 | -49.414 | 2025-09-03 12:50:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 11db1e0e-d59e-3b57-a9e1-8187599b36b5 | -6.0699 | -45.6259 | 2025-09-03 12:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 7226c064-01b4-3abc-bc2c-f52b96ebabc9 | -11.6836 | -57.3518 | 2025-09-03 12:50:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 76.1 |
| be583173-b3b8-39e6-b1be-9608e1a76000 | -5.908 | -57.7311 | 2025-09-03 12:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 204.2 |
| 1747cbe4-3b43-393b-a3f3-e2872baacee2 | -11.6165 | -52.0689 | 2025-09-03 12:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 87.0 |
| a63c4783-3446-3f56-a34a-426bdd2db8cb | -10.9323 | -50.8529 | 2025-09-03 12:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 5b26438f-f660-380a-9c39-93578ce8d5a6 | -9.1373 | -49.6659 | 2025-09-03 12:50:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 085501bf-339e-3318-ab87-251da0e4c15e | -7.53 | -47.4662 | 2025-09-03 12:50:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 157.4 |
| 7b67767e-2be7-38da-b04c-d279958d3b08 | -11.3897 | -43.5839 | 2025-09-03 12:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 28edc63d-846a-3106-8ba7-690c0eec654a | -5.8642 | -45.6408 | 2025-09-03 12:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 90466c24-416b-3f48-9403-63dfe26dfbaa | -8.0197 | -44.1072 | 2025-09-03 13:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 82.0 |
| b88b4277-c655-3441-831a-062698c9d880 | -12.793 | -47.6415 | 2025-09-03 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 63af4709-0017-364b-9d4c-0804740084e5 | -7.7036 | -48.7587 | 2025-09-03 13:00:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 138.0 |
| 1926870d-f1ed-3cab-b691-811896217d0f | -12.824 | -48.06 | 2025-09-03 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 64d0da01-679f-31d5-9f78-7dfea92323d8 | -11.0184 | -51.479 | 2025-09-03 13:00:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 116.8 |
| f6199937-80f4-37c0-b4fc-27b39b54779f | -9.7615 | -49.4121 | 2025-09-03 13:00:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 119.9 |
| c2351217-453c-33d6-89dd-987dc577ce00 | -10.4853 | -50.346 | 2025-09-03 13:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 528148dd-c011-3824-a492-246a2c30d709 | -10.0221 | -45.6235 | 2025-09-03 13:00:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 282e1c40-f826-35f3-8eb2-4dbc321eba85 | -12.7926 | -47.6638 | 2025-09-03 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 34847db5-d4a7-3fd6-b14e-03130c0049e4 | -8.8842 | -45.822 | 2025-09-03 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 5004f83f-f446-3c82-a57c-3c0728674258 | -11.3701 | -43.6104 | 2025-09-03 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 42a90b41-f058-38a3-a492-fb09a0f42545 | -11.0181 | -51.5001 | 2025-09-03 13:00:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 305.1 |
| 12d4a81e-e31f-3483-ba8f-4d9979f44808 | -5.908 | -57.7311 | 2025-09-03 13:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 215.7 |
| a1162a9b-9f21-36b1-8e2e-5b05801bc907 | -11.6647 | -57.3533 | 2025-09-03 13:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 74.4 |
| fcef76ce-97ad-3bf8-a049-cd2ef90575e8 | -9.7613 | -49.4337 | 2025-09-03 13:00:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 202.9 |
| 049e1ec6-3ea8-3ed3-9523-c86d563c47d3 | -6.994 | -43.2543 | 2025-09-03 13:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 100.1 |
| 16bd8d9a-02be-334e-83e9-bb9d0c636bf4 | -6.35 | -45.6723 | 2025-09-03 13:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 09863f2e-4e59-3f99-916f-077482f81310 | -13.5162 | -47.0393 | 2025-09-03 13:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 70.9 |
| c981777e-85ab-3dac-9c4e-03cfab25219a | -8.8839 | -45.8446 | 2025-09-03 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 7fa2372e-eaeb-3fec-8193-3c45dfc32e68 | -10.0411 | -45.6212 | 2025-09-03 13:00:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 117.7 |
| a650ed88-315d-3c13-a811-89d802adab57 | -11.9443 | -45.7769 | 2025-09-03 13:00:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 169.0 |
| c3837188-12ab-3410-9a1d-0c67c3c06c28 | -12.8244 | -48.0377 | 2025-09-03 13:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 0d51548b-b07c-3fa5-9bc9-3a96084ef6f3 | -8.3644 | -48.3116 | 2025-09-03 13:00:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 89a993ee-5117-36be-8e37-d29dbcae54c5 | -9.6232 | -47.0416 | 2025-09-03 13:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 8c5afa54-b119-3458-a37a-2417465ba466 | -8.2006 | -49.5559 | 2025-09-03 13:00:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 084146a5-d902-3f82-af1b-24ef999783a2 | -8.4601 | -45.0724 | 2025-09-03 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 4298dc74-8515-38a9-8090-c4f306b1d0f4 | -11.9631 | -45.797 | 2025-09-03 13:00:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 7210616d-7c10-305f-83a9-87c2103d55ea | -7.4966 | -45.3722 | 2025-09-03 13:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 77d8d678-7677-3fcb-84f2-bcc2876aa5cd | -5.9264 | -57.7303 | 2025-09-03 13:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 1f40ac3f-6b91-3cc0-989d-5caa9fa44a53 | -7.5302 | -47.4443 | 2025-09-03 13:00:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 0f258284-6d6c-335e-9c13-6e5f5677e6bd | -6.1234 | -45.9139 | 2025-09-03 13:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 142.7 |
| da72daed-b3a5-3db9-9d92-7ec68122cac0 | -11.8533 | -51.4318 | 2025-09-03 13:00:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 2e430572-3595-375d-bb50-0cdb8f99e576 | -5.7795 | -42.5837 | 2025-09-03 13:00:00 | GOES-19 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 89.1 |
| 0c6ec423-4ef6-37cc-a775-8269d67182a7 | -7.5157 | -45.3478 | 2025-09-03 13:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 182.1 |
| b1b82851-84f0-3e02-b75f-080eb82dc61a | -7.4842 | -44.8043 | 2025-09-03 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 92.2 |
| aa10b6a7-1fb6-3bb0-ac37-8c28e31c2429 | -9.96 | -51.6244 | 2025-09-03 13:00:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 77.7 |
| e289488c-567a-3817-8fdd-b1a529192f5f | -15.2675 | -52.7261 | 2025-09-03 13:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 147.4 |
| 03e1c492-5796-3b06-94c2-18ce5c61b240 | -7.0131 | -43.2291 | 2025-09-03 13:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 82.9 |
| d950affa-5b86-33de-939d-109b5400c939 | -6.797 | -44.0859 | 2025-09-03 13:00:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 04fafa48-d2b5-3d12-be95-d9bbef86b015 | -10.9133 | -50.8549 | 2025-09-03 13:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 138.9 |
| 8bc7e342-75a1-3f02-a110-0438d1bb4001 | -6.4648 | -49.5151 | 2025-09-03 13:00:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 2afad207-f9b2-3ef0-957f-47c2926c43d7 | -7.7226 | -48.7355 | 2025-09-03 13:00:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 135.0 |
| d147d37f-f72b-3f20-ae5f-049a33ccb47f | -11.3901 | -43.5602 | 2025-09-03 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 160.2 |


[Clique aqui para ver as próximas entradas](README114.md)
