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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1811bcf2-7b70-3f3e-87a4-6e9d736ed0f9 | -6.20968 | -43.50162 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f5389ba4-ddae-34ab-b435-b986b352570f | -5.71363 | -45.41994 | 2025-09-10 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8b1b3def-c92f-38ac-93e5-d01603a080f4 | -5.58309 | -45.0415 | 2025-09-10 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 7ece2ccf-0d63-38bd-baed-c326506f254c | -5.40568 | -43.44122 | 2025-09-10 04:40:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5eb77bab-0f1c-3a8f-aa22-24b9bfbc4268 | -5.72184 | -45.41662 | 2025-09-10 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3ec549a1-3fce-3366-8d4e-ce52f888eac2 | -5.80655 | -45.67654 | 2025-09-10 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c5e5804b-8c11-37d8-bd1e-e154086f6179 | -4.7226 | -46.80625 | 2025-09-10 04:40:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ffa0577b-2e39-32ab-807d-c4c6b72de08e | -5.74427 | -47.46041 | 2025-09-10 04:40:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3a59d643-ded6-3f92-bbb0-c93b12efc40f | -4.32849 | -48.39623 | 2025-09-10 04:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d1661db4-5861-393f-8b3f-d3d9a130b5f8 | 0.83178 | -51.18336 | 2025-09-10 04:40:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f073ed0-5499-3fbc-8564-860b74861e02 | -5.66268 | -47.48931 | 2025-09-10 04:40:00 | NPP-375D | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ba7b7e7-d970-3abe-a69e-bd0f523ea9fb | -5.62113 | -45.01073 | 2025-09-10 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d1d1926e-f9b7-3cc3-80ce-bcd801c392cd | -5.22715 | -43.68771 | 2025-09-10 04:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 746f77bb-30cd-3c92-a9b6-94dbb41851cc | -5.74597 | -47.47198 | 2025-09-10 04:40:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 385d231b-250d-3247-a0f0-d7d61ae6f1a6 | -5.91645 | -45.81691 | 2025-09-10 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c8042ffa-8b52-3006-a498-1d56230c1eac | -4.20288 | -55.13638 | 2025-09-10 04:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 80ee450c-454e-33f9-9443-e894433cde0e | -6.23228 | -43.49684 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ae99ae2d-5aa4-3ffa-8eac-77fe2326985d | -5.66797 | -43.35577 | 2025-09-10 04:40:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c4ff14d2-a245-390a-af4a-cd523622fea9 | -5.71432 | -45.41542 | 2025-09-10 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| be20211e-adf3-39b9-8574-83d792bf160d | -6.18474 | -43.40245 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e4a6436e-177c-3ccf-840c-ca5136509c16 | -6.17674 | -43.39687 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4c74ef0a-0492-3f71-b7c3-6ef1c9762896 | -5.74254 | -45.256 | 2025-09-10 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f63c45da-bbd8-37f5-89a3-90849ca34d18 | -5.67773 | -43.34905 | 2025-09-10 04:40:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0f75a06d-2a03-322d-95d2-7bfb0b3685f2 | -5.74539 | -47.47567 | 2025-09-10 04:40:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9be4b7d1-3a74-3a1d-99ce-15aa0fb88894 | -5.79647 | -43.88393 | 2025-09-10 04:40:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1947cc3c-95f7-37dc-ad93-eb9877873209 | -5.84656 | -43.8611 | 2025-09-10 04:40:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 69f93be6-f03f-38a3-b393-9a10f6dfab34 | -5.92577 | -46.17442 | 2025-09-10 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ade8a638-0640-3194-808f-926f4518af9a | -5.50553 | -42.67269 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 29dcfbc7-7bdf-3650-ac33-c20ac50252d7 | -4.08932 | -50.69178 | 2025-09-10 04:40:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7a53840b-ff3e-33e0-bd33-628fb1087ce3 | -6.06248 | -43.13582 | 2025-09-10 04:40:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| af1ea609-bdde-38d3-b17d-7c0338d19229 | -5.64386 | -43.91813 | 2025-09-10 04:40:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8b1130fd-7911-32d1-a766-1e29a2f9eac7 | -6.17457 | -41.05027 | 2025-09-10 04:40:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 08d82d1e-4795-38a4-aaf9-602f8ce7d6d1 | -5.22598 | -43.69539 | 2025-09-10 04:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c8aa902d-85c6-3f56-bf97-5172f9f0fa70 | -5.74654 | -47.4683 | 2025-09-10 04:40:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 09814ec8-58ca-3c56-b39b-66f136bf38a2 | -5.96641 | -45.81116 | 2025-09-10 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f1546239-7698-3085-95bb-9de0944fc61e | -5.80397 | -44.85287 | 2025-09-10 04:40:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d7e4a35d-59ee-3fb8-8b60-6fa647a1c226 | -6.2047 | -43.29558 | 2025-09-10 04:40:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 872bc8d0-e435-3aad-849d-65b670c907e7 | -4.89377 | -42.68606 | 2025-09-10 04:40:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 258e6236-17cf-3656-9e70-5e237045f338 | -6.20107 | -43.32053 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 22991488-3558-353c-a277-88a6cdd80083 | -5.48509 | -42.65616 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b47b2588-c2ad-3060-958e-a68c31a97e2e | -5.8095 | -45.67393 | 2025-09-10 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 76f337a4-bc81-31c9-bc7a-e5f965054aad | -5.50804 | -42.67075 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 60cd5e27-5379-3a44-949c-109d9f3b50ee | -5.72481 | -43.89661 | 2025-09-10 04:40:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cd0be022-8923-3f5d-b6f8-ec7d0fecf372 | -5.42476 | -43.98725 | 2025-09-10 04:40:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b5f8cca7-0a17-3c92-9c98-39a933564ba4 | -5.99443 | -43.3255 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f423b0d0-9632-3156-8acc-e3d5e7aa699b | -5.67713 | -43.3531 | 2025-09-10 04:40:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d7275f01-bf86-32b1-be6b-51ac984d64fb | -5.74254 | -47.47147 | 2025-09-10 04:40:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 287c705f-b419-3b79-b92a-78b7c26b3699 | -5.55835 | -45.17659 | 2025-09-10 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0f3495ad-ec6f-3eaa-b7fb-eeaa95568956 | -5.7256 | -45.41722 | 2025-09-10 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 965a1293-f70c-3fb1-ab5a-57b4d0a49382 | -5.56602 | -45.11781 | 2025-09-10 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f7b6eb04-54e4-377c-b1ca-af437cada509 | -5.64495 | -43.92231 | 2025-09-10 04:40:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b23a326f-33a0-3fb6-af99-664e8fe3b113 | -4.35864 | -50.6243 | 2025-09-10 04:40:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7057b6a0-2730-3459-bccb-58098011d124 | -6.17969 | -43.3765 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ff1c9d6f-70a4-383d-b42f-ce2ee849dda2 | -3.79943 | -52.25827 | 2025-09-10 04:40:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3cab37b4-3080-345f-a086-e2b09d986207 | -6.24846 | -43.40159 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3e6d127b-bc73-31a4-b91d-2eac7eda9798 | -5.58615 | -45.03436 | 2025-09-10 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| e2813e9d-1d50-3237-b71a-b3d004b10937 | -6.00627 | -46.6785 | 2025-09-10 04:40:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b49cf14a-d38c-392c-80f6-6465fea7225b | -5.57927 | -42.9199 | 2025-09-10 04:40:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| cfddb40d-a051-369d-8150-200b37f66b89 | -5.56771 | -45.1159 | 2025-09-10 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e12416f4-a960-3d49-88a2-4fb76f51e8de | -6.46953 | -41.79643 | 2025-09-10 04:40:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e37deb55-348a-3308-a2fa-ea207e6feb10 | -5.93674 | -45.95656 | 2025-09-10 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 91c5d869-a420-3cd1-afab-ab3668cc4db6 | -3.51633 | -52.74904 | 2025-09-10 04:40:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9f1d3be1-e774-3626-afa9-c867d6869ba9 | -5.84713 | -43.85735 | 2025-09-10 04:40:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 22449a1b-f05b-3b2d-a5df-fa615915fbe2 | -5.70987 | -45.41934 | 2025-09-10 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ae1fb538-b217-35dc-bafc-c7550b8f8f04 | -6.17538 | -43.3758 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5efc33e3-ec5d-3ae6-92d7-bf6c0e4ab193 | -6.16128 | -43.3819 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 944af3b1-d999-3f93-b91b-8b6be4550ee8 | -6.19333 | -43.40397 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 27181352-6f1e-3479-bdb2-d022c983fd1a | -4.48072 | -48.11648 | 2025-09-10 04:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f2397dc7-a862-3385-a7f1-616ecf113794 | -5.42034 | -42.81637 | 2025-09-10 04:40:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8c02d5ad-8b66-3090-b1ff-20fc17ac0032 | -5.91883 | -45.75031 | 2025-09-10 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b3ada631-f7dc-31c9-96f0-eb8886658a11 | -2.96017 | -48.74938 | 2025-09-10 04:40:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ecd41a6e-0303-3d67-bede-027c6efe3547 | -5.66416 | -43.90638 | 2025-09-10 04:40:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 67c2b9d0-6557-3624-9898-d5405919b9f3 | -5.91383 | -45.75848 | 2025-09-10 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cc5607ee-e4dc-3fc5-98b1-41f4170aa3aa | -5.10377 | -43.05132 | 2025-09-10 04:40:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 184d158c-9404-3948-b177-d088bfcd0266 | -5.91006 | -44.9698 | 2025-09-10 04:40:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 03d71e9f-537b-36ba-8053-544c21d4463f | -1.19852 | -46.15439 | 2025-09-10 04:40:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6eaf3e1-0053-3196-8ddc-cccf70959a31 | -3.63881 | -49.20699 | 2025-09-10 04:40:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e5a6f29f-7313-3c45-9e66-dfce38afbcd3 | -6.25069 | -43.40338 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9fe67d29-af43-38ae-891b-da44b1f6ea75 | -6.25747 | -43.4169 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| e50e1af5-2a68-372c-a85c-c2dfa40b23c6 | -5.57775 | -45.03803 | 2025-09-10 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| f200aba5-4d4e-392b-b989-ec2d1798a5fb | -6.34578 | -43.65324 | 2025-09-10 04:40:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b0f25b7c-8927-30b6-b129-3ba241828562 | -5.53303 | -42.65641 | 2025-09-10 04:40:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 2289c99e-2d85-3655-b11f-86420684b0df | -4.97695 | -48.9425 | 2025-09-10 04:40:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 12debfc0-3038-301d-990c-854bab2d0ab9 | -5.58545 | -45.03912 | 2025-09-10 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 5819b6ae-8d9b-3895-a630-2cd21f3f75c3 | -5.71808 | -45.41602 | 2025-09-10 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 918ef3d8-7d36-3fb5-b718-867aaca7d29f | -6.20697 | -43.54935 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7dd7302b-bbc3-39e5-a4b3-4ed942234ecb | -6.0554 | -43.31215 | 2025-09-10 04:40:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 78003744-91af-372e-a7dd-e9f603be8845 | -5.8199 | -43.7248 | 2025-09-10 04:40:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8f15911a-c96f-33b9-99cd-8605f665dbe6 | -5.67673 | -45.46039 | 2025-09-10 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ae2d9486-661d-3bea-bbb7-a67792da6553 | -6.4489 | -43.57394 | 2025-09-10 04:40:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cb022221-8192-3ecb-8054-e2ed5786a3d1 | -6.20034 | -43.29502 | 2025-09-10 04:40:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c2c1db94-f59c-3035-a152-f05d5d99bc09 | -4.1985 | -55.1368 | 2025-09-10 04:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b597f2f8-e832-3d99-81ed-34ef4d6ca712 | -6.19633 | -43.50314 | 2025-09-10 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a9229ca4-1ade-356d-8622-1521bb43c60b | -3.86208 | -52.00625 | 2025-09-10 04:40:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2d79f291-5eac-3d8d-8d12-1353ae876579 | -5.4507 | -43.4598 | 2025-09-10 04:40:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5b92c40a-e2fb-3042-8923-604e8d54cdb3 | -5.73901 | -45.27908 | 2025-09-10 04:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e6aba2d1-e5db-39d5-8a94-f9ceba2e105d | -6.27965 | -44.79329 | 2025-09-10 04:40:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a15d15ba-4059-3bc4-98f0-6d07cb918bd3 | -5.53359 | -46.49719 | 2025-09-10 04:40:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cf1b9db5-a230-35d6-ab7a-e0860322675a | -1.96758 | -48.43768 | 2025-09-10 04:40:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 36187242-e37a-3cba-85bf-c00930deb080 | -5.5843 | -42.91626 | 2025-09-10 04:40:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |


[Clique aqui para ver as próximas entradas](README52.md)
