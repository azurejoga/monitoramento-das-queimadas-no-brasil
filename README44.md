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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 80431966-4722-3bde-9de6-c5fde80ab48f | -12.30303 | -47.26374 | 2025-10-29 04:25:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c6685db4-3620-3c00-ba9f-12b76738d22c | -13.01945 | -48.77354 | 2025-10-29 04:25:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 867b50c3-69aa-3225-96d2-b2f2fc50e2ed | -16.19115 | -45.06805 | 2025-10-29 04:25:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 592dbcc7-22b7-3d72-8e4f-79ec0cdce71c | -12.05311 | -47.8271 | 2025-10-29 04:25:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 62558340-8748-35e4-b603-565553f5fe9d | -15.57477 | -43.54255 | 2025-10-29 04:25:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 27dddc4b-3d48-3a81-881d-f23c6868df48 | -18.92626 | -45.03212 | 2025-10-29 04:25:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 5ada756f-b92f-3941-83fa-85d6adeab614 | -13.55263 | -47.35186 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4e038b80-831b-3d84-9fa9-a5df4b461cf2 | -12.32072 | -48.04616 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3fd37d58-a24e-3881-89a7-bf5fe9924c50 | -10.97447 | -50.2515 | 2025-10-29 04:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 477a1dfc-b522-3638-977a-c1179c10174b | -18.77743 | -44.34085 | 2025-10-29 04:25:00 | NPP-375D | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 24cb23b2-91e4-3831-a335-b389b3b67b90 | -13.02011 | -48.76956 | 2025-10-29 04:25:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 3a0d08e4-849e-3b80-80b2-e98b62377fc5 | -14.92757 | -49.65181 | 2025-10-29 04:25:00 | NPP-375D | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6c047aad-74ea-3800-9f43-768f3409a17f | -14.51627 | -48.00223 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0ba9147f-e28c-3ce0-bf9f-28230c7229a2 | -18.91909 | -45.03246 | 2025-10-29 04:25:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cfbd97d6-b076-36e5-83a7-635b53fa273d | -13.04208 | -44.98631 | 2025-10-29 04:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9676683-88a4-3f9a-b3a6-ae53464888ac | -12.00985 | -49.83739 | 2025-10-29 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c89c04c7-d318-3267-b122-24e496c2a391 | -13.05634 | -48.46396 | 2025-10-29 04:25:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c0073d98-30f1-34b8-af64-86c7b5622def | -13.94556 | -48.46985 | 2025-10-29 04:25:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3b467a1a-4cab-3b87-aa92-c68f73ca0ecf | -13.15247 | -48.21583 | 2025-10-29 04:25:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 709726b1-3e84-39a8-a691-7e3eff927d06 | -13.63484 | -46.51844 | 2025-10-29 04:25:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2384d077-1f67-3b08-8b5f-7a3cdf3dea55 | -12.69771 | -46.30674 | 2025-10-29 04:25:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ce5d6d90-8174-36e7-a4f4-d4684a4a65d7 | -13.56443 | -47.34276 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 065631d6-bc6c-3f2e-84f4-b8457b6cceec | -14.26139 | -48.10738 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f47904d4-ebcb-3c26-8069-929ff0451048 | -12.01057 | -46.77636 | 2025-10-29 04:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c1e4a2c7-f639-335f-a722-b9bc9d794e49 | -14.30791 | -46.52023 | 2025-10-29 04:25:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7dc3d5e7-ef04-3e3c-aa1b-09b5e4a89bd6 | -19.33837 | -43.04221 | 2025-10-29 04:25:00 | NPP-375D | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 0f80141a-2bd3-3d06-a43e-0af2f89c39af | -15.09792 | -43.83957 | 2025-10-29 04:25:00 | NPP-375D | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 15.9 |
| b18972b0-75ae-31f4-9241-5074f21d548f | -12.15496 | -47.69487 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 318f23c3-dc76-3848-a7e9-52cbea7fca8b | -13.27811 | -47.72907 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d23c1496-2077-3db8-9d36-c9fd52df63c4 | -12.10155 | -47.17055 | 2025-10-29 04:25:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 22b0747b-cdbe-3363-94ca-15cd1e978689 | -13.68118 | -47.18529 | 2025-10-29 04:25:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bde58299-821b-3033-9309-e5e3ff59fc2f | -12.1787 | -46.71598 | 2025-10-29 04:25:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ee472ecc-0ac3-3c60-bb75-00f32dc99e03 | -12.55378 | -44.96207 | 2025-10-29 04:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bcb31939-6403-3e31-8fa7-b5c0602eb9f3 | -14.26295 | -48.1191 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8a0dbe34-9216-323b-b318-144de1a33390 | -13.05169 | -48.66779 | 2025-10-29 04:25:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b69a0d71-5fc9-32c5-9a2a-a066f072c415 | -12.20615 | -46.52377 | 2025-10-29 04:25:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bbb25a40-fa95-3be4-bc8c-1a0039b132f4 | -11.97681 | -44.03539 | 2025-10-29 04:25:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6c03f05b-54bd-3c6d-aa44-d256c4ce86af | -14.44062 | -44.82145 | 2025-10-29 04:25:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b076d82d-d7a6-37d0-850e-9d66169366d4 | -14.60951 | -48.43218 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bb696986-cdd0-34d6-82f2-5b2e115c6451 | -11.8058 | -47.07385 | 2025-10-29 04:25:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bb870af5-e7d0-3eec-a2d7-91bdfd10461d | -12.08688 | -46.38453 | 2025-10-29 04:25:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 12474f55-e3a9-323c-bcb5-34964dfaaf5f | -14.26874 | -47.31598 | 2025-10-29 04:25:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 958d6379-7b1e-3ba7-b5b7-01a81330558a | -13.88519 | -48.45908 | 2025-10-29 04:25:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f6233d39-a58f-3d1b-b7aa-49fdd2222f5b | -14.27876 | -47.31766 | 2025-10-29 04:25:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c604c29a-0e07-373c-b665-d0850d97ef52 | -19.3364 | -43.05725 | 2025-10-29 04:25:00 | NPP-375D | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| df39a013-d234-3472-94f1-26fe403184ab | -13.53527 | -47.35285 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c03618a3-9e63-3bcc-ac1a-ab50547b5652 | -17.62754 | -43.99323 | 2025-10-29 04:25:00 | NPP-375D | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 545a7aae-6be0-3833-a030-f9a56c120e82 | -13.56943 | -47.16259 | 2025-10-29 04:25:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fa942cb5-be9a-3afd-9977-058bbb91e137 | -11.33493 | -46.06645 | 2025-10-29 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4a52f920-6950-3074-95eb-76ee30954bf3 | -15.79541 | -45.19467 | 2025-10-29 04:25:00 | NPP-375D | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 65286399-486c-3f50-9706-6636b84f185a | -18.91862 | -45.03515 | 2025-10-29 04:25:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| da160666-bd62-347a-9269-8d252d19f220 | -12.97236 | -47.91044 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e5aad375-fcf9-30f4-81db-e8b04560b765 | -14.66029 | -50.1871 | 2025-10-29 04:25:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0df1912f-1ad1-3761-b057-01d733a8fece | -13.25069 | -44.11094 | 2025-10-29 04:25:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cc7ffb0c-2cc1-3c27-9f61-d87fbc7328ae | -11.96202 | -43.28501 | 2025-10-29 04:25:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 786eca9f-3af5-3c0f-a2ba-3badb298cac5 | -11.32718 | -51.1604 | 2025-10-29 04:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8d777616-fae7-38d8-8bba-106f2cb43da7 | -12.85652 | -47.23263 | 2025-10-29 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 83348d50-5583-314f-a48d-a6dc79ddea2d | -13.03632 | -46.73336 | 2025-10-29 04:25:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6e6bb5aa-53a3-31a8-99e0-3e8f1710c867 | -12.76713 | -46.65643 | 2025-10-29 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6ff26a91-bf1e-3dff-94de-e90632ee989e | -15.1801 | -47.20734 | 2025-10-29 04:25:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc9077bc-2c05-3541-8523-67bb4beca89d | -14.59612 | -48.41098 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 838e6f41-f331-37fd-9fc1-801d15d5a787 | -12.16112 | -47.69992 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b318db50-d2ee-3f4b-95c7-7c87d86a9a32 | -14.64714 | -48.3961 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6decea88-b9e3-33b7-aa56-0a6a359d5686 | -13.58059 | -49.59663 | 2025-10-29 04:25:00 | NPP-375D | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 51101503-e655-31f5-bed6-9e4a6e39308e | -11.58827 | -47.95295 | 2025-10-29 04:25:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f1176aaf-c7a4-3f74-b189-7a01725f9e33 | -12.7699 | -46.6605 | 2025-10-29 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 08af41a2-2336-3abe-8356-c22c6fa1797d | -11.25352 | -49.84653 | 2025-10-29 04:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5a5d906a-eb2f-3be2-a27e-a4620bbe731b | -14.25461 | -48.10617 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 698c7ef7-e5ff-3ba1-8273-bc0a64cac40a | -12.15773 | -47.69928 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 905e007c-a914-3910-b298-809483726e72 | -13.03186 | -46.73993 | 2025-10-29 04:25:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cc438604-2db9-306f-9e50-26710ef8145d | -14.96799 | -48.1885 | 2025-10-29 04:25:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| d007da9f-c318-3897-98af-0a0335a88159 | -13.53863 | -47.35334 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a13e0ff5-b39d-3ba6-a311-5f707bc82daf | -12.1909 | -46.72531 | 2025-10-29 04:25:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 28bb0f9e-b79c-35cb-92d1-7990ee062d4e | -12.29084 | -47.01004 | 2025-10-29 04:25:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5904a48d-726f-33e1-95ed-98b32058cdbd | -13.2148 | -47.07088 | 2025-10-29 04:25:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 05f3299f-5258-3e35-8f6b-39cbaf64c49a | -14.60076 | -48.40409 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7055401c-0597-36df-9598-8e760838f9fc | -13.31326 | -47.70529 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b956179c-2f1c-3bff-b843-7110b94bfa85 | -13.21204 | -47.06672 | 2025-10-29 04:25:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7d997236-da56-3d7d-8f5c-b8771c3e92ab | -12.71043 | -46.31247 | 2025-10-29 04:25:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 8abc8812-9ff4-31ee-9293-b7d83d36e515 | -13.44361 | -47.37853 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ee43b2c9-5730-3b12-b496-7d89f46e4c4e | -12.18756 | -46.72475 | 2025-10-29 04:25:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5f450c0f-a0bb-31dc-b9a0-d1c5cae7951d | -11.79058 | -44.39027 | 2025-10-29 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6ea9e93e-717f-337b-ade5-5f4fd57d7088 | -12.11684 | -46.57456 | 2025-10-29 04:25:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 99e46e5a-193c-3e02-adaf-1db05464dfa4 | -12.91548 | -45.04094 | 2025-10-29 04:25:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b03a692d-c574-3493-8658-62fa5cbfd682 | -14.59674 | -48.40717 | 2025-10-29 04:25:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c7aa1d66-0630-3ae8-a42f-fb6433ab3cbf | -13.37222 | -47.41477 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 56326aa8-56e9-3a08-9c51-3a7f39bf4010 | -13.6104 | -46.48551 | 2025-10-29 04:25:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f3d620b6-760e-3d4d-8378-c3e0bc8d52a2 | -17.94911 | -44.2951 | 2025-10-29 04:25:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c067bedc-15a9-33d8-9b4e-e92760b0e543 | -13.89541 | -48.50409 | 2025-10-29 04:25:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 907da2e3-1a93-31ee-afc4-5c51af3d69bc | -13.3541 | -47.67371 | 2025-10-29 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4ca9177f-c6ff-3f6c-9852-a23420c80550 | -12.07302 | -46.38589 | 2025-10-29 04:25:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9e59285c-06dd-3f8c-858c-5375d89fa238 | -13.31987 | -47.45093 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c7d10d22-93f3-3d4f-bac2-f62fe909e1f7 | -13.43416 | -47.37302 | 2025-10-29 04:25:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cd5bb83d-6bac-3701-bf76-b6c10db44efe | -17.04114 | -47.05453 | 2025-10-29 04:25:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 07950512-7008-3011-9abc-f14a3d7ca77a | -12.69234 | -48.4394 | 2025-10-29 04:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 82d18427-610e-3dd9-bfe0-913869fe262d | -15.84423 | -49.10236 | 2025-10-29 04:25:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| abf38ec2-4cdd-32a6-8e54-29f18da8fd6f | -13.65727 | -48.44096 | 2025-10-29 04:25:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 863809fd-6fbf-3b3d-a76d-c9bce9921387 | -13.87392 | -48.4842 | 2025-10-29 04:25:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a99037be-2ff0-39fd-a20a-da4cd153e7d6 | -13.57545 | -49.60489 | 2025-10-29 04:25:00 | NPP-375D | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c8cb0f54-0279-38c0-bc9b-d9a1e2fd9fcc | -13.25189 | -47.01096 | 2025-10-29 04:25:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README45.md)
