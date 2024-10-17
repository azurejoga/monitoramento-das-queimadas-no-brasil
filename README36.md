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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 21ff439f-5b5c-38d3-b1fe-12d2d8398541 | 1.94454 | -60.86546 | 2024-10-17 05:01:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d89258d8-a6b8-3f98-8d01-2d1ed4ff72e0 | 1.94383 | -60.86074 | 2024-10-17 05:01:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2cb0e1bb-c2d0-392e-8f68-512be21c8802 | -3.93157 | -42.36919 | 2024-10-17 05:04:00 | NOAA-21 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 780ba663-4e94-3484-8d18-183adecf9c92 | -3.92822 | -42.3934 | 2024-10-17 05:04:00 | NOAA-21 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 9739d8bf-eed7-3633-a26c-aaa87f65c15c | -3.9257 | -42.41154 | 2024-10-17 05:04:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 30.4 |
| 74d82ef2-da3a-3561-ba06-22a2c302b576 | -3.92486 | -42.41759 | 2024-10-17 05:04:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 15.9 |
| ae9d3e8a-1082-396e-805e-c95e609730f8 | -3.92398 | -42.37424 | 2024-10-17 05:04:00 | NOAA-21 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c2e45303-15b1-32c0-86ae-f1a2005368b7 | -3.92341 | -42.40677 | 2024-10-17 05:04:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 17.4 |
| fc059e04-f53d-3d36-9be1-a97fc370063e | -3.92314 | -42.38034 | 2024-10-17 05:04:00 | NOAA-21 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 4e7c533a-466e-319b-9be4-421368d0b666 | -3.92254 | -42.41278 | 2024-10-17 05:04:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 31.4 |
| e7391c55-d918-3d8d-866b-bf2179cc6368 | -3.92166 | -42.41881 | 2024-10-17 05:04:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 31.4 |
| f9a0c672-b976-33d4-9c0c-4f48a2d8ead2 | -3.92064 | -42.39843 | 2024-10-17 05:04:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| f2303461-edd2-3fed-8e9b-4453be6a909c | -3.91981 | -42.40445 | 2024-10-17 05:04:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 30.4 |
| 5c8ba13a-d73e-35f6-8002-2e6e17f5b963 | -3.91897 | -42.41047 | 2024-10-17 05:04:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 30.4 |
| 6af2d845-ccbb-3e54-9525-288d99f2110f | -3.91814 | -42.41652 | 2024-10-17 05:04:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 9cf6046b-e950-3822-a296-637890913802 | -3.91755 | -42.3997 | 2024-10-17 05:04:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 32.9 |
| 08709f07-7629-3ee9-9042-424bb5cf225d | -3.9173 | -42.42259 | 2024-10-17 05:04:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 9aceb11c-8045-3b47-ac85-eea5a949cfb1 | -3.91724 | -42.37312 | 2024-10-17 05:04:00 | NOAA-21 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 2eb95558-336c-3207-bc5e-e3b49f4d1810 | -3.91668 | -42.4057 | 2024-10-17 05:04:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 32.9 |
| 3ae22352-dd74-3677-9065-c3496edc9b60 | -3.91641 | -42.37919 | 2024-10-17 05:04:00 | NOAA-21 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| ab777350-1415-3740-8dd4-98f432c29d56 | -3.91581 | -42.41172 | 2024-10-17 05:04:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 15.7 |
| 8f825ae7-77ae-33c1-a5e1-ef9ce2601a90 | -3.91493 | -42.41778 | 2024-10-17 05:04:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 15.7 |
| 53c55c3c-61b9-30ad-b020-d4550161cacc | -3.91308 | -42.40332 | 2024-10-17 05:04:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 12.8 |
| b59aee44-d906-3109-a0a0-a9db63c330f4 | -3.91225 | -42.40937 | 2024-10-17 05:04:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 12.8 |
| d35db042-d2eb-3490-9f4e-2b2ea5b9d867 | -3.91141 | -42.41545 | 2024-10-17 05:04:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| c174dbf6-5edb-324c-81cb-27ab313b5540 | -3.91134 | -42.3659 | 2024-10-17 05:04:00 | NOAA-21 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 3af2a937-d9d5-325c-bc25-35a378388c33 | -5.96896 | -43.36727 | 2024-10-17 05:04:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 0fa60ac5-8e09-3794-9ee8-e01d0bffcd3f | -5.6584 | -43.00998 | 2024-10-17 05:04:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b9cc43e6-14a5-3fbf-9243-4895c255ecf5 | -5.96245 | -43.36619 | 2024-10-17 05:04:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 7.0 |
| d5e50363-e644-3759-be70-ff52eb7901ed | -5.6547 | -43.00744 | 2024-10-17 05:04:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| acb80d72-b97f-30ab-973f-4dceebf585e7 | -5.65391 | -43.01312 | 2024-10-17 05:04:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 16e402ef-984f-3ac3-92da-7af37587a3fd | -5.21735 | -43.18834 | 2024-10-17 05:04:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7ed024df-7cea-33a4-9b14-6d54e6d15c8a | -5.96165 | -43.37213 | 2024-10-17 05:04:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 4dff62c9-0e78-3543-a5bc-18a7ef621919 | -5.96088 | -43.3779 | 2024-10-17 05:04:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 93583a3a-3c72-382a-be9c-bdbe5fa2399d | -5.65174 | -43.00916 | 2024-10-17 05:04:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 079cb3e0-9cb0-30ee-bc6f-8a5d011c115a | -5.95289 | -43.38786 | 2024-10-17 05:04:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9b978127-220c-3550-b372-67484fd10306 | -5.94638 | -43.38679 | 2024-10-17 05:04:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 4814a5a3-9d39-32ad-9fc0-38a32463b5c4 | -6.72485 | -43.56124 | 2024-10-17 05:04:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b0d1d78c-35ad-303d-bab8-8f87dc3ded43 | -6.7248 | -43.56038 | 2024-10-17 05:04:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0736233c-144e-3f46-870d-973d985c271f | -6.71832 | -43.56037 | 2024-10-17 05:04:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 13627207-2525-3a6a-8560-ddae08d3b039 | -6.71827 | -43.55949 | 2024-10-17 05:04:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ecc57d0d-76c7-3dce-9839-741c383bd14a | -6.71758 | -43.56491 | 2024-10-17 05:04:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f610ca79-4df0-338a-bf5f-a6f019f4e788 | -5.02697 | -43.66591 | 2024-10-17 05:04:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| aeaa15ea-3ac1-3777-93e5-d0d540fcd679 | -5.02062 | -43.665 | 2024-10-17 05:04:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b3d0a8ed-d113-3eda-adce-9a881a4ea3c9 | -5.02469 | -43.66055 | 2024-10-17 05:04:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 43581005-38bc-3dc6-b376-a44c5c9c5bc7 | -5.02395 | -43.66574 | 2024-10-17 05:04:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9aa79d06-92fd-3e76-b9e6-029c583d62c3 | -5.02133 | -43.65979 | 2024-10-17 05:04:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 8eb1a74d-37ec-31f6-9fd3-44f000806042 | -4.13032 | -43.08709 | 2024-10-17 05:04:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e4023536-d158-3cad-8abe-98eafc3cce26 | -4.12958 | -43.09249 | 2024-10-17 05:04:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2479864d-d4fa-3052-9133-517de063127f | -3.64162 | -44.28804 | 2024-10-17 05:04:00 | NOAA-21 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 44c47bb4-94d9-39ab-8ed0-ace6609b60fb | -5.50581 | -43.69884 | 2024-10-17 05:04:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a7786cda-d834-374d-bb45-caeb00c2c584 | -5.54446 | -43.90945 | 2024-10-17 05:04:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3bc350ab-5c7b-3a1a-aae7-86d9639f05c8 | -5.54064 | -43.91111 | 2024-10-17 05:04:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c5d43985-ec40-3dd1-a085-a66954917ede | -5.50651 | -43.69375 | 2024-10-17 05:04:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6d26df98-c225-34c6-9794-579614951671 | -5.28146 | -44.09374 | 2024-10-17 05:04:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7a0ec987-26a9-3b6c-adf2-2ea2bed0b5ef | -5.54689 | -43.91225 | 2024-10-17 05:04:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c35dc348-652d-3867-911a-979ed61eb357 | -5.54377 | -43.91457 | 2024-10-17 05:04:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b92280af-84b4-3298-9052-b1037b280a23 | -5.57966 | -44.87918 | 2024-10-17 05:04:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dbd386e8-3fcc-31b6-a3cc-c7402cfa508f | -5.57907 | -44.88337 | 2024-10-17 05:04:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4e5178fd-bf63-3b8b-9c2f-d855e80ccd08 | -5.57848 | -44.88753 | 2024-10-17 05:04:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4ff2c5e0-f147-38c4-bbbc-3d6942253941 | -5.57375 | -44.87826 | 2024-10-17 05:04:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 29fb0f50-7b74-34da-8e2a-1c154116dd3d | -5.57316 | -44.88249 | 2024-10-17 05:04:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9a3e27ad-454f-301f-acf9-95dfe7733541 | -5.57256 | -44.88671 | 2024-10-17 05:04:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c227e129-a4f6-375f-a144-88e910d350b8 | -5.27529 | -44.09271 | 2024-10-17 05:04:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 36d7cf82-647c-3809-8c76-09c92f82e91e | -7.87289 | -45.35516 | 2024-10-17 05:04:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 78459751-c3e8-334b-ba80-a44246c1a7f9 | -7.87231 | -45.35949 | 2024-10-17 05:04:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 27145541-cf37-33dc-a1c2-001363a612b2 | -7.87151 | -45.34948 | 2024-10-17 05:04:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 85d98871-0067-3797-9e97-d9b3097dad91 | -7.87096 | -45.35384 | 2024-10-17 05:04:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0da70adb-8d08-3ad5-b265-e7c3d2e59c8d | -7.87041 | -45.35818 | 2024-10-17 05:04:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 98dfe053-14ab-313a-b76b-e4c9b7ba828a | -7.86754 | -45.35001 | 2024-10-17 05:04:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| cefa4aab-7bd7-3c9c-b4c2-c774f1da2510 | -7.86696 | -45.35435 | 2024-10-17 05:04:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 5db7dbb8-bfbc-3070-9e39-3baa0cc81893 | -7.86639 | -45.35868 | 2024-10-17 05:04:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1494746c-3ee5-329c-b9d1-c3c10db804fe | -7.86582 | -45.36296 | 2024-10-17 05:04:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f3821228-446f-3e30-b449-53422f0a1d1c | -7.86525 | -45.36717 | 2024-10-17 05:04:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 816275f7-c8c7-3798-bf80-cff0ed1390e5 | -7.86105 | -45.35353 | 2024-10-17 05:04:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 0259840f-7cd1-3f25-9d19-99fc6ed48c52 | -7.86047 | -45.35785 | 2024-10-17 05:04:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2549adc5-c9cf-37b9-a350-0534aba5237a | -7.8599 | -45.36215 | 2024-10-17 05:04:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2726a9ca-52c9-3510-bafd-8d846134761e | -3.60374 | -44.78982 | 2024-10-17 05:04:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 391c6fbf-2209-312c-86bf-0a02efefb368 | -3.12389 | -45.229 | 2024-10-17 05:04:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e621ef0b-4980-34b8-b1f4-b7407fe504dc | -3.12336 | -45.23268 | 2024-10-17 05:04:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 41447ba3-ca6f-33be-940e-087af6ff2a8d | -2.32322 | -45.07512 | 2024-10-17 05:04:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8c6dd368-9e76-3a25-a792-7ca09b9faa86 | -2.31821 | -45.07054 | 2024-10-17 05:04:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c0b27bf1-6818-3c2d-bd6a-cb1a72040e04 | -2.31765 | -45.07427 | 2024-10-17 05:04:00 | NOAA-21 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a1ee638c-7513-3991-996c-449fe4962300 | -4.77616 | -45.97247 | 2024-10-17 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bb57e053-acb4-345b-930d-a7e3317fbf71 | -4.77562 | -45.97621 | 2024-10-17 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c0d798a9-792a-3fbc-b194-03b6043745d8 | -3.7062 | -45.91445 | 2024-10-17 05:04:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2cdbc2d-b5cf-318b-81fd-11d19753dea9 | -3.70179 | -45.90707 | 2024-10-17 05:04:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| beebc4af-2f03-36c1-ba35-2e47fc4da3e6 | -3.7013 | -45.91041 | 2024-10-17 05:04:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| cbeff8c1-3f97-391b-97a7-c1dc394dbcea | -3.70081 | -45.91368 | 2024-10-17 05:04:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 12.7 |
| e3ecb821-e8fa-336a-9d19-d7bff9034580 | -3.70033 | -45.91698 | 2024-10-17 05:04:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 463dfe2a-49d0-36c4-9953-382bf2b4b77c | -3.69984 | -45.92029 | 2024-10-17 05:04:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 15.0 |
| c11a42b4-21b5-38e8-9c01-a353b072f484 | -3.69592 | -45.90961 | 2024-10-17 05:04:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| fcf501a9-1998-3df0-b721-a486d24c1ce6 | -3.69542 | -45.91298 | 2024-10-17 05:04:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 12.7 |
| a219d0f7-8694-3b0d-9fdf-8d21d69a9dda | -3.69495 | -45.91623 | 2024-10-17 05:04:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 12.7 |
| dc075280-1981-360f-8c6c-883f45c3d95b | -4.73641 | -45.70016 | 2024-10-17 05:04:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f42c06c8-8ed5-3f6d-ae99-7a4bb43b740e | -4.73598 | -45.70187 | 2024-10-17 05:04:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1654c854-4050-3bb7-8537-5ebd5c54a5e7 | -4.7359 | -45.70367 | 2024-10-17 05:04:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 45e3f8a2-4639-35b0-b307-0909ac72564e | -4.7309 | -45.69917 | 2024-10-17 05:04:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 65689da1-4296-371e-9b75-fb2fe2266f5f | -4.73048 | -45.70075 | 2024-10-17 05:04:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b8a8c1c5-685a-3821-9568-5388bed99e68 | -4.40557 | -45.80713 | 2024-10-17 05:04:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README37.md)
