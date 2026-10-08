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

## Dados Diários - Página 207

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7b9ffd08-e641-3a2e-972c-db446ce2b669 | -6.03725 | -53.21589 | 2026-10-08 12:19:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 38.9 |
| d2c0e4e5-3821-3093-acc2-ac15de7763b5 | -1.20743 | -55.69426 | 2026-10-08 12:19:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ae5c0c1f-78d3-366b-a7b8-cd513a1196ce | -3.12337 | -54.1662 | 2026-10-08 12:19:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 421b9d2a-22c0-39b1-884e-ac3912d142a4 | -1.53834 | -54.54391 | 2026-10-08 12:19:00 | TERRA_M-T | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 141.9 |
| 662c1daa-cb48-30f7-8774-6f78f455e8ca | -3.01591 | -54.08144 | 2026-10-08 12:19:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 2eeef3b7-b158-3159-b3f7-4c3b47f59ea6 | -3.72386 | -54.22765 | 2026-10-08 12:19:00 | TERRA_M-T | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| f017ec00-a021-3775-ba77-67fadbee287f | -5.8793 | -53.62801 | 2026-10-08 12:19:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 11c0990f-9ad1-318d-a11a-032c7b40d65a | -3.70598 | -58.9346 | 2026-10-08 12:19:00 | TERRA_M-T | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| f4fe1d88-afa0-3b83-86aa-1acf24965468 | -1.19903 | -54.2063 | 2026-10-08 12:19:00 | TERRA_M-T | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| c0595c3c-3345-3faf-98a5-4c6cfa75870e | -6.20025 | -53.14465 | 2026-10-08 12:19:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 7f7ce2b0-fb5d-3f10-b082-8b6f34c849f4 | -1.32036 | -53.14455 | 2026-10-08 12:19:00 | TERRA_M-T | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| ef4408ab-c76f-3fca-8c6b-f9000d9933e6 | -3.43549 | -59.53429 | 2026-10-08 12:19:00 | TERRA_M-T | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 2000cb9d-8284-306e-af83-bc692d26ee35 | -2.39627 | -57.8861 | 2026-10-08 12:19:00 | TERRA_M-T | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 303da87a-47f8-39c6-b4e3-db5921985374 | -7.12047 | -46.95501 | 2026-10-08 12:19:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 9cd40940-c1ad-30f5-b79d-65580862b353 | -2.50189 | -56.07374 | 2026-10-08 12:19:00 | TERRA_M-T | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 36ae3dd2-77be-3a6c-a26f-13dea8be1937 | -3.10458 | -53.77555 | 2026-10-08 12:19:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 2a8fe325-64b9-35f1-a20f-f7851ba911df | -3.54857 | -55.52263 | 2026-10-08 12:19:00 | TERRA_M-T | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 7d480668-1bd0-3371-9ec0-9543f50b131a | -6.54512 | -49.85601 | 2026-10-08 12:19:00 | TERRA_M-T | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 132d8943-7be4-3aaa-9d5e-faee302420ed | -3.99892 | -56.24678 | 2026-10-08 12:19:00 | TERRA_M-T | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| a613759b-c72f-398c-ad19-afee56166335 | -6.02962 | -51.72898 | 2026-10-08 12:19:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| d860567a-d10b-3377-bf37-53f8adb2f2a1 | -6.23958 | -52.8475 | 2026-10-08 12:19:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 29.5 |
| c1e8b000-2d0c-3aeb-b19d-ce1ef3968566 | -3.87035 | -55.99948 | 2026-10-08 12:19:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 9ce68604-a463-38a3-8b3d-23e3abf1c739 | -4.54099 | -55.62016 | 2026-10-08 12:19:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 40a85d94-0de6-30f8-bc47-5f10f4a3c1bf | -1.46117 | -54.76903 | 2026-10-08 12:19:00 | TERRA_M-T | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| f2064bd3-4854-30d3-b694-5c3066efe8d3 | -10.28065 | -53.96181 | 2026-10-08 12:19:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 557121a0-645a-34cb-a6dc-8a7342fb6cab | -3.05519 | -53.92728 | 2026-10-08 12:19:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| c1db0051-ffe2-3552-a399-a8419e763911 | -5.95378 | -55.35386 | 2026-10-08 12:19:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 67100264-837c-3c01-82f1-1f7efc31959e | -2.50693 | -56.1639 | 2026-10-08 12:19:00 | TERRA_M-T | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 77e3f8ca-1377-3e9a-b4a1-d260ed76d6c4 | -3.32172 | -58.26419 | 2026-10-08 12:19:00 | TERRA_M-T | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 65a99b9a-a565-38a4-b0f8-0cb552fdcc91 | -3.16356 | -54.73211 | 2026-10-08 12:19:00 | TERRA_M-T | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 65cac0c9-6667-33b9-ad1e-8a4c4c234fa3 | -3.72621 | -55.96708 | 2026-10-08 12:19:00 | TERRA_M-T | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 665671af-618a-370a-821a-b5a1f32784f1 | -3.31477 | -54.70992 | 2026-10-08 12:19:00 | TERRA_M-T | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 9e873aa1-3a56-3bb6-9fca-fcb8491d9237 | -1.20868 | -55.68552 | 2026-10-08 12:19:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ec7502d9-495f-3e97-8824-4e11cab6fef4 | -3.92547 | -55.86446 | 2026-10-08 12:19:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| eb2dec71-f9e4-392b-ae2d-128211547066 | -3.00544 | -54.08966 | 2026-10-08 12:19:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 6edcdabe-8157-32d6-9241-8b93a21c1a3f | -3.0041 | -54.09911 | 2026-10-08 12:19:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 2f807ac8-d7fc-3440-afa5-0ae96de8f64e | -6.40502 | -56.40956 | 2026-10-08 12:19:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 345534ba-81d6-3efb-bbd0-2806fce33cdd | -5.69638 | -53.45263 | 2026-10-08 12:19:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| bc038ce2-fbd7-3e02-a335-2d06d42baeee | -4.12378 | -59.87287 | 2026-10-08 12:19:00 | TERRA_M-T | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 60036bce-95bf-3cfd-aa41-b2f1fbaf2c55 | -4.12195 | -59.88549 | 2026-10-08 12:19:00 | TERRA_M-T | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 8d181f15-8867-3753-9dbc-1a480a317259 | -4.26999 | -54.86602 | 2026-10-08 12:19:00 | TERRA_M-T | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f65fde14-2c95-3096-a8f9-5dff66af4358 | -3.40681 | -57.98515 | 2026-10-08 12:19:00 | TERRA_M-T | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 32c29f7a-f545-3a76-9edc-6c0ee7a1fdba | -5.91679 | -53.88636 | 2026-10-08 12:19:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 0a7f764b-4a38-3353-b55b-07084199ce49 | -1.52818 | -54.55167 | 2026-10-08 12:19:00 | TERRA_M-T | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| a224c220-d258-36d8-b5fc-f39ae909cd8e | -4.93258 | -55.85804 | 2026-10-08 12:19:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 714656e6-1be6-3e8c-8f47-410b05e70311 | -1.29587 | -54.55609 | 2026-10-08 12:19:00 | TERRA_M-T | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| c85e1584-ee61-3c59-86e8-c1a685d1124b | -8.18061 | -54.72958 | 2026-10-08 12:19:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 5a0c1658-b3dc-364b-8d78-6b49ecd9bd11 | -7.75356 | -54.94706 | 2026-10-08 12:19:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 686b4647-f335-3de1-91e8-2cd7087b7efe | -5.97034 | -55.36529 | 2026-10-08 12:19:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 284823a3-b539-3ac3-9bc1-61c68a35dc3c | -1.10421 | -54.15948 | 2026-10-08 12:19:00 | TERRA_M-T | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| c80a1580-70ea-386a-a186-f3fa7ecde667 | -2.51197 | -56.25434 | 2026-10-08 12:19:00 | TERRA_M-T | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 2119ae99-b046-3ba4-a892-dfe92a8cb3b4 | -3.2631 | -54.02681 | 2026-10-08 12:19:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 2025debe-b878-3162-a380-9dda5b4d51dc | -3.01282 | -53.90566 | 2026-10-08 12:19:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| bc33c9d8-77ca-3e04-9ea4-2e6fb5aef96a | -10.44092 | -47.2591 | 2026-10-08 12:19:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 1f17f157-0d45-31b9-a25c-fa937d2cf20d | -5.2993 | -60.09945 | 2026-10-08 12:19:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 39161eda-5ddf-3045-8a87-32db4ecb1fb7 | -3.11558 | -54.15548 | 2026-10-08 12:19:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| f66934f9-6f77-380e-aff0-bed79baee54d | -1.53072 | -54.53376 | 2026-10-08 12:19:00 | TERRA_M-T | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| c6a886d5-7353-31dd-b9cb-0c5699a22672 | -3.12174 | -53.7879 | 2026-10-08 12:19:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 8f8c856f-a7b6-31d5-8a97-61e8b467d430 | -3.36805 | -58.1835 | 2026-10-08 12:19:00 | TERRA_M-T | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 254c8216-37fa-3d75-b557-a9ea9ef1139a | -4.66948 | -56.21999 | 2026-10-08 12:19:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 85392836-1e8e-3dd5-97cd-f12510bbb5bd | -10.06381 | -55.29272 | 2026-10-08 12:19:00 | TERRA_M-T | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 7030f5ea-b2bc-3664-aca6-98da7883d682 | -3.08794 | -53.96111 | 2026-10-08 12:19:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 8d7a255f-1a68-3b90-a221-3ef93444f3d0 | -3.36169 | -58.18688 | 2026-10-08 12:19:00 | TERRA_M-T | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 2517cdfa-76a6-37eb-a125-f5f15f7060ff | -3.09724 | -54.287 | 2026-10-08 12:19:00 | TERRA_M-T | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 8cf67e96-45b1-3317-a7b9-a9c8eff97620 | -3.45267 | -58.06232 | 2026-10-08 12:19:00 | TERRA_M-T | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 21.2 |
| e7fe1db6-2fa8-324e-88f9-9d82729f6cd0 | -4.1571 | -55.13869 | 2026-10-08 12:19:00 | TERRA_M-T | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 7516e170-ac2c-38c5-8737-7ebba3dc0ac2 | -1.1055 | -54.15038 | 2026-10-08 12:19:00 | TERRA_M-T | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 79ad51f5-ff27-3025-9bf3-c6d4a04df53e | -3.01322 | -54.10036 | 2026-10-08 12:19:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 78f21b12-f55a-3119-a992-c60beffb2b48 | -3.01456 | -54.09091 | 2026-10-08 12:19:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| e3118f6e-c9c9-3b63-967e-40578469b0dd | -5.98998 | -55.36476 | 2026-10-08 12:19:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 968cf691-9028-38b1-9521-37b933d986e2 | -2.81396 | -57.04942 | 2026-10-08 12:19:00 | TERRA_M-T | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2767bfb8-bed9-3e57-88c2-186a4e601b99 | -3.98254 | -56.11062 | 2026-10-08 12:19:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| ae357a2e-c6ff-31a0-a377-d3751fc0d66b | -3.31605 | -54.70082 | 2026-10-08 12:19:00 | TERRA_M-T | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 25291377-5d88-38f7-b94b-a8796b8e55b9 | -4.93883 | -55.81407 | 2026-10-08 12:19:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 09e2cfa9-14bb-33ad-8cec-8e42d827561d | -2.99887 | -57.74705 | 2026-10-08 12:19:00 | TERRA_M-T | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| cda5ca5a-562d-39ce-9c84-33d4f8418045 | -3.56735 | -54.48595 | 2026-10-08 12:19:00 | TERRA_M-T | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 4a4b79fb-5eb3-3b78-870a-a61021b7dcef | -7.23327 | -55.10817 | 2026-10-08 12:19:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 131.6 |
| 72bfac57-cac4-368e-b9f6-c33ff45af264 | -3.31462 | -54.05003 | 2026-10-08 12:19:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 0a8acd51-9029-3f61-ad4f-d47fce4faa90 | -2.52079 | -56.25555 | 2026-10-08 12:19:00 | TERRA_M-T | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 77d291dc-2dfa-3f9d-a788-9ed93cc3ffdf | -1.80754 | -57.11441 | 2026-10-08 12:19:00 | TERRA_M-T | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| c8f820a4-ea9a-3f5a-b2c9-19fb4eef9984 | -3.05653 | -53.91763 | 2026-10-08 12:19:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| e08805b8-fc28-3508-91b0-6d83c2ebd3da | -11.85262 | -48.03614 | 2026-10-08 12:19:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 7f679780-8d7e-3b56-bc8e-a8a40f6c93f7 | -3.61179 | -54.56446 | 2026-10-08 12:19:00 | TERRA_M-T | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 19e6c434-9769-3d53-b4d3-1eb25bb188cb | -11.34884 | -51.87405 | 2026-10-08 12:19:00 | TERRA_M-T | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 67.4 |
| fa628354-aa1e-3f11-817e-0f9c0302db46 | -3.26175 | -54.03638 | 2026-10-08 12:19:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 15ef788b-3ece-3008-a54a-6ceeb064fb9f | -8.14361 | -50.01452 | 2026-10-08 12:19:00 | TERRA_M-T | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 8960e9e8-fc86-32a0-9265-1b8545aa6f1c | -1.91057 | -55.50287 | 2026-10-08 12:19:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 6f590b45-58bd-3a06-9e85-d9d8ec1fc75f | -3.04042 | -54.1004 | 2026-10-08 12:19:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 015b573b-84aa-344c-b025-d83450dd752b | -7.67792 | -50.49392 | 2026-10-08 12:19:00 | TERRA_M-T | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 40.2 |
| c74a091f-602c-3e08-954f-9f6f8329e118 | -3.47785 | -55.43473 | 2026-10-08 12:19:00 | TERRA_M-T | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| bac8428a-c88f-3739-b6e8-bd1b78218e02 | -5.88075 | -53.61733 | 2026-10-08 12:19:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 738820ef-33d6-3286-a34e-520ca8d7e56d | -2.98719 | -54.08715 | 2026-10-08 12:19:00 | TERRA_M-T | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 35b67e2c-0768-322e-9645-8afe6889065a | -3.94692 | -56.02789 | 2026-10-08 12:19:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 130f6c6c-1365-3b79-a910-a2e346481254 | -6.04075 | -51.73045 | 2026-10-08 12:19:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 1fcb8750-6a35-3e8a-9652-bc7b35b7d1dd | -3.55502 | -59.47754 | 2026-10-08 12:19:00 | TERRA_M-T | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 9ab24488-e9d9-37b4-bcbd-10d3707f9f9c | -5.7373 | -53.46402 | 2026-10-08 12:19:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 24.6 |
| b697039a-68d7-30e5-b4db-66e60e852c31 | -1.29458 | -54.56501 | 2026-10-08 12:19:00 | TERRA_M-T | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 621f0ea3-fdb2-3464-82b6-15ef07d25e30 | -3.22852 | -57.87733 | 2026-10-08 12:19:00 | TERRA_M-T | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 611c6a74-f266-3430-be63-b0ce9e402a9d | -6.78145 | -50.64252 | 2026-10-08 12:19:00 | TERRA_M-T | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 79926a13-4060-34a0-9203-32513c39e9bb | -4.77463 | -55.73403 | 2026-10-08 12:19:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |


[Clique aqui para ver as próximas entradas](README208.md)
