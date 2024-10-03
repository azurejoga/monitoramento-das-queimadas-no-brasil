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

## Dados Diários - Página 164

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8e35bdad-e173-3380-b522-116b5138f14f | -9.73912 | -59.12812 | 2024-10-03 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7ceef22-d361-3cdf-963d-bb51dc5f40eb | -9.56633 | -59.10452 | 2024-10-03 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b829bce-bfd8-3d4e-9c81-df020c0dbd99 | -9.51468 | -58.97768 | 2024-10-03 05:16:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b5e3038-5831-3556-b7eb-4bccd07b6783 | -9.46715 | -58.97736 | 2024-10-03 05:16:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e8dfa6e2-d90b-3bc3-9c94-30f413434743 | -9.46438 | -58.97334 | 2024-10-03 05:16:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c2f9beba-a30d-3cdf-b174-531f9c3e7b16 | -9.46383 | -58.97684 | 2024-10-03 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8cd4d44e-4072-33e2-83a4-8c7b446d10d0 | -12.23288 | -59.24192 | 2024-10-03 05:16:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ec584eb-68c1-3dd9-83be-a72ef145dabf | -12.22954 | -59.24139 | 2024-10-03 05:16:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| da54c3f4-d7f4-3a51-8b96-eb73b0de7e94 | -12.229 | -59.24497 | 2024-10-03 05:16:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6342b8b2-f112-342c-ba59-181b221cafa8 | -12.11276 | -58.71647 | 2024-10-03 05:16:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3a54c9c6-f2f5-398a-b8ed-0023dd8a5d25 | -12.10994 | -58.71227 | 2024-10-03 05:16:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6bbf3426-179c-3532-9828-b4863a409444 | -12.10938 | -58.71595 | 2024-10-03 05:16:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 43f04131-690e-328b-a738-ce592e67dbae | -11.84854 | -59.07209 | 2024-10-03 05:16:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a0f3d177-f5e4-364d-b56c-0d9ef7112798 | -11.72668 | -59.13721 | 2024-10-03 05:16:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 79004cef-3484-3316-8409-3ea35d4516e4 | -11.68022 | -58.88738 | 2024-10-03 05:16:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 177decbe-90f1-34ea-bd47-adcb5057c6eb | -11.67967 | -58.891 | 2024-10-03 05:16:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d22c126f-6c11-370c-89aa-c1b462ec8339 | -13.03639 | -59.86517 | 2024-10-03 05:16:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7ac30885-bafd-3dfe-9d3c-6b181c7119dd | -12.94872 | -60.10178 | 2024-10-03 05:16:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 92f830e7-9d4f-3f05-9210-ae68f6384509 | -12.94817 | -60.10531 | 2024-10-03 05:16:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf7b9148-28fc-3f8f-8f80-06b174437c56 | -6.86039 | -59.6795 | 2024-10-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6020abeb-467e-3315-bc92-ff3e71652608 | -6.78637 | -59.89016 | 2024-10-03 05:16:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 248f5adb-d91b-3c76-9f4e-6f2af3d465ca | -6.71892 | -60.01336 | 2024-10-03 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7c53c730-0a5e-3214-8168-973f81461cc2 | -6.71692 | -59.12632 | 2024-10-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae0fd97c-1501-38ef-b09e-2ed79c4c27e9 | -6.71637 | -59.12978 | 2024-10-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f08323bd-8c7f-3d4e-a3a6-87813f5b4763 | -6.71361 | -59.1258 | 2024-10-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 27711fd9-456f-3bdc-9a62-90a269bc9342 | -6.71307 | -59.12926 | 2024-10-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a3978b50-3170-3c6a-a3c0-5c92845a12b6 | -6.71252 | -59.13272 | 2024-10-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b0383dbc-8e64-3cee-b79c-4962cfb6f952 | -6.70976 | -59.12874 | 2024-10-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8256dec1-7c22-3609-a806-344a2f528ae8 | -6.70921 | -59.1322 | 2024-10-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d0a870cd-5086-3d74-9b0f-20c2bc50ce46 | -6.70867 | -59.13565 | 2024-10-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4e21a614-e1e8-3a00-ac6a-3b3c8eb920b1 | -6.70591 | -59.13168 | 2024-10-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5915e24e-91c3-3373-aa71-4a80a1ce8fe6 | -6.64909 | -60.04957 | 2024-10-03 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fdc2e425-b228-3d2d-90fc-38df4e3c9eea | -6.64852 | -60.05311 | 2024-10-03 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6592051e-317b-31c4-bdee-c06255ce94bf | -6.64687 | -60.04193 | 2024-10-03 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 347ea3b0-e012-33b3-8473-6757da93cfef | -6.6463 | -60.04548 | 2024-10-03 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 32335c4b-4d9a-3b51-ade1-faef98444b31 | -6.64574 | -60.04903 | 2024-10-03 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44b237d9-51da-33e3-9f99-b4b51a175d0d | -7.47001 | -59.86276 | 2024-10-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 82ce2d54-8486-3f5e-a37e-13330c0726b1 | -7.4656 | -60.40637 | 2024-10-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c7285f26-6808-37d9-99ff-20dde8be1347 | -7.46225 | -60.40582 | 2024-10-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ca63c7d-9e38-3d45-8718-d437d70a9ae4 | -7.33217 | -59.89801 | 2024-10-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 520a6747-4bcb-3e9e-b7f1-28f3f0b772e3 | -7.32885 | -59.89747 | 2024-10-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b3a8ab71-fabc-3cf9-8ab7-367b1d74a5a5 | -7.19897 | -59.7939 | 2024-10-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5532433e-2807-3b73-87b6-c57c1fd8522e | -7.19841 | -59.79739 | 2024-10-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb2f69b4-bb11-3041-946d-7ab8eed6e731 | -7.19565 | -59.79337 | 2024-10-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b2084704-c512-3f93-91ce-4d5ac24f1287 | -7.19509 | -59.79686 | 2024-10-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| faab581c-e3ca-3960-9e17-1bffb9802d44 | -7.05613 | -59.30085 | 2024-10-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5fcee6f1-c370-300d-ae1f-8314f090059c | -7.05558 | -59.30431 | 2024-10-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| d234c3d9-c098-361f-aae9-c477e22c5426 | -7.01929 | -59.38382 | 2024-10-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 712de65c-38f8-34c1-a044-7adf7c86c892 | -7.01874 | -59.38728 | 2024-10-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9475f2cf-4e6d-3765-a1f9-0e1a3be31edd | -7.01653 | -59.37983 | 2024-10-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d722472c-b806-3c7a-b22c-ce717c4c5d65 | -7.01598 | -59.38329 | 2024-10-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 92968d9d-dd6e-358d-9977-3f0eda842e0d | -6.93545 | -60.04074 | 2024-10-03 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6a2a3075-dd48-3a5f-a7b1-56c5bad0138c | -8.73264 | -60.49161 | 2024-10-03 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c846aa63-f642-38e5-abe5-673ce06a5211 | -9.33704 | -60.38556 | 2024-10-03 05:16:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef597a2d-d640-3a27-838d-dd19f38489f0 | -9.26048 | -60.33315 | 2024-10-03 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f1726a70-9c8c-3d28-9acd-0e01e31e6d17 | -9.39296 | -61.05564 | 2024-10-03 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 29d5b046-d9cf-3c58-aaba-8a39d5c33b36 | -9.39076 | -61.04781 | 2024-10-03 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 416a5a88-6eeb-3e3f-8197-b65fa944f72d | -9.38958 | -61.05509 | 2024-10-03 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3baea471-ce50-30af-b1b3-6b84e1d0ee23 | -9.38679 | -61.0509 | 2024-10-03 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 9a0e03e9-98db-3881-8c59-093f18e376d6 | -9.38621 | -61.05453 | 2024-10-03 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8c9ce2e3-9196-382a-b370-0b3a8f203bbe | -10.38119 | -61.21198 | 2024-10-03 05:16:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 84ce97c2-4e02-39b8-b18c-e61c3d313ecb | -10.38061 | -61.21561 | 2024-10-03 05:16:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7ead38ce-a029-333c-97a6-c64916d87fc6 | -10.37782 | -61.2114 | 2024-10-03 05:16:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 10200ec3-9db8-3f32-bd80-a94281b2742f | -10.37724 | -61.21505 | 2024-10-03 05:16:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b130454-943b-33d1-8dad-9a222e2c89d3 | -10.19441 | -61.30848 | 2024-10-03 05:16:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ddac042-8c46-33df-b93a-aa7ec3be54fd | -10.19381 | -61.31216 | 2024-10-03 05:16:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24630cda-cd84-3cbd-ab1f-d0163fd73226 | -10.19043 | -61.31162 | 2024-10-03 05:16:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d12fe45-a997-394e-a680-9b971241fecb | -10.18983 | -61.3153 | 2024-10-03 05:16:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 468f4a50-5cfa-375b-880c-538051f04a31 | -9.98769 | -59.88275 | 2024-10-03 05:16:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3fdd9bba-db1b-37a9-a7cf-e786fce11f13 | -9.98714 | -59.88623 | 2024-10-03 05:16:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c320758f-e59c-3363-bb55-3f0d82abe834 | -9.92918 | -59.93066 | 2024-10-03 05:16:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| f4669d98-ecab-31ff-a165-869debf28bb6 | -9.92641 | -59.90516 | 2024-10-03 05:16:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fe32dfc4-bb41-37c6-9c79-d90dc392ab13 | -9.90768 | -60.0884 | 2024-10-03 05:16:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 86e6c7d2-3d9f-3762-9f63-43c6f7dde663 | -9.90437 | -60.08786 | 2024-10-03 05:16:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d4617cb5-f66c-3c30-b679-9ee55f5085ac | -9.90381 | -60.09136 | 2024-10-03 05:16:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5235c396-9ce0-33b1-9f58-d5714d3a1b0a | -9.85792 | -60.67669 | 2024-10-03 05:16:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d67a5f43-33d0-357f-9571-69e15027ce03 | -9.85458 | -60.67614 | 2024-10-03 05:16:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd608c76-e9c8-3d2f-ae3d-bd8e8936dda4 | -9.79598 | -60.47031 | 2024-10-03 05:16:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 50bea90c-7db0-3afa-bc1d-5e797db84179 | -9.78819 | -60.4763 | 2024-10-03 05:16:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8c120e9-9f05-3fee-ac64-1ca6cc44d0a6 | -9.78487 | -60.47577 | 2024-10-03 05:16:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f2888f2a-9c06-3b08-b761-952f979a4cb0 | -9.78154 | -60.47523 | 2024-10-03 05:16:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5d249ad2-31a7-3da0-9123-8c0486881cc8 | -9.78097 | -60.47877 | 2024-10-03 05:16:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76f0ae14-d580-3723-8d20-28c9955abe8a | -9.77764 | -60.47823 | 2024-10-03 05:16:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0cba82d4-99f2-364b-87d8-0057f5852545 | -9.77432 | -60.47768 | 2024-10-03 05:16:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 345eb49c-6306-33bb-84fd-b2f6df5011cb | -9.70976 | -60.7515 | 2024-10-03 05:16:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 10c0c3fe-137f-38e4-b54f-d0cd9e8e8bf9 | -9.39413 | -61.04836 | 2024-10-03 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f626b47-decb-3619-b80b-70bca28cfc81 | -9.39354 | -61.05201 | 2024-10-03 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e056ce2d-2d9b-3763-ac79-d04393b666d6 | -9.39017 | -61.05146 | 2024-10-03 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4916d753-a698-3b2c-bf01-a966d8c48dcf | -12.08993 | -61.19153 | 2024-10-03 05:16:00 | NOAA-20 | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ebca2f6-9058-3bd0-a31f-e2ae3c51c971 | -12.08935 | -61.19511 | 2024-10-03 05:16:00 | NOAA-20 | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ccee40a-c684-348b-ab44-d262a25a9cbe | -12.08878 | -61.19869 | 2024-10-03 05:16:00 | NOAA-20 | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c8f6e2c1-2d5d-3f5c-8692-480d6d7854b8 | -12.08659 | -61.19098 | 2024-10-03 05:16:00 | NOAA-20 | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec793e03-91c2-3181-ac5d-29e7cde66342 | -12.08601 | -61.19455 | 2024-10-03 05:16:00 | NOAA-20 | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa9d2091-bf9d-330c-8d16-f89d723cf5b8 | -12.05351 | -61.03496 | 2024-10-03 05:16:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 260cd5a5-08bd-3096-b8bf-06f75952bbb5 | -12.03783 | -61.23815 | 2024-10-03 05:16:00 | NOAA-20 | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b7cc6ae7-27a7-3367-b239-44a1b886c4a9 | -12.30506 | -60.75944 | 2024-10-03 05:16:00 | NOAA-20 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cab646aa-bf6f-38cc-894a-d23b3a9e2509 | -13.29316 | -60.78379 | 2024-10-03 05:16:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| eb5ecb7b-2de8-33ed-8e33-cbb01d3dd8e4 | -12.80357 | -60.48645 | 2024-10-03 05:16:00 | NOAA-20 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62f93bbf-fa15-3d70-81c4-76da85a8768c | -12.69411 | -60.81226 | 2024-10-03 05:16:00 | NOAA-20 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bbc2dcf3-4670-3652-b17e-ead92431123a | -12.65503 | -60.75862 | 2024-10-03 05:16:00 | NOAA-20 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README165.md)
