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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 26dc624e-70cb-356f-bbe2-77f84b59d885 | -1.85767 | -54.35038 | 2026-01-03 05:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d4053f0-8196-365c-bce4-f46412563a33 | -1.6898 | -54.04593 | 2026-01-03 05:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a7b8312e-8207-37d6-8dfa-4c0c53db9edb | -2.38949 | -56.0526 | 2026-01-03 05:27:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 045e2fce-2dfd-3e09-a544-9bfbaed92e4c | -1.96729 | -53.35987 | 2026-01-03 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 84e933eb-1a0f-3950-887f-5d6cf96634c5 | -2.719 | -54.54638 | 2026-01-03 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92d10a4a-b859-3f24-85a3-4445191fcfe8 | -2.38881 | -56.05706 | 2026-01-03 05:27:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74cf66a2-75a2-3e35-829e-3fa3cf990b89 | -3.16957 | -54.97731 | 2026-01-03 05:27:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 323a7c03-3a7a-3a6e-a6e9-0159733b2e54 | -1.66983 | -53.92445 | 2026-01-03 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d2e9ce8d-88ef-3151-b38e-854fd341b4f2 | -3.1701 | -54.9739 | 2026-01-03 05:27:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8787adbd-9393-371a-90f0-f5e2fefc626f | -3.86951 | -54.23244 | 2026-01-03 05:27:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1b34e766-7c0a-344b-89c5-69b9f1bebba8 | -1.67044 | -53.92048 | 2026-01-03 05:27:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1f4cfeee-5a33-3bc4-ac19-96984deebe0f | -2.72088 | -54.54684 | 2026-01-03 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a72b9f6-ab5e-3aaf-8280-c1ca5cefea1b | -12.14198 | -63.03817 | 2026-01-03 05:29:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 737eeb4c-12a5-3c6d-b4d9-74bd0cf7db55 | 4.33934 | -60.79792 | 2026-01-03 05:46:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 858c4064-9e86-39b5-9c95-e05f47d5f069 | 2.52285 | -60.9867 | 2026-01-03 05:46:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e4f312f-6238-3959-9aa0-e08d76d5ed44 | 2.56376 | -60.30597 | 2026-01-03 05:46:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa6eb8b8-bd54-3f8e-a5f1-81e6e1d9e914 | 2.55306 | -60.36423 | 2026-01-03 05:46:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf72db06-4d06-32b8-af97-584b7133aa84 | 2.54914 | -60.36492 | 2026-01-03 05:46:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 18119711-2891-3837-98bd-03bd7e2c9e4d | 2.52361 | -60.9913 | 2026-01-03 05:46:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c2131418-058c-3a03-a9db-5995ea86199d | 2.52339 | -60.98819 | 2026-01-03 05:46:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d45d1e54-ecc9-32ed-b2a3-4b61dec43bde | 3.11122 | -60.97875 | 2026-01-03 05:46:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5512ac1-f9ad-3269-a429-0ab332e16637 | 2.55699 | -60.36359 | 2026-01-03 05:46:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76269fea-85f3-3ae4-98db-b6df6e6fd75a | 2.52412 | -60.99281 | 2026-01-03 05:46:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1daaf7d1-8ce4-3bec-b273-6b30d37081f9 | 4.34234 | -60.79293 | 2026-01-03 05:46:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5152bcba-12b3-310f-83d9-c7e4e3c73559 | 1.28218 | -60.32692 | 2026-01-03 05:48:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c64bc92a-394e-3326-b744-b5e4c64f0de5 | 1.28162 | -60.32343 | 2026-01-03 05:48:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c316def1-328e-350f-98b2-a6301946dafb | 1.2862 | -60.32629 | 2026-01-03 05:48:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 764f99a6-67ee-3ac7-8880-e56c5c4af1ee | 0.46653 | -60.44087 | 2026-01-03 05:48:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8179b077-5a43-3b23-816e-44d25260b39d | 1.28274 | -60.33041 | 2026-01-03 05:48:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 84b55f3e-58bb-364e-b689-a68c8ba04eee | 0.46598 | -60.43734 | 2026-01-03 05:48:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 242bd14a-27bf-3bd6-bc4c-51445ccb3001 | 1.85087 | -60.84918 | 2026-01-03 05:48:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8aaa661b-10ae-32e4-a553-204fc9e868aa | 1.28676 | -60.3298 | 2026-01-03 05:48:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 1da1b5db-c335-33c1-bb0a-9e57f24ab9f1 | -1.66657 | -53.92739 | 2026-01-03 05:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2f69e188-d9e8-3021-aeb6-0fed689f875d | -1.68725 | -54.04839 | 2026-01-03 05:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab876999-0cce-34d7-a5f3-e545440e0cb7 | -1.68807 | -54.04316 | 2026-01-03 05:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f44cda59-e73f-3395-943c-2fb102f86f8d | -1.68933 | -54.04615 | 2026-01-03 05:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 928e0282-60e4-32f6-a85e-c85d14b577be | 1.28657 | -60.31995 | 2026-01-03 06:33:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 16e64222-5cd0-302d-923c-2d671ee59c94 | -1.66343 | -53.92087 | 2026-01-03 06:33:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a3447a96-0f12-304a-9f96-90bf29316000 | -10.29298 | -38.40027 | 2026-01-03 11:17:00 | TERRA_M-M | SÍTIO DO QUINTO | BAHIA | Brasil | 2930766 | 29 | 33 | nan | nan | nan | Caatinga | 17.0 |
| 521f7026-3ca7-3f12-9f8c-26c6e7d0609f | -9.85947 | -36.17146 | 2026-01-03 11:17:00 | TERRA_M-M | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| d78ba1f3-bbc2-3bad-97f2-f6a37bcbe10e | -7.16421 | -35.17558 | 2026-01-03 11:17:00 | TERRA_M-M | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| c65721dd-5ccc-33ce-a3ea-68b5c72db79c | -7.32728 | -37.29456 | 2026-01-03 11:17:00 | TERRA_M-M | BREJINHO | PERNAMBUCO | Brasil | 2602506 | 26 | 33 | nan | nan | nan | Caatinga | 10.6 |
| c239ebaa-d239-31a5-a102-d4b737572ce4 | -11.05822 | -38.09501 | 2026-01-03 11:17:00 | TERRA_M-M | ITAPICURU | BAHIA | Brasil | 2916500 | 29 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 538879bf-dff2-317a-b2c1-c3592d5976d5 | -6.53627 | -37.78654 | 2026-01-03 11:17:00 | TERRA_M-M | JERICÓ | PARAÍBA | Brasil | 2507408 | 25 | 33 | nan | nan | nan | Caatinga | 20.0 |
| c090256e-07cf-3cc6-8c9a-02a39683db30 | -13.7745 | -39.01268 | 2026-01-03 11:19:00 | TERRA_M-M | ITUBERÁ | BAHIA | Brasil | 2917300 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.9 |
| a2c18f34-7a69-3ca2-ab3b-34547fc783ca | 1.28418 | -60.32841 | 2026-01-03 12:53:00 | TERRA_M-T | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 546e6922-6c9c-39d3-8c11-5e4f93f0d995 | -1.80694 | -54.10972 | 2026-01-03 12:55:00 | TERRA_M-T | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| d968475a-63a9-34fa-8a00-eb4bb8aae19c | -2.10714 | -53.50501 | 2026-01-03 12:55:00 | TERRA_M-T | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 45be8b26-71bd-3b2f-a805-eade79bb192a | -1.66955 | -53.92395 | 2026-01-03 12:55:00 | TERRA_M-T | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 9d4dc898-23dd-3034-bc4d-5a57a0c213c8 | -1.27928 | -52.8543 | 2026-01-03 12:55:00 | TERRA_M-T | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 589e350a-6ef2-3eb8-b1cc-75e68dec1457 | -1.05236 | -52.92374 | 2026-01-03 12:55:00 | TERRA_M-T | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 9be53bba-b752-320c-b9ed-1c411144598e | -14.05451 | -56.102 | 2026-01-03 12:57:00 | TERRA_M-T | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6f253818-51ab-349a-b826-b6f6f55e270f | -25.93219 | -53.48692 | 2026-01-03 12:59:00 | TERRA_M-T | AMPÉRE | PARANÁ | Brasil | 4101002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 41.5 |
| d1873a02-a4ef-3d9d-bd48-2420638a163e | -25.93317 | -53.48197 | 2026-01-03 12:59:00 | TERRA_M-T | AMPÉRE | PARANÁ | Brasil | 4101002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 22.3 |
| 6d254946-31b8-3f39-ad70-b014f32977f6 | -25.2845 | -54.23455 | 2026-01-03 12:59:00 | TERRA_M-T | SÃO MIGUEL DO IGUAÇU | PARANÁ | Brasil | 4125704 | 41 | 33 | nan | nan | nan | Mata Atlântica | 25.0 |
| 8162c9fa-5f34-3f4e-8a29-bf1058dade55 | -30.60774 | -52.66457 | 2026-01-03 13:01:00 | TERRA_M-T | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 67.4 |
| de5a0cca-aaa3-38cb-8a7e-11a613275195 | -30.6123 | -52.67045 | 2026-01-03 13:01:00 | TERRA_M-T | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 73.4 |
| c2b10102-abf5-33e1-b1ed-6f807c90e899 | -30.89753 | -55.52979 | 2026-01-03 13:01:00 | TERRA_M-T | SANT'ANA DO LIVRAMENTO | RIO GRANDE DO SUL | Brasil | 4317103 | 43 | 33 | nan | nan | nan | Pampa | 17.8 |


