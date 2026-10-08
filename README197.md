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

## Dados Diários - Página 197

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 494598b7-bf5c-3a0b-9307-0b1fcaae401d | -4.06261 | -59.8389 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8cda31ec-73e1-3ca6-8b1c-917e246c9fef | -3.70686 | -59.67597 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| edc48d0d-2c73-30e3-8ee7-f11f1a3551bb | -3.2722 | -54.05381 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6827ee29-a2d4-32ad-ad57-d389bb48d939 | -3.30549 | -53.87146 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5691a250-041a-343b-a898-f031de32a7c0 | -3.87762 | -55.82392 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 89fb26e5-3cc2-309f-aee7-2a8fa7a43dbf | -4.66493 | -56.21877 | 2026-10-08 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f67b77df-ab8d-3dde-9c9a-3c9a1ce66f58 | -3.05964 | -54.21669 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 904a202c-ccf9-3f77-a88b-3592e48725c8 | -5.21924 | -62.59132 | 2026-10-08 05:42:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e957fdf-0e60-362f-b2fc-a4b8cdc46878 | -6.25096 | -52.87412 | 2026-10-08 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f13349b3-2aab-34d5-a486-c3cf831e45a6 | -3.47877 | -59.57718 | 2026-10-08 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3748e17c-1b4d-3059-adba-2689a935a6ff | -2.7837 | -54.0872 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aef3423c-6cd2-35b6-a724-5617092fe52b | -2.50511 | -56.18015 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 478b980a-7cca-3439-ab61-56d215995d3b | -3.45321 | -58.06254 | 2026-10-08 05:42:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bf80e20f-85ff-39f7-9b73-f9cd5f071c81 | -3.07577 | -54.28521 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 12d08d0d-3678-3b31-810e-6a6842f80f45 | -3.3658 | -58.19808 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4e53dbb7-14aa-3a45-ba2b-1c0639b45b86 | -2.87981 | -54.87837 | 2026-10-08 05:42:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 507c3528-957d-3705-b530-64320d9af905 | -3.10625 | -53.78201 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c99d4931-761c-317e-8e23-3544650fb8c3 | -3.96739 | -56.11315 | 2026-10-08 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9b955d74-8dc4-3345-82d5-fe4ddd12e11d | -3.38103 | -59.43306 | 2026-10-08 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8882e8ee-9b99-3ae3-9d65-485cb18d6eda | -3.01559 | -54.07993 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 03d219bb-2529-3e21-bc7d-b96e0ff7932d | -2.15813 | -59.2231 | 2026-10-08 05:42:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2f772cd5-d129-3867-8eb0-a112a4380d7a | -2.98225 | -54.12159 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 91ed4047-19a7-3877-8141-dc0ca26d3962 | -2.99288 | -54.08651 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| b3b8f5e1-9be8-36c7-8351-4996ac218c85 | -3.30794 | -54.05589 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6600d853-11b8-32b7-9acc-b55f08cd07b4 | -2.49418 | -56.0684 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 832454cd-4768-3af5-ac62-d57d4aeb3876 | -2.5119 | -56.25625 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1dd4bdc4-af0b-3ac5-83dd-3dfd998f2b1c | -4.54027 | -54.98642 | 2026-10-08 05:42:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 894e70f8-53bd-3ef8-8c62-a6e75cb53cd0 | -3.17655 | -54.61178 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b08bcf4d-33f9-3489-b6af-3cffbd56df97 | -5.88117 | -53.62484 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| de7c0fe6-2e14-3c69-a33c-170edcf7855b | -3.27019 | -54.06705 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ca69fd29-4549-3242-8642-8246827477ac | -3.30536 | -54.69601 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4b5c6a1f-d3c5-34d4-9c9a-da1921e0b4e8 | -2.05036 | -56.38651 | 2026-10-08 05:42:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cd64f847-e6e1-3055-bdc7-eb83c49c0fb3 | -6.6198 | -59.94067 | 2026-10-08 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3157e795-1d1d-3e88-a102-eaa6f2da452d | -3.08148 | -54.2829 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7160758d-6cef-3d0c-b37e-e707553d613a | -3.30988 | -59.60908 | 2026-10-08 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2c4a1af2-da9b-3f94-bf03-a07ef85dbe1c | -3.54251 | -59.50999 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a8ca3c12-6795-3999-898b-f38c7299a4b7 | -3.28169 | -54.04857 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a914ecb6-eca8-3ed7-b806-914d218a76d5 | -3.31476 | -54.04662 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 0d3e96e3-f8b5-3447-a911-17df4f1f0efc | -3.74347 | -59.44081 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d69501b9-af79-3612-a7f7-8ac263f9aa12 | -3.54894 | -50.09887 | 2026-10-08 05:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7eb95a6-46c9-3e75-90e6-9e82919532fe | -3.53995 | -59.47771 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 09e5ed85-a6c2-3d9f-bf7f-6de1533cb34c | -3.50853 | -60.36699 | 2026-10-08 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ddd80672-1a41-3cab-a518-8898a18bcad4 | -7.20719 | -55.10256 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 752ee923-e37d-3341-9a2d-0365fb6c19b9 | -7.00023 | -59.12075 | 2026-10-08 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 05446fdb-fc46-3a7e-b553-3b6a66b7267c | -3.54699 | -60.2058 | 2026-10-08 05:42:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0f0c850f-8eb0-3b79-810b-1bb6fbe4d5ff | -2.98806 | -54.08241 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 0c240150-88f3-3c9b-a038-faec367d3b3c | -2.97022 | -57.76314 | 2026-10-08 05:42:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e79dbe56-4d69-3eb7-bdd6-654c93dc7f6d | -2.50898 | -56.18531 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 90140670-f808-3103-8b36-51cc67c49719 | -3.09576 | -54.2949 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe286712-1b5d-3cd8-8c94-1119f8ac42db | -2.22024 | -53.70198 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| e27b4e1a-f094-3d8f-8b5e-c8a36d300317 | -2.49985 | -56.18402 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ff3ce08c-d65d-3e64-93f3-86a266d46a6e | -2.50268 | -56.16564 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 747cfe91-42ad-337e-ba17-95051757c702 | -3.11657 | -53.78733 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ba9870a1-d230-3b9b-95d1-b572942bd490 | -3.30602 | -53.86805 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 86b73db8-fb46-3a15-a54c-30410a836ba3 | -7.00874 | -59.11852 | 2026-10-08 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7bdd2ba0-4e61-3bb0-8917-fd0b9713f756 | -3.26889 | -54.03963 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bd9160d8-4f47-365e-9648-a3784850321e | -3.48112 | -59.58653 | 2026-10-08 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 58d7a366-1dc7-36b2-855b-51249bf9ad56 | -7.75765 | -54.95545 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 760a1ae3-60bd-38dc-8ac8-56db29acc887 | -3.66751 | -60.62203 | 2026-10-08 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d73af7b-ed80-355b-8d3b-e3d215b8934c | -3.27093 | -54.02626 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b9016fc6-da91-3686-8889-d03d7a9e0be7 | -3.28851 | -54.03922 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2229e65c-fd1f-3aa3-82b7-659640ec998c | -3.11707 | -53.78387 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 814f120b-1d25-3c09-a6ba-8dc71b5d80d7 | -3.19192 | -50.56401 | 2026-10-08 05:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f386aa22-2e24-39d3-9960-0916d23e757c | -3.74074 | -51.21202 | 2026-10-08 05:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 96c7a892-5e8b-3608-b07e-20a4c7d337bd | -3.55114 | -59.47941 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3ea68dd8-4d0c-3f7d-8f88-d1f65486c2a8 | -3.29141 | -54.05683 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0dbb9780-cf3a-32a1-8128-1af61d292524 | -2.78886 | -57.64484 | 2026-10-08 05:42:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 49611c5f-50fa-38e8-8478-180cd6b53cef | -3.70401 | -60.55071 | 2026-10-08 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f20c065-685f-3c7a-962d-a86d83419a1d | -3.58621 | -54.67446 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 01b62d65-b560-3af1-8708-5eac1cfbae7f | -3.16862 | -50.60394 | 2026-10-08 05:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 112ab745-8077-37aa-845b-8b1037d33562 | -3.15954 | -54.7235 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9779f94e-5741-383c-92c1-a9512f861b14 | -2.79046 | -54.0782 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3176ee73-4582-3b4d-86d7-2da3bdf62c59 | -3.03563 | -53.94656 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be7adc19-38d8-3aaa-a4f5-361dbec3d6e1 | -2.77554 | -54.06932 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8e15df1a-4844-329a-80a3-2f251d06892b | -3.30021 | -54.034 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b055c1c0-5d52-377d-8567-de129046e9a8 | -5.2526 | -55.92007 | 2026-10-08 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a9b18a3a-5606-3845-98ce-e448e79f44a7 | -2.5034 | -56.16102 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 72aea101-fa24-3f4b-81f0-e81c63e3fcdb | -3.83537 | -55.97371 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7b464625-b6fa-3c87-aafa-3d04b7295815 | -3.19362 | -50.55235 | 2026-10-08 05:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1a6cc1c9-7339-3fdc-8c82-566e677e58c7 | -3.85381 | -55.98856 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 89b96c36-a3d9-3f56-b0ed-dfb005029fa7 | -3.32426 | -58.22762 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 075047ec-b3fb-31cb-b0a0-0b33bf02e903 | -2.99819 | -54.08734 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 2d06d08f-e110-3533-b662-27979695b69f | -3.70136 | -61.32145 | 2026-10-08 05:42:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| efc5ae90-7184-307e-9b42-df3cf4bc565f | -3.57071 | -54.49387 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c1f6b7d-90fa-3f10-9be5-da62e90f97aa | -2.76973 | -54.10829 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5e818aaa-4f80-3b8e-b7a1-5ae27dded9cf | -3.30447 | -54.70212 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7cda6883-fad6-303b-9343-489ff90bac9a | -6.7327 | -63.0504 | 2026-10-08 05:42:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7381e47e-a81d-3e1d-ad1d-634e991e097b | -3.55577 | -54.66688 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2d7f755e-9ecd-313f-8b1a-33a9950baea2 | -5.73952 | -53.45529 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7176a4dd-528b-34a7-a066-82ad7011942c | -3.56397 | -59.47938 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c398f233-71ce-3c5d-97a8-38b69c443f15 | -2.8981 | -54.07469 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e47cc88f-f4ad-39aa-9104-1c622fa0ee45 | -7.39076 | -55.20487 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea8fc571-dfc3-38d7-8dc0-ca5b2a94406a | -3.8626 | -58.64695 | 2026-10-08 05:42:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 392450e1-33ee-344f-928d-dabb32dcbe6d | -4.14421 | -54.03285 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1a551f25-82ee-3682-81b0-2f382646a2ac | -4.36872 | -54.7491 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 81e13afc-e28d-3e76-9440-8237ed48499b | -5.30085 | -60.09995 | 2026-10-08 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f192f5b9-5956-32b0-8edd-38014f9770c0 | -3.67466 | -61.15723 | 2026-10-08 05:42:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3a2dcf8f-002f-362d-bfe7-430b69ea3bc6 | -3.18695 | -50.55134 | 2026-10-08 05:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3a42b7b5-c3e7-36f0-9b39-0da0e4512c2a | -3.32828 | -58.22823 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0c1349c0-2c79-3df9-9cc7-acb3b6bf2822 | -3.01424 | -54.05267 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README198.md)
