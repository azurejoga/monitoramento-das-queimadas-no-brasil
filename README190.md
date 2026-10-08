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

## Dados Diários - Página 190

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9ff7226e-3982-34ca-8621-38461758faaa | -3.30491 | -54.69906 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89a1ac1e-0e20-304d-9f2d-fa0e29195bc4 | -3.86105 | -56.00505 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 39aa6c34-2243-33be-869c-ba73ecd164d4 | -2.49231 | -56.11132 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3aec40aa-43fa-3965-9978-8af6b1664ba8 | -6.09009 | -55.72808 | 2026-10-08 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 79d824a7-92dd-3357-9496-4830490186fe | -3.28423 | -59.20741 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2707e5f2-0b91-36d1-9692-ca478d79ce59 | -2.77938 | -54.07992 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a3ce6823-2ff6-3336-a1f2-eb2322e4d765 | -2.57993 | -56.15103 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 27cb603c-28e6-306c-951c-dd474422d038 | -3.03279 | -53.92887 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ba0eedda-c23b-3e9c-96b4-0a0f4d830776 | -3.04506 | -53.92032 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 05e2e944-4d43-32de-877b-3df8c12527db | -5.27136 | -55.95988 | 2026-10-08 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 95b171da-4379-303f-8ea7-12961e83b46a | -3.11527 | -54.16534 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| e2d4e87b-a177-38b3-b1dd-e55b4ddd2ad5 | -3.26608 | -54.02209 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| c7c5fa88-286f-33f0-a3cb-ff7a36ef9884 | -7.75228 | -54.95469 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0cc44168-846f-3736-9a5f-e08a0128c2e4 | -3.29244 | -54.0122 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ee499e28-92c4-30d9-a23d-b0beab77c2e9 | -2.99907 | -54.11772 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8189b198-9ef9-3f34-9353-33c2aef9b43d | -4.06975 | -51.0452 | 2026-10-08 05:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a9efadf6-f974-392c-9f29-1bb753c6cf34 | -3.04711 | -53.90675 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ebcb711-64fe-3c80-b255-8383c7562c45 | -2.90019 | -54.02442 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| daa06ef5-d4e0-3f9d-a2c4-611fe1e3cd28 | -2.78615 | -54.07088 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cfce8432-bcb6-3610-8b98-b4234b7318e9 | -3.20819 | -57.86928 | 2026-10-08 05:42:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38af8107-f2e8-3b5d-b343-f45c22a4ec92 | -5.87544 | -53.62414 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3f71e491-7341-3b34-ac53-a9d13a21dfd9 | -6.14377 | -52.64764 | 2026-10-08 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1f8d082e-5345-3f71-a673-f7d00c4f799c | -3.02721 | -54.07495 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5a3dee08-8625-3760-abd8-e253c7b5720a | -3.13844 | -54.36588 | 2026-10-08 05:42:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7dfd13cb-cbd4-3af3-96b7-c558bf501623 | -3.29922 | -54.04077 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 622ae0c2-8055-3c98-a97c-6e8c48956392 | -3.51543 | -54.65496 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2714a0f8-0900-31f4-b34b-ff86192c8d92 | -2.50317 | -56.13213 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cd0d6785-7a07-32a6-be2d-c95dbe4695c1 | -2.50631 | -56.14215 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 937b4dd1-7341-35c9-bc2c-40a5243222e1 | -3.28512 | -54.02494 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4e3c581-7b61-3831-8e2f-31e8f718fcac | -3.02936 | -54.23853 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a3653f1-9f59-3f1a-b640-ab0e398ebeb9 | -3.02071 | -57.73671 | 2026-10-08 05:42:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 475c7077-d313-3d31-8d56-265fc9d807d1 | -3.29513 | -54.04689 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d2efe721-cd72-3965-9d76-03c0553bead5 | -2.87302 | -54.88946 | 2026-10-08 05:42:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1eea926b-71f8-3dfe-b27e-0c06dc5f73b2 | -3.0893 | -59.19136 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9c973148-8bbf-38ee-8375-9d651b8bb48e | -3.01397 | -54.1267 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| b330d2d6-a4ad-325b-8e26-d24a19901075 | -3.17895 | -58.63255 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 24cc7e6b-c43d-3e70-a885-ccc11fee5794 | -4.1168 | -59.87812 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 39c58a53-0503-3213-8c53-0239858ca2d4 | -2.75615 | -54.09516 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2bb5990a-53f8-3989-94b6-65957e98a681 | -2.78468 | -54.08068 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 25de9f37-0b5a-347a-ae61-95969638fec2 | -3.12284 | -53.70628 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 134604bc-72de-3a7d-a23c-baf68a6a8dc0 | -3.7623 | -61.17791 | 2026-10-08 05:42:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9f1b1e3f-1c16-3878-ac63-ce9e4b1b61cd | -3.57116 | -54.4908 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5a90bab5-bae1-3640-860d-0d2b31ca0207 | -3.003 | -54.09143 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 862af06b-21ff-34db-a29d-7088c6f98f21 | -2.48872 | -56.13479 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 96f74e6b-6c3a-3610-8dc9-a50d4f73ca5f | -1.97362 | -56.06671 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0b221d0b-7d42-3b07-9b9c-d84b1405bcbd | -3.05579 | -53.92205 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 26d77010-4f20-3f5a-af88-17e7de1f4eb9 | -5.24233 | -50.91548 | 2026-10-08 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 92e42d5c-3d8c-39ad-8e33-fd872ffd10de | -3.6375 | -58.94165 | 2026-10-08 05:42:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7adb3b5e-9f1f-38df-8c8d-be87199e0723 | -3.55277 | -59.47765 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d381150-19df-329d-812a-45cad0a43e54 | -3.30893 | -54.04916 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d811145b-463d-38ea-8e20-cb34d8c2b753 | -4.36825 | -54.75222 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f075f3c-6b19-39d4-a2cf-03648b0d26a2 | -3.59276 | -54.66593 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1ac06426-7a7c-3738-9ffd-5a5d7261a60f | -4.11613 | -59.88243 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| bd1763cd-e904-3751-9371-ec073212cfaf | -3.51813 | -54.65704 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| db3a7eae-1899-3026-972f-32ce5bbf7891 | -3.25041 | -57.86817 | 2026-10-08 05:42:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 48564785-916a-3c28-9ce7-792ed0c1ca61 | -3.57452 | -54.68229 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| d9bd034e-447e-31f1-885c-fb55c5b0c50b | -3.02707 | -59.21611 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2b7deedb-c24c-363d-804e-acf39a7cee5d | -3.00143 | -54.13813 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4de06f2-ee6d-3b48-8328-ca62b03dd691 | -3.09248 | -53.71624 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 47b07957-97a0-3ccc-8ab3-bfc9911444d0 | -3.09184 | -53.93778 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 55e8c5d0-9a6a-3737-999c-a5957174e11a | -3.03917 | -54.1035 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4ace122-4f51-3bb3-a3be-d1dfb0242887 | -4.80888 | -54.67929 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6006cdc6-1ac3-3efb-9b0b-e5405ff42b04 | -3.28378 | -59.41097 | 2026-10-08 05:42:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c1070efc-30fa-35b5-a487-036f3e3e53e5 | -3.11067 | -53.7794 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6cfc1038-6705-3698-99ff-34f5662f59f9 | -3.5479 | -54.68455 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 472ce186-1614-3ae9-9bbf-fae011b00785 | -2.49884 | -56.16027 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1afe9dd9-d4b9-315e-8227-b0748071a02f | -3.29307 | -54.06029 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed430b0f-307e-3e50-a62a-c5c4fb4b6fef | -2.99778 | -54.05359 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d5fd94da-0050-38f7-be76-b98229936e48 | -3.72892 | -58.86164 | 2026-10-08 05:42:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d0ba0cd-e6c6-3576-afda-7f7ed8f2f29f | -3.02389 | -54.06091 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ba2e12f4-7e3f-35cf-81e8-b1a7cf5a0773 | -3.06063 | -54.21024 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca342b97-e9a5-31b7-8465-afd787a6f05f | -3.64101 | -60.63006 | 2026-10-08 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 37453f9f-3444-341f-98cb-e3a25e8dd7b6 | -3.05094 | -53.91779 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97dd88ee-8632-32eb-a56f-be3f8bc6f7ba | -3.55016 | -54.66926 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 099c4e1a-8ecb-3eb1-90b8-805c30e49fa4 | -3.18721 | -60.0589 | 2026-10-08 05:42:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e4e821f-0606-3b9d-8ac9-77df3e810b02 | -3.2671 | -54.01537 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5c2709d2-44fb-38e5-a1f0-059275934586 | -3.52012 | -54.6589 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d1896969-f54b-3508-b0dd-68fc93d13a49 | -3.30071 | -54.0306 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 01e5feca-af7b-33be-bdb5-ba4ef7063d68 | -6.46304 | -55.47844 | 2026-10-08 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 444c72f2-5690-396c-ad13-1f0f103734e8 | -3.62304 | -55.50574 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e0cd3e61-a067-3ce4-8ccf-721a04bb5ac7 | -3.73788 | -59.47675 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 048076d0-6bb7-33a0-8613-c4ff3b63939a | -2.46624 | -56.09779 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| daf9db16-614a-3b74-817c-9d90ae3938e5 | -6.48889 | -62.85399 | 2026-10-08 05:42:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 33f4335a-ab9b-3cf1-b129-ae9de8295f13 | -3.89801 | -59.44586 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4ee07017-1cab-320d-b84c-48b3d27afb0d | -3.01275 | -54.06264 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d7616fdc-50db-3490-ac2b-959d5120d799 | -3.28415 | -54.0692 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5da474df-7c1f-3735-8edb-5a09e5ddee02 | -3.30884 | -53.86133 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 56a5c6ae-69ea-3528-9512-47d83be5984f | -3.84726 | -55.9907 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 452ab0d4-004b-3f67-ac67-a6b652cb1421 | -4.12415 | -59.87925 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 48bfbb99-7328-314c-9869-935d4cb7d3c0 | -5.30281 | -60.08688 | 2026-10-08 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f313230a-9ac9-346d-ba07-9fb9f7a4519b | -2.48069 | -56.0953 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8f400075-56de-398e-81c6-d2b9a2bdb000 | -2.4916 | -56.116 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 00a09bbb-df4b-3a73-b0db-db58b9054bee | -2.48385 | -56.10537 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a073bc66-42f7-3ed6-a7f6-c6b0c1ff5b6f | -4.77424 | -55.72238 | 2026-10-08 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dd742f38-597c-31f7-bf9b-70cab72b990b | -3.16648 | -58.63568 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ff02b8b9-ade2-3e61-aef1-5d6a40e6377d | -3.05145 | -53.9144 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab12650b-a326-32a7-a30b-3c0a9f58228b | -1.82508 | -55.03685 | 2026-10-08 05:42:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b5f19ae5-ed32-3f84-8066-8c0f1a317b75 | -3.35118 | -50.48184 | 2026-10-08 05:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 136d08ca-7ff8-308b-bc95-a4c2aabeb09d | -3.58197 | -54.66763 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 46b1f748-4601-367e-b2ab-41e479ab7feb | -3.04968 | -53.96241 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 30.3 |


[Clique aqui para ver as próximas entradas](README191.md)
