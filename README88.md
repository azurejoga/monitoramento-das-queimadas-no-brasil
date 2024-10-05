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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e2e70e29-7d62-30e5-a28b-8285b1b53c08 | -5.71109 | -44.81591 | 2024-10-05 04:36:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 688b8968-b3ef-31bc-8c6b-9e883e182294 | -5.70928 | -44.81803 | 2024-10-05 04:36:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0006f3b5-ca33-3fcd-bc5c-2c839f726d25 | -5.53694 | -44.3162 | 2024-10-05 04:36:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba100de7-8bbc-3bfa-ae21-1ba22e2ff072 | -5.44496 | -44.0445 | 2024-10-05 04:36:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8dcf4f2-dac7-35a1-a5e5-72c3be4353e7 | -5.88976 | -43.87487 | 2024-10-05 04:36:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f1d60ce7-9fb1-322e-9dbc-33da0e3a724a | -5.85441 | -43.82784 | 2024-10-05 04:36:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c58c7f6c-b1a9-32e0-9f93-eef28b7cdd63 | -6.2911 | -43.85233 | 2024-10-05 04:36:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e1ba16f9-5152-352b-9fc6-6d835baeb7b6 | -6.43552 | -44.03606 | 2024-10-05 04:36:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 43f2cf94-5dd6-3018-bd42-9d943df38ce3 | -6.42178 | -44.07226 | 2024-10-05 04:36:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 50a09fed-9dac-3231-9071-1441d9776312 | -6.18338 | -44.13842 | 2024-10-05 04:36:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a59e25e3-b3a9-3396-af89-0830d6665f16 | -6.17214 | -44.13001 | 2024-10-05 04:36:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 80df43fc-a4aa-3c58-a2a5-446b8879cecc | -6.16756 | -44.13289 | 2024-10-05 04:36:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 04beb9cb-6589-3c38-9266-306a2c3e2cb3 | -6.16147 | -44.14613 | 2024-10-05 04:36:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4d67037a-9a9c-3a7d-a736-d023395e67ee | -6.07936 | -44.70639 | 2024-10-05 04:36:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ddd5190-65b2-333e-9224-91942a8ab3d3 | -6.07545 | -44.70575 | 2024-10-05 04:36:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 19b9c53f-9c3f-3c5b-a0ab-6615c8d47447 | -6.06167 | -44.88016 | 2024-10-05 04:36:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 62a7b279-ef6a-387d-b167-5633f2a19c9a | -5.82392 | -44.12542 | 2024-10-05 04:36:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| eee59069-1cb8-39d7-ab9e-0b482aadd836 | -5.8234 | -44.12901 | 2024-10-05 04:36:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 4acc00e4-e22b-3089-af72-ed93a16fb01b | -5.81934 | -44.12841 | 2024-10-05 04:36:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 824f5056-076d-37f8-a5f7-dd2ea95e07a4 | -5.81529 | -44.1278 | 2024-10-05 04:36:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6dadb44c-ac4b-386d-be7a-ba5e2e1a338d | -5.71567 | -44.81165 | 2024-10-05 04:36:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 64de2805-1917-38d0-b629-323f6b6f952d | -5.71497 | -44.81648 | 2024-10-05 04:36:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 873a3db1-c178-3b2c-8793-6e2b063bef25 | -5.6324 | -44.32024 | 2024-10-05 04:36:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2b978421-d431-3e6f-a312-71a76e1f3f4a | -3.39767 | -45.28304 | 2024-10-05 04:36:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0b60b6fd-e9cd-3ae9-8c1c-8e18e74ddf73 | -3.39701 | -45.28732 | 2024-10-05 04:36:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 39f20fe3-c405-3226-a5fe-f15128ec3cf5 | -3.39401 | -45.28248 | 2024-10-05 04:36:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b63a643b-bca4-3fc6-8f77-a827bc5b0666 | -2.90989 | -45.89301 | 2024-10-05 04:36:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 487601e0-f88d-3cef-abe1-8f71613e9fb6 | -2.61178 | -45.33748 | 2024-10-05 04:36:00 | NOAA-20 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6cdf8cf5-a8e2-35f2-9a56-e258eb8caea0 | -2.52989 | -45.80164 | 2024-10-05 04:36:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 580e0eab-07d6-3fe1-847b-25bc99904174 | -2.52636 | -45.80109 | 2024-10-05 04:36:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 05c43521-9be6-3b2b-857d-707c2770d212 | -5.04814 | -45.39595 | 2024-10-05 04:36:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1bf7dd99-9929-3ec6-8741-dd42e89e506d | -4.92219 | -45.67999 | 2024-10-05 04:36:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b0ab977a-87db-3ab2-a3cf-c134ad6ed851 | -4.87619 | -45.9661 | 2024-10-05 04:36:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d026bc99-45db-30c4-8f0f-5cb303aca1d5 | -4.86293 | -45.84771 | 2024-10-05 04:36:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 397a5ea4-45ab-3321-b890-2de6bba2512e | -4.85867 | -45.85136 | 2024-10-05 04:36:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a51b1e0-e050-3a0d-98e6-434b3ce86204 | -4.69163 | -45.87374 | 2024-10-05 04:36:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8a4bc45b-6d06-3c60-ba0c-9b066b782793 | -4.691 | -45.87793 | 2024-10-05 04:36:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f453a4d3-577b-39ac-ac37-e6997c3e6aed | -4.68802 | -45.87324 | 2024-10-05 04:36:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 185aa103-0d2a-3799-aeec-3a699d9b30a6 | -4.68318 | -45.88099 | 2024-10-05 04:36:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b87a33d-5a68-38d2-9789-9e5d7bc21f5c | -4.67958 | -45.88043 | 2024-10-05 04:36:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83dcc697-3b95-39f6-a619-da84beb17050 | -4.67303 | -45.87498 | 2024-10-05 04:36:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ffe2c85e-6b59-3287-8424-967498fc7961 | -4.67114 | -45.87562 | 2024-10-05 04:36:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 24a3d2bf-f69c-3686-99e5-3ee8dbf86d0d | -4.59724 | -45.60518 | 2024-10-05 04:36:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 55244a5c-5d5d-3c59-978b-ed79b7b45659 | -4.41907 | -45.379 | 2024-10-05 04:36:00 | NOAA-20 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7a189add-611c-30cf-855a-a2c18695c557 | -4.36472 | -45.6337 | 2024-10-05 04:36:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0d31c52f-30e1-3609-8f8f-fb7e894785b3 | -4.92583 | -45.68053 | 2024-10-05 04:36:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b027a4e8-04a2-304f-81db-8412e0efe3e4 | -4.92284 | -45.67812 | 2024-10-05 04:36:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 95a59dcd-8ec4-3271-a8bc-ec2d03e844fe | -4.79088 | -45.26188 | 2024-10-05 04:36:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 51580e6a-d792-30d4-8048-39470252297c | -4.6874 | -45.87739 | 2024-10-05 04:36:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 21b88484-0088-3ae8-a0e2-1bb9a43ab729 | -4.68021 | -45.87624 | 2024-10-05 04:36:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e443a12b-0849-3566-acd4-cbf34206607d | -4.67831 | -45.87689 | 2024-10-05 04:36:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb9de321-622c-33c3-87cf-55e8382641d8 | -4.67662 | -45.87561 | 2024-10-05 04:36:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c19fca6c-61b4-38d6-92db-9e0eb15ec6a6 | -4.67473 | -45.87625 | 2024-10-05 04:36:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f937a021-7d07-33a2-9909-33bdd4906a1a | -4.49933 | -45.90576 | 2024-10-05 04:36:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bcc9243d-cc20-3386-9013-caf69636d9d5 | -4.41538 | -45.37848 | 2024-10-05 04:36:00 | NOAA-20 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b2dcb8c-ce3b-3858-992a-88061df143a4 | -4.4117 | -45.37794 | 2024-10-05 04:36:00 | NOAA-20 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7261d448-fb87-3d95-8b1b-58f52dc6b3f7 | -6.17981 | -45.439 | 2024-10-05 04:36:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| fa0cb002-70a9-356e-8cf9-45baa53dc259 | -6.17606 | -45.4384 | 2024-10-05 04:36:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 80a5bbdf-cfe7-3074-bf7c-0e5cce57177b | -6.1754 | -45.4429 | 2024-10-05 04:36:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c9b9bdc2-610c-35ff-a554-af6db79e4925 | -6.17232 | -45.43778 | 2024-10-05 04:36:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 9664baa6-68f4-31d6-b94f-7abdf581df0e | -6.17165 | -45.44228 | 2024-10-05 04:36:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 660e9efc-eb9b-31b7-9330-ac4fb7aa4a1a | -5.99328 | -46.01483 | 2024-10-05 04:36:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 85a7686c-5a1e-3296-aa52-0e25aae043cf | -5.97336 | -45.37091 | 2024-10-05 04:36:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 085a2c14-7e26-3a33-a8a5-68be8e17087d | -5.89812 | -46.29029 | 2024-10-05 04:36:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5d6c88d9-53ee-302f-98d7-07e5bdba21e7 | -5.89455 | -46.28973 | 2024-10-05 04:36:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 297aa647-a3f7-38b2-89a3-5b01f11833f5 | -5.89161 | -46.28511 | 2024-10-05 04:36:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b5323748-7e33-3f39-a70c-5a786e84c080 | -5.79355 | -46.45181 | 2024-10-05 04:36:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 52b6a83a-c816-3704-86f3-95e63774ce7c | -5.78413 | -46.44216 | 2024-10-05 04:36:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7bbb5869-c65f-3e58-a1e7-ef5a52028085 | -5.7814 | -46.43875 | 2024-10-05 04:36:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0456f5ba-e8b4-37b8-b93e-fcbf7d66ae2b | -5.76699 | -45.0655 | 2024-10-05 04:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5d8ce195-2af2-3759-a885-63f2a8b836da | -5.76387 | -45.06752 | 2024-10-05 04:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b5dbdeac-c28d-3783-8ff7-77a8a9d84114 | -5.66505 | -46.34761 | 2024-10-05 04:36:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 09d22f00-a026-30df-8c08-9496233d5a35 | -5.64482 | -45.82121 | 2024-10-05 04:36:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 01d65ebc-097e-32a7-a47d-1aa8ad61294a | -5.38535 | -46.42623 | 2024-10-05 04:36:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2dd0ccb3-acd1-33b8-a0f1-833a34fcccba | -5.38313 | -45.69809 | 2024-10-05 04:36:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 190773d5-0b22-3219-b40b-44db0e87034f | -5.2054 | -45.48858 | 2024-10-05 04:36:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 31d0fab4-056e-3835-a21a-0d5366de539c | -5.15695 | -45.24194 | 2024-10-05 04:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 21fc84bb-df64-3cbb-a44b-1b0ed4cb050d | -5.09155 | -46.12217 | 2024-10-05 04:36:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a4f70028-5c74-3d2b-ba3d-649ef42686a1 | -5.08859 | -46.11756 | 2024-10-05 04:36:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1263188a-1f2e-3112-b89d-c9a01ab79acc | -6.18049 | -45.43443 | 2024-10-05 04:36:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 704122d5-5a25-35a3-9a73-4e5613790713 | -6.17674 | -45.43383 | 2024-10-05 04:36:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 68b9438b-89ee-3c03-8a16-ee28557dcd9c | -6.09553 | -45.9556 | 2024-10-05 04:36:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fa46c6d7-cd98-3178-9b02-4bc4cbf2595e | -5.89518 | -46.28567 | 2024-10-05 04:36:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1c19bbe0-9a59-325b-9b04-52bb8b75da6d | -5.89223 | -46.28104 | 2024-10-05 04:36:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 49c0a473-4a1c-3ef9-9b28-dae15566f97c | -5.78494 | -46.43929 | 2024-10-05 04:36:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eccd1068-d302-35ab-a4a8-923b09fd5009 | -5.76768 | -45.06807 | 2024-10-05 04:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f7c0bf6c-d200-3a94-89fa-157880606209 | -5.72626 | -46.49134 | 2024-10-05 04:36:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f333e26-e4e7-3f5d-92a1-dfd687fb268e | -5.50253 | -44.9759 | 2024-10-05 04:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6484e4a0-f039-3238-ac79-e98fe3b10649 | -5.38182 | -46.42572 | 2024-10-05 04:36:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 527f0ea7-c8a3-391f-81a8-22bf7401a56c | -5.36472 | -45.89477 | 2024-10-05 04:36:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e7ffe61-08ec-3e9f-9e8e-b406c75e7547 | -5.15321 | -45.24133 | 2024-10-05 04:36:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 88baf9c1-d5a6-3738-9031-e51d09d0e0ae | -5.13143 | -46.12417 | 2024-10-05 04:36:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a8c378c-4df0-3807-ad9e-91cb94f1ae76 | -5.12786 | -46.12364 | 2024-10-05 04:36:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb27ee4d-794a-3911-ae5b-01dd3145691c | -5.08798 | -46.12159 | 2024-10-05 04:36:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65ecffa8-ca6b-3273-bf4f-594efbd2420a | -2.00466 | -46.57463 | 2024-10-05 04:36:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2688f587-2a45-310b-ba83-5cd914b2b8d2 | -2.00409 | -46.57829 | 2024-10-05 04:36:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f43e84b-9606-3461-bdab-e7834e3c809b | -1.93079 | -46.57451 | 2024-10-05 04:36:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| af994590-3901-342f-92bd-a79e16bc4707 | -1.19893 | -46.59007 | 2024-10-05 04:36:00 | NOAA-20 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fc9de20b-e7a4-3cbc-a253-3f4e9bcf1b6d | -1.19554 | -46.58954 | 2024-10-05 04:36:00 | NOAA-20 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2709a139-248f-3903-8129-a763557a71fa | -3.0592 | -46.50887 | 2024-10-05 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README89.md)
