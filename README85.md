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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e66f939d-349d-30d6-a176-e53af1c5decd | -4.5577 | -43.0928 | 2024-11-02 05:15:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| bf805898-4789-3077-a6db-c8e5287f69ce | -1.17411 | -53.62944 | 2024-11-02 05:25:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8979009f-d3ba-3a22-9d3d-fbf795c65c51 | -1.17078 | -53.63108 | 2024-11-02 05:25:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8970aad9-3dec-394f-b8cc-05debebeb76e | -1.16933 | -53.62918 | 2024-11-02 05:25:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0e3937f5-c630-3cf3-a5d4-2c20c9726897 | -1.16788 | -53.68193 | 2024-11-02 05:25:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b75049da-fbd4-32d1-b77c-247cc3be32c9 | -1.16706 | -53.68733 | 2024-11-02 05:25:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d52b1b0-a6a8-3458-8627-f043f19cf7b4 | -1.16519 | -53.68528 | 2024-11-02 05:25:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fbc150e0-fbc5-3e4b-9375-c62befbc9d83 | -1.08868 | -53.65239 | 2024-11-02 05:25:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1ef26c0a-612d-37c3-a6f1-cc49d959020d | -0.98762 | -53.70635 | 2024-11-02 05:25:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9d5959a0-1c3c-3df5-ae1c-74aa7b436ce3 | 3.32028 | -59.91082 | 2024-11-02 05:25:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c0e3ab4e-34bb-34fe-84b2-077fa160bbb9 | 3.31697 | -59.91134 | 2024-11-02 05:25:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 604fd296-5017-3d6c-a3a7-ee3c7c173d55 | 1.05415 | -59.72782 | 2024-11-02 05:25:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 74c9aa13-0192-34a2-9c9e-deb265eca46f | 0.59516 | -60.46709 | 2024-11-02 05:25:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49ecfc50-7289-3bad-b69a-b9fa671c1be4 | 2.98746 | -61.20076 | 2024-11-02 05:25:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2776722c-286f-3e8b-a720-8e0959b9a2a2 | 2.58094 | -60.6982 | 2024-11-02 05:25:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d0231f7c-57b4-3e29-b1c6-0749cd99ca43 | 2.57761 | -60.69871 | 2024-11-02 05:25:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a98eed09-4d65-36b4-bcb1-fce75927e7a5 | 2.57706 | -60.69525 | 2024-11-02 05:25:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 923eb977-608b-3666-8bdf-f6f3a4c3346c | 2.22628 | -61.67317 | 2024-11-02 05:25:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2de2f5c0-1000-338c-8962-b71b6da3e94c | 1.38549 | -60.80309 | 2024-11-02 05:25:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 63205fee-9182-361f-95c9-88e0940a4a5d | 1.38217 | -60.8036 | 2024-11-02 05:25:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b3ccdb3-0246-34df-93fc-c6dd365f6450 | 4.38341 | -60.69855 | 2024-11-02 05:25:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3c45cdc1-01a5-39d1-b8db-77a74401e3be | 4.38184 | -60.69913 | 2024-11-02 05:25:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd327852-55e7-3875-805d-7d3f0fcaca3b | 4.37849 | -60.69963 | 2024-11-02 05:25:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f53bc2a-11ef-30da-83a1-1df9058d4413 | 4.04273 | -60.22197 | 2024-11-02 05:25:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3c793aff-f565-3b35-a96e-2d2bf7188959 | 3.93309 | -60.54193 | 2024-11-02 05:25:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e17a47a1-517d-35a2-934d-d0e471818e2c | 3.52174 | -51.27829 | 2024-11-02 05:25:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1a7e6f1-e658-31f7-8462-4bf8955873e2 | 3.52123 | -51.27526 | 2024-11-02 05:25:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1aa2c787-8ce7-381d-9873-44624e3d13cb | 3.51816 | -51.28824 | 2024-11-02 05:25:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 930846e5-c90f-3300-a55a-da1fb30cd153 | 3.51765 | -51.28522 | 2024-11-02 05:25:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51519173-2546-3eac-a81a-a47d777969e4 | -1.60821 | -47.21352 | 2024-11-02 05:25:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c09ee055-ff10-3e19-a3a5-006c19fa4d01 | -1.60713 | -47.2208 | 2024-11-02 05:25:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 0cdc323b-0709-3fdc-8f3f-c93ebc2c764d | -1.60591 | -47.21475 | 2024-11-02 05:25:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| cd9dc5ba-bcc1-3286-90ca-b15f4691613f | -1.60477 | -47.22209 | 2024-11-02 05:25:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 42633ef5-a5d0-3401-bf7d-130bbb272da6 | 0.08592 | -49.86224 | 2024-11-02 05:25:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a2cfc49c-014a-3f33-93cb-91263b452130 | 1.85179 | -50.50895 | 2024-11-02 05:25:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aaef4ab6-b071-31ea-a067-7c783f53ee7a | 1.85119 | -50.50527 | 2024-11-02 05:25:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 01b491ac-102f-33a7-a746-52477213d8b9 | 1.78904 | -50.43991 | 2024-11-02 05:25:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 71571a7a-4e67-3049-a2ea-090d77e623fc | 1.78843 | -50.43624 | 2024-11-02 05:25:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5ca8aeb8-06b3-337d-972a-0ade76e5353f | 0.10064 | -51.24679 | 2024-11-02 05:25:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7038411b-00ed-3a6e-88e6-999d4c90dfda | 0.10009 | -51.24336 | 2024-11-02 05:25:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d32da961-ec6d-3369-88bf-3eaa7b2342c3 | -0.15939 | -51.38342 | 2024-11-02 05:25:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca8cf149-bcac-342e-a1cf-739b9f57b799 | 3.36807 | -51.29677 | 2024-11-02 05:25:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8aea9de6-d964-3dd9-bdb4-ec9fa6c267cb | 3.36757 | -51.29372 | 2024-11-02 05:25:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3a75aa48-a0f9-395d-83f5-27cb2ffd42b7 | 2.58455 | -50.96349 | 2024-11-02 05:25:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fe7478e3-b950-304b-9865-59641586cd1d | 2.58401 | -50.96016 | 2024-11-02 05:25:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0530f5b3-be8b-3291-9ceb-b3f8e22a0bd7 | -0.74058 | -51.70185 | 2024-11-02 05:25:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dcbf1cb5-4cbe-39e9-9098-247dc83e383a | -0.74007 | -51.70517 | 2024-11-02 05:25:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 411eb36d-0dbf-3a07-b175-1a0432f89934 | -0.6845 | -51.69326 | 2024-11-02 05:25:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f6b3b28-ff52-3962-83aa-f6a15ca9c9a9 | -0.68125 | -51.67916 | 2024-11-02 05:25:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 47b7d2c4-4cd9-3893-8e0e-cfa2b76d9e87 | -0.68073 | -51.68248 | 2024-11-02 05:25:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5dfc29af-6e75-34ac-af1c-6d546f6aa8f8 | -0.68021 | -51.68581 | 2024-11-02 05:25:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f5f831e6-6043-35e7-8a24-6ff6f8cdfafe | -0.67969 | -51.68912 | 2024-11-02 05:25:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 986a0f8e-45ac-3c24-af8e-c461b7bcfbc8 | -0.67486 | -51.68502 | 2024-11-02 05:25:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 97f2571c-0522-332a-ab38-e228f5a6ddf0 | -0.12059 | -51.63126 | 2024-11-02 05:25:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0fccbbf-8bc8-394d-a244-abc5c4829756 | -0.96923 | -51.78264 | 2024-11-02 05:25:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 183bca28-e1c2-3e78-935b-c888110c6156 | -0.96871 | -51.78596 | 2024-11-02 05:25:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e08d58f7-82fb-3dcd-9d6c-f1cc64912441 | -2.2663 | -53.7422 | 2024-11-02 05:25:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 3b03158d-62ad-3762-ac1f-8193462e332c | -3.0726 | -45.1405 | 2024-11-02 05:25:23 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 1b8c572b-b046-3f0d-8b42-f29d72bc0831 | -3.0727 | -45.1179 | 2024-11-02 05:25:23 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 85c96cf3-f052-3833-a990-2f7023ae86fd | -3.1281 | -54.266 | 2024-11-02 05:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| d4e2ff26-f765-3e50-81dd-c62064baca50 | -3.2047 | -53.4179 | 2024-11-02 05:25:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| affe7ead-9f65-3500-b051-a42e07e773ad | -3.2231 | -53.3972 | 2024-11-02 05:25:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| dd57e9a8-88d3-3ee7-b5e3-d6a397cffb6a | -3.2415 | -53.4169 | 2024-11-02 05:25:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| eaf1d735-3925-3ce7-be98-ac9621c95515 | -3.2415 | -53.3967 | 2024-11-02 05:25:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 6296c328-eda9-3b18-ad0b-d9ed573b97cc | -3.2599 | -53.4164 | 2024-11-02 05:25:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 89.4 |
| a780b27b-febc-3d60-a7a1-024a771d0d1b | -3.2599 | -53.3962 | 2024-11-02 05:25:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 937f7fc6-0a59-34f8-8010-509d3e8dfd1d | -3.9473 | -48.3666 | 2024-11-02 05:25:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 2e516cf2-bc0c-3743-8fc7-562d76177b03 | -3.9474 | -48.3451 | 2024-11-02 05:25:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 965e354f-ec2d-3886-adb6-1d360178f222 | -4.3537 | -48.6068 | 2024-11-02 05:25:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 92ec9505-033a-3d63-b1b7-7503d5d99add | -4.5577 | -43.0928 | 2024-11-02 05:25:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 2c228b22-c2bd-3b20-82ba-85d5513cbbea | -2.85124 | -52.41548 | 2024-11-02 05:27:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 794608f2-6b42-34d1-a5e2-5f498376593d | -2.85098 | -52.41562 | 2024-11-02 05:27:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 46b84397-44db-3cef-9051-0701fbb3ff1c | -2.85075 | -52.41866 | 2024-11-02 05:27:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b0f1b474-7c68-386a-811c-b74b5b4e19be | -2.85051 | -52.41881 | 2024-11-02 05:27:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40c41944-1b0b-3ff2-bea0-d3492861e212 | -2.84065 | -52.87666 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 3f15f20d-ce5d-3c5f-80a2-3c95446ce784 | -2.8402 | -52.8797 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d0127d70-8938-3beb-b8fc-7aa4701c348e | -2.83974 | -52.88269 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 406bf88a-3246-37d1-a242-f0a2e473afbf | -2.83648 | -52.86977 | 2024-11-02 05:27:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0b04647f-3c55-3d3c-b82f-2bbd17fb2d89 | -2.83602 | -52.87287 | 2024-11-02 05:27:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 962072e9-1a55-3acb-94bd-6d54badb5835 | -2.83556 | -52.8759 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 1be59a0a-acf1-3895-b275-cf449341aad0 | -2.83511 | -52.8789 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| a5b06a2d-b346-3d62-b6a6-1cca4b789752 | -2.83094 | -52.87202 | 2024-11-02 05:27:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ca80ae20-8779-3759-868a-e65ce4a11094 | -2.81752 | -52.99567 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 76fdf6dd-ab29-34a5-aa55-707256aa1399 | -2.81247 | -52.99495 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d5622955-6ed3-35a0-9171-92277f6183ab | -2.812 | -52.99804 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a38919aa-0d58-30d4-908a-3aaca768c559 | -2.8074 | -52.99428 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 922d29fe-c1ec-39f6-bb3f-059cc141a821 | -2.80694 | -52.99738 | 2024-11-02 05:27:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dc9a6624-216a-32a4-bedc-d611852224c9 | -2.78549 | -52.89782 | 2024-11-02 05:27:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 868126a1-b514-37aa-a67a-fcaf0cbbffe8 | -2.78218 | -52.89674 | 2024-11-02 05:27:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 204df1d9-ad2a-37a9-8adf-1e3eda3e62bd | -2.78171 | -52.89973 | 2024-11-02 05:27:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| da68bcb2-b4c9-3de0-814e-2ad8f0fc0e9a | -2.7808 | -52.89438 | 2024-11-02 05:27:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 80024e20-133e-3495-b9a4-5dba82a2fcfc | -2.78037 | -52.89733 | 2024-11-02 05:27:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d2b0a3de-af33-3f2f-a3bd-3f59f00f2523 | -2.77993 | -52.9003 | 2024-11-02 05:27:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8a889b01-bb7b-346e-9807-fab09163fc20 | -2.77706 | -52.8962 | 2024-11-02 05:27:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a35feafd-891a-37b0-a3a2-ce77c00da488 | -2.7766 | -52.89917 | 2024-11-02 05:27:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b3abfc89-1299-32a1-9d81-bf0182714f5c | -2.67589 | -53.01785 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 80b88431-d9b3-36d4-a3f3-6f6644cada21 | -2.67544 | -53.02086 | 2024-11-02 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b8249cac-0ace-39cb-b02d-ce7b0f2fed85 | -2.31569 | -52.90845 | 2024-11-02 05:27:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 512e22e2-3f30-31ad-9635-1567dda5b7e1 | -2.31523 | -52.91145 | 2024-11-02 05:27:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 108378e8-57ad-3df9-b41d-51ca9d8ac84b | -2.24869 | -52.83892 | 2024-11-02 05:27:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README86.md)
