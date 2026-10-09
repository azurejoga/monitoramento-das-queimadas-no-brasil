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

## Dados Diários - Página 181

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 306d6d01-38ba-3d7d-8059-708c66ae853c | -4.98229 | -46.04683 | 2026-10-09 05:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bd7e9723-2877-381c-b5c5-75538963424d | -2.47701 | -56.09004 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c26852d4-23f0-31ba-8a53-75f152f20a51 | -3.27297 | -54.06157 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ddbfebfa-be0b-3618-8f00-fa7e62e8ac21 | -8.84405 | -61.46425 | 2026-10-09 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d0143c3e-d62d-3077-9c91-46cbd9d410dd | -2.48351 | -56.13281 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cd95b6bc-66a1-3ed1-b3b9-c897835302b9 | 1.31943 | -60.71273 | 2026-10-09 05:23:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ae037d4-be12-3b0c-af7e-08daca37df24 | -3.11431 | -53.788 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 27f27e16-5b03-3e46-aee6-1e7dde87bfd7 | -1.14745 | -54.2192 | 2026-10-09 05:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ff7fbaf7-5106-3db5-bd06-8f63312e674d | -10.249 | -59.02773 | 2026-10-09 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 22c4609e-8bc6-38e7-9ab5-c2e98a607a51 | -3.8044 | -49.94573 | 2026-10-09 05:23:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a4ac2df7-ed64-3169-8d77-35d9dd3d13ab | -3.26412 | -54.01571 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 46efe986-4ed0-39ab-b790-9ae3dd852c4c | -3.58706 | -54.66561 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a8513a97-3e3f-35c7-a572-2b496656b706 | -11.87181 | -47.381 | 2026-10-09 05:23:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 231016d8-e775-318b-be35-9e9ee7bb7e85 | -1.19811 | -55.68621 | 2026-10-09 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bec42ffb-2447-3249-8692-d65e1d15cbad | -3.71609 | -59.65183 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 080a2316-7dee-3fc3-8eaf-5f396dceede1 | -2.57813 | -56.17807 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7dd8aa07-e43a-3ef6-b1e9-0ae9ef4bff23 | -3.99421 | -56.26062 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3da1db6d-23b5-310a-ab04-a99e6aaddd8e | -3.09049 | -54.2955 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7f8eb106-bbce-3374-adc7-0181161551c7 | -2.63049 | -57.7145 | 2026-10-09 05:23:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f22d3b23-0258-3782-8717-26a6df59f565 | -3.35906 | -58.22173 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07bae23e-3ed1-3969-90af-16100003aa60 | -3.00172 | -53.91972 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 63f14d0b-3e44-3195-98a4-682f168e4ae1 | -3.64992 | -59.17181 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0936c7ae-f9a3-343e-8d7e-899b8065a6f4 | -4.8047 | -54.67218 | 2026-10-09 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ac0a49b8-79f0-3d49-b7be-7e814f28c610 | -4.63171 | -50.95409 | 2026-10-09 05:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9d9fc1e0-ef0c-33d8-b0ef-1a9e7b03f23b | -3.0962 | -53.93144 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7a68c18e-de5c-3f73-9837-b9a11c73f5ed | -8.96288 | -45.91629 | 2026-10-09 05:23:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 35bc74f9-2b49-3994-900b-f778494c1101 | -2.99241 | -54.77249 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7f987f70-3e78-34ac-96a0-71499cca6174 | -2.75266 | -54.10223 | 2026-10-09 05:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 25606f76-a8d1-3028-86cf-b9fc5f77ccb3 | -2.78007 | -54.07746 | 2026-10-09 05:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6262d5d6-1916-31e6-98e7-801f85721057 | -3.46282 | -59.57544 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f4a25fc-5781-3d3b-9508-39cb67bfaa4e | -3.17535 | -54.74732 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dc3b6aa3-8d7e-3ab5-91f6-3e34d53c146e | -3.96468 | -60.00815 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3cc2bfc-229e-34b8-9e47-cc9d8fdb6dfe | -3.14543 | -58.56119 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1cb868d0-45b3-35eb-9140-115c01b7bc1f | 0.54004 | -50.89719 | 2026-10-09 05:23:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| de6b8a9e-17aa-390b-9add-71768adacf2f | -2.92149 | -54.13314 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3a427619-eb1a-3b1a-ae01-a059abd4b2a5 | -2.98735 | -54.13834 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0bb5009a-baf6-31c3-a426-a55e3ec60659 | -3.10015 | -54.27992 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0e41aa37-db0d-36d5-952e-bbe548ca709f | -3.78746 | -59.37537 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 766910d9-9911-3d50-b4ea-5a84c48fda87 | -3.01079 | -54.06424 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3a3cbffe-80a8-3d71-9f24-7c69e0321e09 | -3.9456 | -55.84751 | 2026-10-09 05:23:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3490a059-4d48-3adb-ad8e-93e1a23fbaf8 | -1.1907 | -55.66562 | 2026-10-09 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1fa3f704-1277-3add-b8b6-9d37406ce558 | -3.10601 | -54.1895 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 72e2edf3-6a90-3c3b-bd77-5d8b3ca05709 | -8.34492 | -62.82321 | 2026-10-09 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b2fdc37-06fb-370d-89e5-0aad2fb849dd | -3.01205 | -51.01957 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 18c7382e-5644-39db-a4ca-9499efea0dd9 | -3.21007 | -50.55794 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 05afd982-c523-3b76-997f-998d412a0407 | -11.90696 | -46.56931 | 2026-10-09 05:23:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1c01b6e6-de8c-3730-808e-31a9c4669533 | 1.31942 | -60.71273 | 2026-10-09 05:23:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f3b17ae-c24a-3961-a249-2d18fb44d74f | -9.26194 | -60.88095 | 2026-10-09 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b0946d55-86eb-3727-9284-fe615e41672c | -3.24861 | -50.40583 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dfddf28a-10fc-3061-a044-7a1a7064cffe | -3.28549 | -54.08307 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5440c4b3-13e0-302e-8073-b59661850981 | -3.35128 | -50.40604 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 38f8cd0f-8cba-30b5-9c54-ef7fea7eda66 | -3.49988 | -59.2832 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86992084-7744-3bce-9afd-a7b5c32c3a94 | -2.49745 | -56.06561 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d874408a-caaa-3dda-836f-a776f20fd88a | -1.24969 | -55.77813 | 2026-10-09 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 662d29f0-7de3-32e6-b9b1-f80c84d50b8d | -3.38046 | -59.43274 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bb02907b-bc8a-3985-a850-06feaba860e2 | -3.72527 | -59.44433 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6de8a5e8-00b9-3a89-980d-8713f0657b16 | -3.48432 | -59.188 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e761b3fc-8b2e-3ced-b35a-855343f3dbe7 | -2.47368 | -58.08197 | 2026-10-09 05:23:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f0105355-b4cc-301a-8ef3-1585920065e9 | -1.36755 | -55.60501 | 2026-10-09 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| fdebb78c-8bd9-3123-98cf-9f4657aa307c | -4.38717 | -55.44872 | 2026-10-09 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 978a63eb-c522-32d3-87b9-434f74b09cfc | -2.99816 | -54.75996 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 821fb246-770a-3a6b-a986-a9462390b516 | -3.13747 | -54.36608 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 82f1305b-2648-3976-b16b-71a4a6ee2cfe | -2.87836 | -54.19107 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 74b16bb7-dc1c-3504-a763-8aa5acd79793 | -2.46666 | -56.08845 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fd789cbd-0d9f-3300-9ae7-3b4a31640724 | -3.20773 | -53.85937 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 39d65fce-311d-3d30-a602-0e856e9ec9ee | -3.58935 | -54.57169 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e76d596c-1314-3188-9ef3-2b270f7cc71c | -2.02964 | -55.62793 | 2026-10-09 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f1211b82-5e77-3225-8f3f-992c78507c3f | -8.14298 | -64.11453 | 2026-10-09 05:23:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e7178f88-8aaf-3720-ad63-cf0504aa4938 | -6.85668 | -59.04693 | 2026-10-09 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d5c5129-37ea-3c37-8c0c-c42b97f05dc2 | -5.10412 | -46.22352 | 2026-10-09 05:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6d1c37b8-d12c-3a2c-bd28-e3d1254e67f3 | -3.18487 | -58.63441 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 65ff18b7-9295-3bf2-900f-81f9eab99b93 | -9.694 | -58.08825 | 2026-10-09 05:23:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 278a5873-5c3c-34e8-86c7-121854ec55d1 | -3.59311 | -54.57228 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 665de1cf-283c-3ce8-ade0-704cc2730f4a | -9.09163 | -61.01468 | 2026-10-09 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6d31751-b4ab-3da1-8def-3ad35733768d | -3.23572 | -58.74118 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23553a84-5342-3cd0-9674-c96bd8b938c8 | -3.0827 | -54.395 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 657ce42e-0849-38ed-ab3a-df532d36b2c2 | -1.761 | -55.28312 | 2026-10-09 05:23:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3447a45b-86ed-36e1-aba7-8733dea450d9 | -2.98399 | -54.08447 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a824e79c-e109-3f83-aec0-6b739c58bb12 | -2.8557 | -59.2707 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30c0d8df-9d36-38be-b24f-fe2fbbd8af87 | -3.25588 | -54.04389 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 2df8d97c-0dcc-3b32-80a8-7774e6b21cfb | -2.76724 | -54.10924 | 2026-10-09 05:23:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 22e13e3a-b100-31a6-b60f-33502efac4d3 | -3.19132 | -50.54955 | 2026-10-09 05:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 72ed3801-64d9-302b-a238-61dee82bcc06 | -8.75496 | -62.61769 | 2026-10-09 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c4458bb7-93df-3b80-a56f-7bc8d95619e7 | -3.57107 | -54.69543 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 4b2f619a-cfa1-3ded-a8a6-a109d25dfe76 | -9.29129 | -60.52977 | 2026-10-09 05:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5814944e-fbaa-3a45-9e71-e48aafd1b213 | -3.03868 | -54.09993 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 59871823-c9f1-3783-8974-5aa9023b076e | -2.93328 | -54.08162 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5ba82b62-9b17-3eb3-b626-d863679fe59b | -3.93012 | -56.04222 | 2026-10-09 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 756596ec-dbf8-3c56-b3fc-40cb01023968 | -3.10254 | -54.28982 | 2026-10-09 05:23:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c16ccbb6-fc17-30e8-9563-6eeaef797f3b | -6.94021 | -59.09954 | 2026-10-09 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7bbf5101-1099-3f9e-9ade-fe66cd3214f0 | -2.90016 | -59.22757 | 2026-10-09 05:23:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63664d97-cb8d-35c0-bfcb-3708b264f53d | -3.12106 | -54.16771 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| d980fe93-6c96-308d-b8ac-2370c1e793db | -3.10884 | -54.17077 | 2026-10-09 05:23:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5060e384-1024-3312-a47f-9b512bfebffb | -2.5644 | -56.15689 | 2026-10-09 05:23:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| db15a527-89d6-3dc9-99e1-ebba01c2c9a1 | -1.1848 | -54.17505 | 2026-10-09 05:23:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f39a6120-0b6f-30dc-a510-f606101f8e97 | -3.10022 | -53.95683 | 2026-10-09 05:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bf60e3c4-7b91-3aed-b75b-1ef61bbbd0d2 | -3.98344 | -56.11401 | 2026-10-09 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 23ff49d9-ed1d-3427-8bc9-2691cbc49403 | -3.46004 | -59.57138 | 2026-10-09 05:23:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f9a866f9-45df-3093-8b2d-807a1787a444 | -3.53392 | -54.65588 | 2026-10-09 05:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c0a5ed4a-0fbe-305c-945c-ef00d4eb6e5d | -3.72476 | -59.40483 | 2026-10-09 05:23:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README182.md)
