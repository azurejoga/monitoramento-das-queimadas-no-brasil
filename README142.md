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

## Dados Diários - Página 142

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 63a8608d-4f26-3109-8f59-d50ffd06d23b | -4.02944 | -69.50343 | 2026-10-05 17:37:00 | NOAA-20 | TABATINGA | AMAZONAS | Brasil | 1304062 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e493df34-1873-3eb0-b2a8-324e60b15739 | -6.37 | -55.15039 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| a93692dc-6b2e-3bcc-b91f-6dfc273c5e9d | 1.85796 | -55.78947 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 84aeac9e-dd0b-3283-8a92-96f07240eb52 | -9.38592 | -68.32157 | 2026-10-05 17:37:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0b219087-4f14-3e42-bcbd-c257c25a42c8 | -9.12406 | -64.38576 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 11.6 |
| cb5630ae-223f-335f-8af4-57a3941c51d3 | -0.98052 | -53.03633 | 2026-10-05 17:37:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 21817086-56b6-3228-b8d2-c421c3762112 | -8.56202 | -67.06585 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 7288f571-6cae-3b4f-81cc-cfc32bab1b78 | -1.42902 | -55.34748 | 2026-10-05 17:37:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| bb55ad59-0213-33ed-9c34-61ca6add645b | -9.50795 | -67.13227 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 945cba77-4c5f-3840-893b-9bcb61fd74b6 | -3.10415 | -60.19629 | 2026-10-05 17:37:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ce5bb373-c6b8-39ba-8cbb-1f27fd845af5 | -1.2226 | -55.79255 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| bbcfc96c-e929-3766-b585-0164f6184a71 | -2.75991 | -57.64789 | 2026-10-05 17:37:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 0803c90c-b9f2-3429-8ce8-a4a1c2a2f3b3 | -9.34067 | -64.71864 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b9ea19b0-5828-3273-9642-f226b819cadf | 1.76511 | -55.60335 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2a0ab914-9703-3e8e-a489-89653495c654 | -9.13305 | -67.92509 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| c8e00a75-52cc-3830-a525-5c469103792a | -0.73541 | -57.9784 | 2026-10-05 17:37:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 2aae1ee9-f2ed-32e9-a762-ad83f96fe824 | -2.13185 | -56.68566 | 2026-10-05 17:37:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c059b471-5805-3bfa-8036-5937edb3e6fd | -3.17991 | -60.07019 | 2026-10-05 17:37:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7098474b-a068-3887-aaf1-a2fa3b986188 | -9.23801 | -67.86829 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| e6b2e84b-396c-39a7-a1b8-6cd99e8625c1 | 1.51507 | -55.64856 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5c76f175-51cf-30a3-bcf8-e65c9b7a5a28 | 1.29283 | -51.12804 | 2026-10-05 17:37:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 2cb06780-93f4-34e4-96c0-f6eeb488f058 | 1.60185 | -55.7875 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6f4bb303-aa8a-3ef2-9c7d-66cf1caad684 | 1.47083 | -55.6728 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| c33f88cd-d3b7-30a5-8523-376f698f0643 | -8.90456 | -68.64143 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 4ff90521-39f3-379f-b8f7-47bafb932fdd | -10.24436 | -68.30401 | 2026-10-05 17:37:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 04001205-0e67-3f10-9edc-0e099af6fcab | -7.21582 | -55.19922 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| d0151c29-d32a-3921-8a4d-9207a4967ecf | -9.23605 | -66.11169 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| b616e7c0-f09a-3af6-98b7-158f0786c7bd | -2.27026 | -55.83981 | 2026-10-05 17:37:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 083db081-1eac-32d9-a707-a4229c2ed31d | 1.75245 | -55.59694 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| aaf06524-d26d-318f-9a0b-6b7473584ca2 | -9.05138 | -66.10235 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 56ab967a-5a10-3d28-ad9c-e2f3fc600291 | -9.09975 | -67.74522 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 86329444-0c92-365b-8727-630fd7a36818 | -10.62189 | -67.92179 | 2026-10-05 17:37:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 93127b78-2270-30e2-90dd-13a7fea52966 | -9.35077 | -68.79651 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 8a2c0f59-c4c1-3b88-b7b8-e4a100a637e7 | -8.77793 | -66.5649 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 18.8 |
| b1d5bdcb-a16a-39ab-8e72-5afa4ad0ba1a | 1.87718 | -55.7518 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d89df779-a377-3c23-8637-d27e731f8392 | -10.24962 | -68.30333 | 2026-10-05 17:37:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 47c5f75c-1c35-398c-9b42-3eb788ff92bb | 0.06923 | -60.68464 | 2026-10-05 17:37:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3f20a070-c5fb-3d82-937e-4a533a160933 | -9.10384 | -67.69839 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| c5ff2e94-6a9a-379f-b773-438c2fdac283 | 3.06947 | -60.59629 | 2026-10-05 17:37:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 10.6 |
| e7e04ed9-aabf-3b6c-b501-6454444e4014 | 3.58728 | -61.34097 | 2026-10-05 17:37:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 8cd2eb97-23ad-3293-a738-7772b1c75423 | -9.14349 | -68.22695 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 1f35dae0-f2a1-3c44-b205-b13187795b1e | -2.07567 | -56.83369 | 2026-10-05 17:37:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e3e9b378-db0b-32e4-8073-51f1b02eedfe | -9.43488 | -68.85512 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 9.5 |
| b5957706-c5de-3c8e-8bba-90e04f3563d4 | -1.60443 | -55.97047 | 2026-10-05 17:37:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 025b842d-d7bc-3e4f-ac2e-3673596e07b1 | -9.41693 | -68.84356 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 083f2dfd-f880-31e0-89a2-8e1b00a7032f | -7.22438 | -55.1766 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 41.9 |
| b8841af9-df50-31db-9f1d-d36632a41ef1 | -9.01596 | -68.43203 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 1e583bab-40de-32b9-88da-60a8059017d0 | -1.84785 | -64.13732 | 2026-10-05 17:37:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 290.5 |
| 6bd3e8f5-9720-3575-8fda-f60cbabdf3c3 | -10.23502 | -68.23296 | 2026-10-05 17:37:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 61851ba6-32d3-3c20-8353-2c622fa5e2c5 | 1.51441 | -55.65288 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e9cc6744-756d-3697-94dd-d529623a38ca | -8.9978 | -65.40137 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| fd3e5c6d-53be-3d23-a395-92edf493340b | -9.23134 | -67.89614 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 5458729e-ca9b-33ce-b5c7-a8108bffdd0f | -9.69594 | -69.09075 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e66a1fe5-2626-391c-9569-3f0ab8621f45 | -9.34776 | -68.9224 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 82e002a9-bf09-3981-9968-963fe6d58743 | -9.42276 | -68.84624 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c19a7dee-2d7d-34ba-99f2-310ea6b63522 | -9.77194 | -65.01553 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0cc1c054-a6d2-3d63-bde9-a61556f2a5dd | -6.46147 | -55.45506 | 2026-10-05 17:37:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| d20167b9-d075-3c30-b03a-1bc14ad2f422 | -9.12529 | -67.82517 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 8a38bc39-b7fa-3779-a310-d73eb1af2b7d | -9.10382 | -65.35896 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 8416b4e3-20db-3cb2-8c3e-8bddb26929ee | -8.92545 | -66.86057 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 4085353d-dd96-3f58-b498-361c364ce635 | -1.51966 | -55.80791 | 2026-10-05 17:37:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9a6f4070-59b1-31ef-9cd7-4bdde7946c89 | -8.72568 | -68.90014 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 25.6 |
| abeabe88-df8a-353f-912c-36a6d72b536a | -10.40766 | -69.70371 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 11.2 |
| e88abb28-7891-3918-b989-ea9933754256 | -2.55578 | -58.04498 | 2026-10-05 17:37:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 99765496-da00-3f52-a5fc-c8e23a491e4b | -2.77155 | -57.65048 | 2026-10-05 17:37:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| ea5f6ab6-c127-3632-a899-3b20f4251430 | -9.48695 | -63.95014 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 6abb79f2-3a82-36ce-ab28-22743f0f8ca3 | -9.13607 | -68.24998 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a41aa304-5b2e-38ea-ad8d-e933e2885d09 | -9.06412 | -66.0963 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 21685739-53e9-309e-9330-0460273555b5 | 3.51638 | -51.50484 | 2026-10-05 17:37:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 1b269964-d933-3308-bf94-64f1cd544015 | -9.34015 | -64.71523 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fe380a70-444c-3672-8125-562776fcd1dd | -7.23088 | -55.19153 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| d8949586-41ec-3aea-88b4-d6d571b4b2d4 | 1.80849 | -55.54723 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| d5ea69c2-f335-3ca3-9a2e-7c647bc55407 | -9.4002 | -65.89949 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 2ab5b13e-86bd-3729-9e7b-a2a700b7ec70 | -9.08127 | -66.08946 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| ebaa2d0a-10a4-30cc-a7bf-ce8cf0c6394c | -2.95942 | -59.3212 | 2026-10-05 17:37:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 40368d2d-fd13-35a8-b98c-19ecec64f5ea | -8.61917 | -66.97933 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 34f280a9-8d00-3072-93ac-e4ed111eba40 | -9.48763 | -63.95502 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 425ea602-61be-322a-b484-f8b994bcdeaf | -9.8206 | -65.01964 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.1 |
| af4009c2-660a-3140-af60-1915ad3bc4cd | -8.8478 | -70.59642 | 2026-10-05 17:37:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 6b1a07c5-8e6a-334c-8422-bef5920ccdb2 | -8.69412 | -69.42022 | 2026-10-05 17:37:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 43f82ff0-2e26-3c28-84d4-5d97e74b9eb6 | -2.37081 | -55.27528 | 2026-10-05 17:37:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7b117903-c696-3049-8403-8b9740841478 | -10.14416 | -68.39685 | 2026-10-05 17:37:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 13dc85ce-400b-33ac-8602-10508c01b226 | -10.0781 | -69.14147 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 799d38b9-6dbb-3d7b-9935-c090c6311dc0 | -9.10606 | -64.37264 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ebd60260-4ec0-3bdc-be9f-b8b54fb55439 | -8.93232 | -67.34646 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 571f1c8a-8ae9-367b-9835-48a9166bf8e6 | -7.22122 | -55.18226 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| d85e11e7-400b-38a1-b6d2-5c16bb45d592 | -9.77496 | -64.97616 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 324a8734-1ab9-35ce-9941-a67d61ff5ba6 | -2.60678 | -59.41676 | 2026-10-05 17:37:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| eb0b0366-949e-33f0-9ea5-efdd25bbc7bc | -9.5538 | -68.45833 | 2026-10-05 17:37:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 27.3 |
| a0488784-1581-3e80-81b8-f28e1da02a1a | -9.3364 | -68.79469 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 1c61b2fa-8b28-3a4e-9952-54d2735b9124 | -8.66525 | -66.93271 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 21559568-046e-36de-8472-c92749f8a047 | -8.75169 | -69.09278 | 2026-10-05 17:37:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 73dfe66d-1066-31c9-959d-8fabc32e7feb | -10.78128 | -69.52342 | 2026-10-05 17:37:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 68.9 |
| b753d430-d526-355a-b40b-40dec3a29a37 | -8.59686 | -67.13594 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 681c04de-f554-38dd-a1e0-2e7ae7d5b95c | -9.52712 | -68.25065 | 2026-10-05 17:37:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 038792c1-b93b-32fd-a868-5230a0fa5187 | 3.4486 | -60.40464 | 2026-10-05 17:37:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ebfec46c-0db5-3504-b9c1-8b197b59c825 | -6.72073 | -55.07699 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 62cdc7cc-86d5-3f67-a9ec-2ea04d58f56f | -10.10495 | -68.26022 | 2026-10-05 17:37:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 061b578a-54bf-3615-8272-6a886517d694 | -9.91553 | -65.01888 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c0820983-cf01-3360-ab4e-ce2a24fdfaff | -2.56295 | -57.97217 | 2026-10-05 17:37:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README143.md)
