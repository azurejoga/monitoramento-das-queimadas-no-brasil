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

## Dados Diários - Página 111

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 58ed9984-3e28-3582-94a7-654b77870dd1 | -9.6553 | -46.0973 | 2025-09-04 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 5844169b-7f46-3b18-b6df-d7f7bb28ca1c | -10.5031 | -50.4295 | 2025-09-04 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| eb433196-2917-3918-9d9d-7637d153f071 | -10.5316 | -57.7747 | 2025-09-04 14:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 1c473978-a560-3456-9279-005caf1150bc | -6.8941 | -45.5609 | 2025-09-04 14:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 167.5 |
| c60e49f1-1154-38f4-b83a-836ab021f533 | -10.1454 | -46.265 | 2025-09-04 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 38ae095a-3677-3226-98d1-7da3740ce5b9 | -11.5856 | -47.7836 | 2025-09-04 14:20:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 79.3 |
| fd4d40f0-e0c6-321c-afcb-42604eece9fe | -7.6851 | -48.7386 | 2025-09-04 14:20:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 186.2 |
| dedc9f22-ac63-33ad-8b37-90b2fbc79014 | -12.5233 | -53.8071 | 2025-09-04 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 163.8 |
| bcc6fda6-dd2d-31c7-a882-98ebb31a7792 | -13.8651 | -47.9734 | 2025-09-04 14:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 83fdfb07-ccd4-3249-9ba9-0fcf4cde35ca | -11.5972 | -52.092 | 2025-09-04 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 175.6 |
| 6468b722-3d8a-3d9c-937b-c850088232e6 | -7.0128 | -43.2525 | 2025-09-04 14:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 100.9 |
| be724acc-a44f-315a-a63b-7f0c72568473 | -12.4981 | -48.061 | 2025-09-04 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| a1ce63ce-658e-369b-96ac-3c784943c007 | -11.0062 | -45.9072 | 2025-09-04 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 8b0e9572-7978-341e-ba35-b666bcf9cba7 | -11.6047 | -47.7811 | 2025-09-04 14:20:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| b83d34f7-ed9d-3fa6-91ba-deec6d68c865 | -8.0417 | -45.3882 | 2025-09-04 14:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 76.7 |
| cd8c682d-2c2e-3c17-9c56-cf01968c3f3a | -11.853 | -51.453 | 2025-09-04 14:20:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 3fc68bf4-04e4-32b9-9203-fb60e7ea51ba | -9.5023 | -57.8229 | 2025-09-04 14:20:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 1236856e-2c1c-32ec-9044-0b2ad85203f5 | -8.0796 | -45.3617 | 2025-09-04 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 137.5 |
| 077b0b01-bb8b-347d-a148-19547c467dc1 | -4.9951 | -56.256 | 2025-09-04 14:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 109.9 |
| 945272fb-fee9-3d1e-a965-c4b05bd25342 | -14.3916 | -53.0722 | 2025-09-04 14:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 90.9 |
| afb331a4-244d-3965-8e10-26569b933f25 | -7.7066 | -50.3188 | 2025-09-04 14:20:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 41ff68c0-c74b-3154-b76e-e37cea4527fb | -5.774 | -45.2639 | 2025-09-04 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 161.3 |
| 74cd1a6f-bb3d-3dd0-81aa-1d1a289e407c | -10.6577 | -51.5996 | 2025-09-04 14:20:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 158.2 |
| 03fdacd4-ec5f-3be7-a499-23eccccf055c | -6.2952 | -43.5961 | 2025-09-04 14:20:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 51402c21-8794-35a8-97ad-6107c3d8e803 | -5.7729 | -45.3995 | 2025-09-04 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 21fd1a41-5bb5-31be-b8a1-1652923e7355 | -12.2344 | -50.1488 | 2025-09-04 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| d7dc77dd-8f59-3585-9519-abee3f4349b8 | -14.9865 | -50.0769 | 2025-09-04 14:20:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 3929b2ef-09a0-3e79-a675-7ad1da683065 | -13.1079 | -57.1109 | 2025-09-04 14:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 647cd686-484d-3851-9608-b2bb11f19488 | -11.6601 | -54.5093 | 2025-09-04 14:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 108.4 |
| dda25121-5573-35e2-a303-b651029d53f3 | -8.0389 | -44.082 | 2025-09-04 14:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 4e4cd000-d817-3367-92c7-d14e213ce869 | -6.2289 | -42.7118 | 2025-09-04 14:20:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 83.9 |
| f34a449c-8960-3a44-8bd3-e2086c563fd5 | -14.3888 | -53.2406 | 2025-09-04 14:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 49e00890-19f5-3e07-b9d9-6fb0503b7066 | -5.7187 | -45.1773 | 2025-09-04 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 145.4 |
| 9c61bd83-42e6-3683-8d66-26d81e47b7ed | -7.6854 | -48.717 | 2025-09-04 14:20:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 93b40924-293b-3610-b7c9-e4426f3279a6 | -5.7341 | -45.56 | 2025-09-04 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| e76ff28f-a8fb-342a-a408-f8dd1bf7a69b | -6.2315 | -42.4515 | 2025-09-04 14:20:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 158.6 |
| 0da5d83f-294d-37a9-b820-afb800a4ebbd | -5.7189 | -45.1547 | 2025-09-04 14:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| dc3e4055-d362-3a1c-b590-8ae938d66a21 | -12.8999 | -57.0091 | 2025-09-04 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 65.3 |
| bf69f612-c773-3544-839e-c98615b9bd39 | -12.9006 | -56.9488 | 2025-09-04 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 21fb1144-c338-3a2c-b9c2-871d15a3aeae | -11.8524 | -51.4954 | 2025-09-04 14:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 84a6c434-eaef-3ca0-a97a-b26bc4b02a9f | -5.1134 | -43.7777 | 2025-09-04 14:30:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 8b3e2d9e-5c02-3663-b631-57293ee46b67 | -6.8466 | -52.8132 | 2025-09-04 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 803df372-76d7-3cef-9964-daf4151301c4 | -5.6777 | -45.6089 | 2025-09-04 14:30:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 56e45906-7610-3866-823d-59d2a31751f2 | -11.0044 | -49.7541 | 2025-09-04 14:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 472edd18-22d0-3738-be78-9bcf8caa5db2 | -6.2205 | -43.5558 | 2025-09-04 14:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 155.1 |
| 03eaa61c-dabb-3c0c-b8ae-200bbaed524c | -11.6228 | -46.684 | 2025-09-04 14:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 7e7abb05-73fa-3eca-9c95-41f39777b8ca | -12.967 | -54.7705 | 2025-09-04 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 08e5ca71-e66b-3783-81f2-5203b1d787a2 | -11.8343 | -51.4339 | 2025-09-04 14:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 97.7 |
| be70b78e-65e1-3383-af07-3733b42c0e1c | -5.8108 | -45.3291 | 2025-09-04 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 99a07fd6-5565-3d2b-bb03-b8247ab8f868 | -5.6813 | -45.18 | 2025-09-04 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 5fd8b1aa-f780-31b4-823a-f83a582d3c85 | -5.774 | -45.2639 | 2025-09-04 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 3c695d34-1c4e-38da-95bd-4d56f6bbd792 | -7.7036 | -48.7587 | 2025-09-04 14:30:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 108.5 |
| b4bc8a22-ea45-363d-b068-810b889d03fc | -12.523 | -53.8278 | 2025-09-04 14:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 9989822c-4f12-3977-a334-3b0e3db83449 | -10.4655 | -50.412 | 2025-09-04 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 191.4 |
| ac8b39b0-057e-32cb-ba43-48dd6ce94db5 | -12.9668 | -54.791 | 2025-09-04 14:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 77.4 |
| b2b20841-979f-3bc2-951f-2b000565b068 | -11.3701 | -43.6104 | 2025-09-04 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 7b9942e1-f6bd-32fe-b3e5-4551623837e3 | -5.7341 | -45.56 | 2025-09-04 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 9058318b-d81c-318b-b225-fb1533a56f8c | -5.6782 | -45.5414 | 2025-09-04 14:30:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 6e9ee514-500a-3887-a772-2981e1aa17a5 | -5.7734 | -45.3317 | 2025-09-04 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 205.4 |
| 831af8ee-a9a4-3ac9-80d2-0031c5bd02ac | -6.2952 | -43.5961 | 2025-09-04 14:30:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 112b8718-0575-3f52-9dd4-49e0c05cdbc6 | -15.737 | -53.635 | 2025-09-04 14:30:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 449bf453-865c-33da-867f-4bfbbd3b587d | -17.0652 | -46.449 | 2025-09-04 14:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 82.3 |
| ba8c7e53-1623-3708-bd35-dfb68f6b7396 | -6.2127 | -42.4532 | 2025-09-04 14:30:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 214.0 |
| 8378908e-ad8a-3898-8283-ba318e904f58 | -15.7366 | -53.6561 | 2025-09-04 14:30:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 78d86a54-3bb7-39da-aa95-3084a1b5df14 | -5.7528 | -45.5587 | 2025-09-04 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 147.1 |
| be1c584d-b4f2-3f49-ab45-20ddcc67c3ad | -9.5023 | -57.8229 | 2025-09-04 14:30:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 799c1391-92fc-390a-86a1-e9a7bb4f038d | -10.5316 | -57.7747 | 2025-09-04 14:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 109.9 |
| 96897f09-60d5-3f49-8c2a-6bfb8d9fdbc5 | -6.3692 | -45.6258 | 2025-09-04 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 964908c9-a2e2-3e20-a3a7-b9ba446972b3 | -11.5782 | -52.094 | 2025-09-04 14:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 117.6 |
| 0e8fb4dd-f964-3ce5-a7f3-6a7f3d47c4c0 | -10.9855 | -49.7562 | 2025-09-04 14:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| c28713f2-24fe-3daf-930d-60a1e6bf6d6b | -4.9951 | -56.256 | 2025-09-04 14:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 129.3 |
| 6346822d-47d3-3d4e-8261-5fa76f77a4e4 | -9.3014 | -47.0986 | 2025-09-04 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| ccc11864-f94f-36d5-85ca-063a23b578be | -7.7066 | -50.3188 | 2025-09-04 14:30:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| e4f34e16-1bf1-3d68-8231-d5e3c6e777d2 | -10.5129 | -57.776 | 2025-09-04 14:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 9f3784e3-5ff9-3a5a-907c-82089e07ebd2 | -9.6913 | -49.0089 | 2025-09-04 14:30:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 003c1aeb-1276-3a6e-ba0e-16c29cb6540b | -11.6599 | -54.5297 | 2025-09-04 14:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 81a7396e-00e4-3a1e-ab38-d5ef495b872a | -13.0889 | -57.1126 | 2025-09-04 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 96023147-6fe6-31da-9649-b4df642b347f | -9.4376 | -46.7947 | 2025-09-04 14:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| a9efb165-5bbe-35ac-b214-e58d668f4d4a | -5.753 | -45.5362 | 2025-09-04 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 91.0 |
| aed46387-9c37-31ef-b514-7f91b79dcc64 | -5.7914 | -45.4208 | 2025-09-04 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 6d470310-7a00-3837-aeb9-c37306252c77 | -4.8862 | -41.771 | 2025-09-04 14:30:00 | GOES-19 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 128.3 |
| 4e0d67b3-e936-3889-acfc-12ddcb166f49 | -13.1079 | -57.1109 | 2025-09-04 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 131.7 |
| f802ddfd-a6fc-362d-8785-16df3084deef | -8.8848 | -45.7767 | 2025-09-04 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 6aaab7a3-6bdb-3bfa-a518-70d3bea5383f | -6.0232 | -46.6784 | 2025-09-04 14:30:00 | GOES-19 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 173.9 |
| fcc7a097-ec28-3492-af92-733181b7ca68 | -13.8457 | -47.9764 | 2025-09-04 14:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 6c1306f7-8067-3359-9cf3-e647b7590082 | -5.8292 | -45.3729 | 2025-09-04 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 227.7 |
| e9256d74-b547-39a4-9fe6-e28e48a6ab5b | -5.2632 | -43.7675 | 2025-09-04 14:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 2b8c8e35-64be-3300-930d-d4a6b60c9af3 | -7.6854 | -48.717 | 2025-09-04 14:30:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 99.3 |
| aefa065a-224d-345e-81d2-8005ec300bdd | -15.5848 | -50.3129 | 2025-09-04 14:30:00 | GOES-19 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 59.1 |
| e61cdf24-b178-3323-be2c-a85f84503e81 | -5.7187 | -45.1773 | 2025-09-04 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 851c69e8-26eb-3098-953c-0579fcd3d389 | -13.8651 | -47.9734 | 2025-09-04 14:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 67.5 |
| a0c20f18-c943-3ba7-b847-362fbdf82b79 | -5.7177 | -45.2905 | 2025-09-04 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 20e32f3f-60a1-39a9-bf15-0adf689e3cdb | -6.7928 | -44.4776 | 2025-09-04 14:30:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| f56d5bd9-1177-3514-a3e9-0994a3ece904 | -15.4567 | -52.9971 | 2025-09-04 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 412ad04b-59ca-3d0c-b79b-1931bae4d6a4 | -5.7 | -45.1786 | 2025-09-04 14:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 193.3 |
| 2f6f9606-0118-3e93-ad96-222d45dc9fb0 | -4.9049 | -41.7696 | 2025-09-04 14:30:00 | GOES-19 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 144.7 |
| f326b0d4-735b-3ce8-9ed2-12f0198bbc52 | -6.2318 | -42.4278 | 2025-09-04 14:30:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 123.8 |
| 7542b56e-a5d6-399b-9947-109fb0ef4ae3 | -11.834 | -51.4551 | 2025-09-04 14:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 10add317-a654-31cd-97f4-2b4e4bb678ff | -7.7409 | -48.7772 | 2025-09-04 14:30:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 138.1 |
| 00bc1f3d-6943-3420-9cb7-d586655ba2b7 | -6.2606 | -43.2961 | 2025-09-04 14:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |


[Clique aqui para ver as próximas entradas](README112.md)
