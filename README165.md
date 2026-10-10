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

## Dados Diários - Página 165

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6633a7c3-f2fe-330a-87f8-18dfadabc6b3 | -3.2766 | -53.8602 | 2026-10-10 15:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 129.7 |
| 74766b29-2bd4-391a-bba4-53f63d0513b3 | -1.4487 | -48.9739 | 2026-10-10 15:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 4382bda1-ec2c-3220-b72b-1a32c969accd | -12.8303 | -44.6239 | 2026-10-10 15:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 244.8 |
| 8341772d-ee8e-3f5f-be38-8c506c9f7355 | -10.9575 | -45.389 | 2026-10-10 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 351b37ff-eef0-3354-9c70-08b17fd94a78 | -4.1039 | -54.0164 | 2026-10-10 15:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 5ef0d04f-c1b1-38e0-b5c5-90c5abe17c3a | -10.9957 | -45.3839 | 2026-10-10 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 134.6 |
| 5c6bc06c-7e69-320d-b7e3-47bd0cf13dac | -3.022 | -59.1462 | 2026-10-10 15:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 2ac7906a-a404-30e0-97cd-0515001e1e39 | -1.1992 | -55.6712 | 2026-10-10 15:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 2d2a6ff9-5f75-3a63-b4c3-11c833e6df3e | -1.3264 | -56.4176 | 2026-10-10 15:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 21dfc104-8eaa-3bbc-8c34-fae23fc0c135 | -2.8247 | -57.606 | 2026-10-10 15:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 82bbb68c-cfbb-3ffe-9c7e-6eef4fdc651b | -3.0192 | -53.887 | 2026-10-10 15:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 7bd58f19-df71-38c9-9abb-9d8b7919502c | -1.3264 | -56.398 | 2026-10-10 15:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 106.1 |
| ca152455-0e7f-3070-8ecc-6030b155d2fa | -10.8591 | -50.6692 | 2026-10-10 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 67.1 |
| d1e90b5e-caa3-3580-9989-8bd629e4957f | -2.4031 | -57.9041 | 2026-10-10 15:10:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 53.2 |
| aaaf3df9-0c41-3491-b829-d547d8876b39 | -3.1284 | -54.1857 | 2026-10-10 15:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 57b160a7-1f87-3fd5-b8fa-a559d1e2ee7d | -3.0219 | -59.1653 | 2026-10-10 15:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 4dee4219-d9aa-352e-a528-808fca5eab73 | -6.5519 | -61.4177 | 2026-10-10 15:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 8a0e0127-c3c5-3a08-857d-32c2ccded175 | -3.2393 | -54.0222 | 2026-10-10 15:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| db5f329d-85de-3596-a8fa-a7a7ece43733 | -2.8247 | -57.6254 | 2026-10-10 15:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 69.6 |
| e7535842-4125-3906-ac21-f4f6c03567dd | -11.5998 | -43.6226 | 2026-10-10 15:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 226.4 |
| 8ed87d85-13d9-3cf9-b776-c66dd681c86e | -13.7624 | -45.3519 | 2026-10-10 15:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 194.4 |
| 0cf2d870-fbfe-3bf3-bf00-e42b4afd2611 | -3.053 | -54.7679 | 2026-10-10 15:10:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 171.8 |
| 9b976e5a-ff62-3c39-8411-e1af5fb7e201 | -1.3447 | -56.4175 | 2026-10-10 15:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 162.7 |
| ca43619b-76c8-3be4-b01f-eca86e19dc14 | -1.6579 | -55.1912 | 2026-10-10 15:10:00 | GOES-19 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 119.7 |
| 0655135c-4397-35ef-bfe5-558125c5728a | -2.5552 | -55.5731 | 2026-10-10 15:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 101.8 |
| 1d62de69-47af-3e0c-81d3-aee417e04af6 | -2.4259 | -55.9901 | 2026-10-10 15:10:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 4c9ef0df-5a43-3ba8-a973-29d29ab30369 | -2.5689 | -57.4163 | 2026-10-10 15:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 7ad96d3e-1f04-380d-971c-429cfc23dd59 | -3.1285 | -54.1657 | 2026-10-10 15:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| df2d142d-949e-325f-a09e-9d775b0f65af | -9.1257 | -67.8322 | 2026-10-10 15:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 3d77acca-e22b-35d8-93de-d1d53504a57e | -1.2088 | -48.9133 | 2026-10-10 15:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| c7117814-d90d-37e6-97a9-7617f37fed73 | -3.0008 | -53.8874 | 2026-10-10 15:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| eb71ea69-8a01-30e3-b169-02379a372580 | -2.5171 | -56.1262 | 2026-10-10 15:10:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 5263c38b-d00d-3377-8c71-e99288197a48 | -1.6578 | -55.211 | 2026-10-10 15:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 9541af39-4ccf-3294-8c84-12d7964ab9e4 | -10.9766 | -45.3865 | 2026-10-10 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 68dcea96-3b9a-3866-874b-02cf2af484cd | -3.2765 | -53.8803 | 2026-10-10 15:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 126.4 |
| f1a17054-2b50-3304-ab4d-f0dcbe614bfd | -1.2175 | -55.6512 | 2026-10-10 15:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 716b82ff-8ef3-32a7-a63b-964d86a1bd90 | -1.8986 | -53.9899 | 2026-10-10 15:10:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| e52ec326-06e5-3774-a8d0-5d41b5e17108 | -3.1114 | -53.7839 | 2026-10-10 15:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| a1eb4b3b-2133-3475-8bbc-ea806a8cfa34 | -1.2907 | -55.7295 | 2026-10-10 15:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 127.6 |
| 6a244eef-c321-370b-8bf7-80c436af078f | -14.7513 | -48.2135 | 2026-10-10 15:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 168.2 |
| 956825b9-e173-37ca-a7b8-dde54a1134ed | 1.345 | -56.1426 | 2026-10-10 15:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 53a52b70-2f60-3c09-ac02-28b24e1f65fb | -8.9119 | -45.1605 | 2026-10-10 15:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 714bcd68-1ac4-35cc-bce5-f6a77381d3e0 | 2.0713 | -50.8799 | 2026-10-10 15:10:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 74b79a04-4753-336a-b998-2af74e3126b4 | -2.8491 | -49.8763 | 2026-10-10 15:10:00 | GOES-19 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| d7b5a647-934f-3fae-9fca-5deebf04a34b | -2.4442 | -55.9897 | 2026-10-10 15:10:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| f638cb1e-e6bb-3bcf-a89d-929a625e9306 | -8.3045 | -45.4525 | 2026-10-10 15:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 74.9 |
| b9402bc0-0310-3a09-821b-c89950399649 | -2.8899 | -54.0711 | 2026-10-10 15:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 54d774f6-2989-345e-95fc-daa3d2281611 | -14.7318 | -48.2167 | 2026-10-10 15:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 159.4 |
| de6d92bc-97e2-3c03-90da-a5f16616ede3 | -1.6395 | -55.1914 | 2026-10-10 15:10:00 | GOES-19 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 195.3 |
| de1b9b88-47f6-319a-be16-8202b4c21c7c | -3.1602 | -50.5812 | 2026-10-10 15:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 93.9 |
| cb4f5d53-4991-3a09-aae6-8b440c33c98e | -1.5307 | -54.5159 | 2026-10-10 15:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 451250fd-15ac-33af-91db-325f0061cb79 | -2.9817 | -54.1091 | 2026-10-10 15:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| e02cf3c9-a9bb-3bf9-b184-208c75aed9b4 | -10.9197 | -45.3712 | 2026-10-10 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 157.0 |
| 2c79bc0e-8b01-3b13-8ccb-861212adc1c6 | 4.2067 | -60.6106 | 2026-10-10 15:10:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 78.5 |
| a2204a02-14c2-382a-b60c-3b27e770ae3a | -3.0531 | -54.7479 | 2026-10-10 15:10:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 104.2 |
| cede5c65-ed9c-3486-a4e4-ee29efbe69e1 | -8.9311 | -45.1355 | 2026-10-10 15:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 91.6 |
| d5d57abb-3525-3953-a150-4d6ec76d1dd0 | -9.1613 | -68.2383 | 2026-10-10 15:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 1b8a0a53-7fc7-3aaf-81be-aeafa2f23dc3 | -14.7323 | -48.1943 | 2026-10-10 15:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 609afc74-f0cf-3b40-b5db-b8288edf6642 | -2.4806 | -56.0678 | 2026-10-10 15:10:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 37f0959a-0feb-3019-a580-3bc32340781a | -2.3834 | -51.2887 | 2026-10-10 15:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| c045ffd3-7863-3674-8b31-fd0598c0a559 | -3.0252 | -57.9319 | 2026-10-10 15:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| b5ce120d-e934-3b60-8ca2-00b4aee94d8d | -3.188 | -58.6241 | 2026-10-10 15:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 82.7 |
| a9cd87e1-bd90-315e-9adb-363181f390ce | -3.2533 | -50.3899 | 2026-10-10 15:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 6c4b02f6-bdf4-3715-9e21-595ff582334d | -1.3447 | -56.3979 | 2026-10-10 15:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 178.5 |
| fff464e5-34be-3c4c-a0b2-fe25b2d3c3b7 | -11.619 | -43.6196 | 2026-10-10 15:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 192.9 |
| 26ce84e4-48e5-32e6-b0d2-3f27340e4bd4 | -2.6079 | -56.4782 | 2026-10-10 15:10:00 | GOES-19 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 737a25f8-a8f5-39b1-ae96-55660fafb83d | -9.9208 | -44.7893 | 2026-10-10 15:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 56bb7dc1-4c31-3b91-ba6d-7ce43a38b806 | -15.1088 | -46.9343 | 2026-10-10 15:10:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 826ecded-ec37-36ac-bcc6-bb441360b40f | -10.7302 | -45.305 | 2026-10-10 15:10:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 301.2 |
| 9ab25c42-abb1-3539-b05d-145384a1b52a | -2.4806 | -56.0875 | 2026-10-10 15:10:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 7d247fd6-0b20-3f58-ab38-3fbec4ac1d5a | -3.2031 | -53.842 | 2026-10-10 15:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 3d61f5d0-949c-3e83-9a0c-88dcc6668281 | -8.76 | -45.3 | 2026-10-10 15:15:00 | MSG-03 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 049ce8d3-2bce-358f-878e-841b5297bde2 | -7.52 | -39.38 | 2026-10-10 15:15:00 | MSG-03 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 92a8b61d-73d7-374c-b1bb-3e7f5b576502 | -7.12 | -44.92 | 2026-10-10 15:15:00 | MSG-03 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eedb1cc8-e68b-3617-add6-09a75ce07780 | -3.29 | -50.43 | 2026-10-10 15:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44e79e36-29bf-3acf-92c1-baa0ab75d111 | -3.26 | -50.43 | 2026-10-10 15:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ea33d46-3e93-33b4-89ba-28b195912ed2 | -10.26 | -36.43 | 2026-10-10 15:15:00 | MSG-03 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 825f4bac-733d-3236-bf07-5935e17ce6ef | -11.11 | -44.14 | 2026-10-10 15:15:00 | MSG-03 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7bc0986f-3808-3f05-9f5c-ee85d747d8f2 | -7.12 | -44.87 | 2026-10-10 15:15:00 | MSG-03 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 00fb1075-0ab8-328c-82c9-57836bfda741 | -7.76 | -45.02 | 2026-10-10 15:15:00 | MSG-03 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3ce074c8-dc43-3891-a9fa-3cd666267410 | -7.76 | -44.97 | 2026-10-10 15:15:00 | MSG-03 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 723fb121-fe1a-31cd-bd7d-dabbffdc9463 | -7.15 | -44.92 | 2026-10-10 15:15:00 | MSG-03 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f26076d0-5001-39ff-ab4c-75ab0b7b0897 | -18.64 | -41.33 | 2026-10-10 15:15:00 | MSG-03 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 53976c1e-f2e3-3088-8ceb-f208889d627b | -2.8247 | -57.606 | 2026-10-10 15:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 304d6505-06d9-38ba-bbd9-dd67f881cdda | -9.9208 | -44.7893 | 2026-10-10 15:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 136.5 |
| 95610584-1a83-3698-a0fb-46bb1e08c567 | -2.8247 | -57.6254 | 2026-10-10 15:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 7a814fd7-0a30-3775-b7a5-ea5947c59da8 | -2.3889 | -56.1285 | 2026-10-10 15:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 85db04cc-f9ad-3bb2-bf03-c016483a3bd6 | -9.9384 | -44.8791 | 2026-10-10 15:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 178.2 |
| f83e6d6b-4a22-3267-9101-d4a1314b97e9 | -3.2086 | -57.8313 | 2026-10-10 15:20:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 98.5 |
| 28eb8c97-3d69-34fe-a316-30d72a175997 | -3.5893 | -59.0773 | 2026-10-10 15:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 63f1ef41-d9a5-3f5a-9e0c-3cefa8eed129 | -11.619 | -43.6196 | 2026-10-10 15:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 220.0 |
| c719e139-c4ee-3c1b-b5c5-9b5ccc4c8273 | -3.053 | -54.7679 | 2026-10-10 15:20:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 186.8 |
| 4140708a-e8c1-3076-9287-abb174f9740d | -2.4031 | -57.9041 | 2026-10-10 15:20:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 042b652f-4bff-3ad5-86f2-18874988d9d0 | -4.104 | -53.9963 | 2026-10-10 15:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| e3866ab2-c81a-3771-9fb5-977fc42ddf1a | -9.1613 | -68.2383 | 2026-10-10 15:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 074c34ee-9e35-3a9b-be9c-c3633a098053 | -12.8321 | -50.9981 | 2026-10-10 15:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 64.3 |
| aa74c2ef-b120-3e24-b804-d239991a9307 | -3.0219 | -59.1653 | 2026-10-10 15:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 6850597c-3d6d-33e3-b7d3-02dd4d54842c | -3.2086 | -57.8119 | 2026-10-10 15:20:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 192.2 |
| 741cdbde-bfbb-3b7f-886f-042da9edc2f0 | -1.8986 | -53.9899 | 2026-10-10 15:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 6fc8c8fd-704b-3284-8855-1b75203a2452 | -8.9308 | -45.1584 | 2026-10-10 15:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 118.8 |


[Clique aqui para ver as próximas entradas](README166.md)
