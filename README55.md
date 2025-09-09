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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 035c7b39-de5e-3c10-b73f-24099bb64751 | -20.45812 | -42.5113 | 2025-09-09 04:36:00 | NOAA-21 | SERICITA | MINAS GERAIS | Brasil | 3166303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| bd9aef47-ae55-320b-a6eb-e98dda9fa423 | -15.67033 | -48.19009 | 2025-09-09 04:36:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aec76504-d69a-3971-8d9b-2049a7ce3d93 | -15.77721 | -53.53833 | 2025-09-09 04:36:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a84bfbd6-d62e-3245-aec1-718658a4d6ef | -14.53264 | -48.7398 | 2025-09-09 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 24c835eb-971f-39d2-b359-0181af3d6aed | -15.71948 | -53.54308 | 2025-09-09 04:36:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| de0a5502-1839-3864-97f5-7bd8ef701f18 | -17.72991 | -44.49311 | 2025-09-09 04:36:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2947e7b0-07e5-3da0-890d-d8137707b7a7 | -15.25355 | -53.80634 | 2025-09-09 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7b72029f-ea7a-3c4f-87ca-e0d3882b35bc | -16.06231 | -50.47917 | 2025-09-09 04:36:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 06386cfa-7668-3dd7-9db3-061c35e925a9 | -12.89718 | -62.08057 | 2025-09-09 04:36:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 957f9bcd-f219-3a57-9739-16adaf107920 | -15.77758 | -56.41121 | 2025-09-09 04:36:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 98f0eabb-0aa9-3bc6-87f7-52a523def39b | -17.57221 | -44.54758 | 2025-09-09 04:36:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2d797be7-a42f-38fb-a102-bc63e88f9ffd | -15.82547 | -48.95217 | 2025-09-09 04:36:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5abb9a37-1ffc-3ae2-a598-7fe76bdb1829 | -15.10423 | -48.06385 | 2025-09-09 04:36:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 012d40c7-04cd-39ae-8f1b-baee3de1020f | -15.77172 | -56.41868 | 2025-09-09 04:36:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| d7e09755-e801-35ad-a54c-fe4a7cac9b57 | -14.77845 | -48.11195 | 2025-09-09 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f2d5ef45-f1a8-3a92-bae7-996860a3ad7e | -14.52875 | -48.7429 | 2025-09-09 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5001abda-6946-3c7a-96fa-e86ea5725a3e | -12.87224 | -62.10231 | 2025-09-09 04:36:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ea26a38f-3eea-3742-a670-0b8357740b4f | -16.78753 | -49.09625 | 2025-09-09 04:36:00 | NOAA-21 | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dd228101-126e-3717-b62b-1c95ad807d84 | -15.21734 | -44.03659 | 2025-09-09 04:36:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fcb05efc-5390-32f6-b457-0c6770de8395 | -18.78379 | -49.64284 | 2025-09-09 04:36:00 | NOAA-21 | CAPINÓPOLIS | MINAS GERAIS | Brasil | 3112604 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2da41690-eff3-3373-95ed-d976d317c95e | -22.59912 | -47.42933 | 2025-09-09 04:38:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f86810bd-70b2-34b8-84ac-1fc27cc960d9 | -23.70946 | -47.33204 | 2025-09-09 04:38:00 | NOAA-21 | IBIÚNA | SÃO PAULO | Brasil | 3519709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 7aad54ca-2f6e-349a-8345-6b8b3900de95 | -22.34839 | -50.89603 | 2025-09-09 04:38:00 | NOAA-21 | JOÃO RAMALHO | SÃO PAULO | Brasil | 3525607 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 14cb075a-8417-33ce-bc88-5eb23745d1ab | -21.8602 | -46.08062 | 2025-09-09 04:38:00 | NOAA-21 | IPUIÚNA | MINAS GERAIS | Brasil | 3131505 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2c25bbed-85a6-3423-a1a0-cc8d910e00b1 | -23.32886 | -50.87943 | 2025-09-09 04:38:00 | NOAA-21 | JATAIZINHO | PARANÁ | Brasil | 4112702 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 01984d57-7857-3b47-80a5-2dfbed7f963d | -22.33784 | -50.89806 | 2025-09-09 04:38:00 | NOAA-21 | RANCHARIA | SÃO PAULO | Brasil | 3542206 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 40b9a665-e83a-3ead-80ce-2d1cee01cfd4 | -22.34782 | -50.89979 | 2025-09-09 04:38:00 | NOAA-21 | JOÃO RAMALHO | SÃO PAULO | Brasil | 3525607 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 960a9e8f-d284-3c42-a640-18483d8d4a8f | -22.35285 | -50.88912 | 2025-09-09 04:38:00 | NOAA-21 | JOÃO RAMALHO | SÃO PAULO | Brasil | 3525607 | 35 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 308615ba-3bda-3b30-b4f4-9ba3d023fa91 | -22.35001 | -50.9079 | 2025-09-09 04:38:00 | NOAA-21 | RANCHARIA | SÃO PAULO | Brasil | 3542206 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fa4c39d3-58b9-376a-9300-f6a76f3de902 | -22.82316 | -46.69778 | 2025-09-09 04:38:00 | NOAA-21 | TUIUTI | SÃO PAULO | Brasil | 3554953 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a04e37b3-46f2-3022-9403-891c181ca529 | -23.14195 | -48.26347 | 2025-09-09 04:38:00 | NOAA-21 | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| a07ec4cd-89b9-32bc-9e55-43be72b560aa | -22.35228 | -50.89287 | 2025-09-09 04:38:00 | NOAA-21 | JOÃO RAMALHO | SÃO PAULO | Brasil | 3525607 | 35 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 420c08ec-75c9-34f0-a4f7-66fbcb1a5219 | -22.76659 | -47.08406 | 2025-09-09 04:38:00 | NOAA-21 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 6642cd18-180b-3895-ad90-bb291e9d5eb1 | -21.00398 | -47.72034 | 2025-09-09 04:38:00 | NOAA-21 | JARDINÓPOLIS | SÃO PAULO | Brasil | 3525102 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b9a8727-cbbc-34aa-a1ee-3dcb8be4e6fa | -22.23037 | -49.72769 | 2025-09-09 04:38:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 20fda9c8-b3c4-3808-abc9-e4933a2f4c05 | -23.32943 | -50.8756 | 2025-09-09 04:38:00 | NOAA-21 | JATAIZINHO | PARANÁ | Brasil | 4112702 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| df501030-c8ad-3a84-a584-5af072f0c5a4 | -22.37518 | -45.96561 | 2025-09-09 04:38:00 | NOAA-21 | POUSO ALEGRE | MINAS GERAIS | Brasil | 3152501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| e04d4458-3a57-3cf1-afd5-f42a7b247f2e | -21.90941 | -46.66261 | 2025-09-09 04:38:00 | NOAA-21 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 522c2240-bd4c-34c5-ab02-de3993bb0572 | -23.5664 | -47.16835 | 2025-09-09 04:38:00 | NOAA-21 | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b957dfcb-0f91-3667-ade0-4dce4f86ab8d | -22.336 | -49.02119 | 2025-09-09 04:38:00 | NOAA-21 | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 16f339cf-16d9-32b7-94b3-57f2c4a283a0 | -21.722 | -46.23304 | 2025-09-09 04:38:00 | NOAA-21 | CAMPESTRE | MINAS GERAIS | Brasil | 3111002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 33e848d4-241f-398f-a40f-e05123a066f5 | -21.16303 | -48.67891 | 2025-09-09 04:38:00 | NOAA-21 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9fed2a97-9c7a-3673-9be7-1ef2bcdd5f2e | -23.71612 | -47.46549 | 2025-09-09 04:38:00 | NOAA-21 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ed609a21-de4f-35ab-98c4-31cbd6c459a4 | -21.72569 | -46.23022 | 2025-09-09 04:38:00 | NOAA-21 | CAMPESTRE | MINAS GERAIS | Brasil | 3111002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 40a04d1e-a38e-3a34-8e77-5ce7e03cfe5b | -20.42473 | -50.83178 | 2025-09-09 04:38:00 | NOAA-21 | MARINÓPOLIS | SÃO PAULO | Brasil | 3529104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| bfcbb8de-bb84-3508-81a6-bfba8b7e394f | -20.9989 | -49.31209 | 2025-09-09 04:38:00 | NOAA-21 | CEDRAL | SÃO PAULO | Brasil | 3511300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3333a3e3-c129-34ad-a051-510aca85145a | -22.59927 | -47.36738 | 2025-09-09 04:38:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 5f287920-7c95-3514-88fb-b0a807ed02ed | -22.09847 | -51.37439 | 2025-09-09 04:38:00 | NOAA-21 | PRESIDENTE PRUDENTE | SÃO PAULO | Brasil | 3541406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 62f47417-2b94-321b-ac34-4adc598d59c6 | -21.43745 | -48.83384 | 2025-09-09 04:38:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 3768c800-cdb8-3d51-bf9d-4b4d0b3bfd03 | -21.23199 | -49.88107 | 2025-09-09 04:38:00 | NOAA-21 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 0ecba77d-01f5-34a1-9afc-447cc830dff3 | -21.00233 | -49.31263 | 2025-09-09 04:38:00 | NOAA-21 | CEDRAL | SÃO PAULO | Brasil | 3511300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d0854046-9ed2-35ac-8a28-da01af321873 | -21.629 | -47.02502 | 2025-09-09 04:38:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 92b2823d-3c68-356d-805d-07dbcd5d58b0 | -21.43394 | -48.83327 | 2025-09-09 04:38:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 32d69002-a82a-38ca-865c-9a60cdf1d4e5 | -21.01847 | -48.41851 | 2025-09-09 04:38:00 | NOAA-21 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 36e14a3c-c21c-3f6c-b64f-e54284606608 | -21.44036 | -48.83863 | 2025-09-09 04:38:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 34bb58d7-688d-3453-9af5-26d97b195a11 | -22.34449 | -50.89921 | 2025-09-09 04:38:00 | NOAA-21 | RANCHARIA | SÃO PAULO | Brasil | 3542206 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 46847ea5-720b-3454-a01a-9fac3296c932 | -23.21102 | -44.93254 | 2025-09-09 04:38:00 | NOAA-21 | UBATUBA | SÃO PAULO | Brasil | 3555406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 8b369e04-141d-30a6-b0ec-2c3a46145e8c | -22.92964 | -49.16158 | 2025-09-09 04:38:00 | NOAA-21 | IARAS | SÃO PAULO | Brasil | 3519253 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f54c311a-8979-336e-942a-8e606d734276 | -21.45029 | -48.84453 | 2025-09-09 04:38:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 11.9 |
| bd46b2a3-4171-37ea-b738-20b27091e931 | -21.57779 | -50.35309 | 2025-09-09 04:38:00 | NOAA-21 | BRAÚNA | SÃO PAULO | Brasil | 3507704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| ca981158-a1d1-3c37-909e-f0c0750c99e3 | -21.19297 | -46.11782 | 2025-09-09 04:38:00 | NOAA-21 | ALTEROSA | MINAS GERAIS | Brasil | 3102001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| b6b8938d-4108-3459-a7f8-f226c6baa6df | -22.15265 | -47.68892 | 2025-09-09 04:38:00 | NOAA-21 | ANALÂNDIA | SÃO PAULO | Brasil | 3502002 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3138dfa8-e526-3da3-bfb3-152ba5c83106 | -22.60516 | -51.96419 | 2025-09-09 04:38:00 | NOAA-21 | ITAGUAJÉ | PARANÁ | Brasil | 4110904 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 40a30837-7869-3369-9b17-a5231e1aa84f | -21.43627 | -48.84224 | 2025-09-09 04:38:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 203440b1-98e6-3ecc-b89a-07e43dd47083 | -21.631 | -45.39513 | 2025-09-09 04:38:00 | NOAA-21 | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 98d573a8-ead9-3a6b-b560-b48173171a41 | -21.23255 | -49.87723 | 2025-09-09 04:38:00 | NOAA-21 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| b939d3d0-f560-3863-81df-d2692aa878c4 | -23.14559 | -48.2642 | 2025-09-09 04:38:00 | NOAA-21 | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 8c0a2199-7535-3915-a885-5f1dfb1ff975 | -21.43977 | -48.84282 | 2025-09-09 04:38:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 7da12314-0027-3951-ac2e-d60c52d5dab0 | -21.23481 | -49.88549 | 2025-09-09 04:38:00 | NOAA-21 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 1c2b73e8-de18-3931-9ba4-1061433b19cb | -23.71771 | -47.46704 | 2025-09-09 04:38:00 | NOAA-21 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| 454cc503-daf9-3e11-8064-d413192ffc6b | -21.44795 | -48.83562 | 2025-09-09 04:38:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 6866b562-d290-3432-95dd-bd968b3625a8 | -21.23819 | -49.88605 | 2025-09-09 04:38:00 | NOAA-21 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 98ed9373-55bd-3049-a7ca-d265b755f452 | -22.34116 | -50.89864 | 2025-09-09 04:38:00 | NOAA-21 | RANCHARIA | SÃO PAULO | Brasil | 3542206 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 759be8d7-c4b9-322b-bc84-98955774ebae | -22.54226 | -47.42348 | 2025-09-09 04:38:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2a185b3e-8037-34f4-a0fd-171a0f31ded6 | -23.71996 | -47.46617 | 2025-09-09 04:38:00 | NOAA-21 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| d643877f-d96c-3fd0-ac1f-088044aa2053 | -22.92614 | -49.16098 | 2025-09-09 04:38:00 | NOAA-21 | IARAS | SÃO PAULO | Brasil | 3519253 | 35 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 7d2e82ec-efb8-3188-8224-0bf889736b57 | -21.69847 | -51.10293 | 2025-09-09 04:38:00 | NOAA-21 | ADAMANTINA | SÃO PAULO | Brasil | 3500105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1d7b5059-0731-3e4c-8fe2-01f5b81b1a1d | -21.32653 | -46.6954 | 2025-09-09 04:38:00 | NOAA-21 | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 9a0034c8-ed4e-37d4-8d2e-d4aa817768a7 | -22.93541 | -47.26689 | 2025-09-09 04:38:00 | NOAA-21 | MONTE MOR | SÃO PAULO | Brasil | 3531803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 6c56541e-9f30-3420-b5b2-94a064905213 | -21.43686 | -48.83804 | 2025-09-09 04:38:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 51943bdf-8608-35e8-ae7f-52ee092ebff5 | -21.23875 | -49.88221 | 2025-09-09 04:38:00 | NOAA-21 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| f8488ddc-2f77-34af-8646-130c6428dbfa | -21.63989 | -47.03192 | 2025-09-09 04:38:00 | NOAA-21 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 886a1533-ce21-347a-b61b-517aa14f19c1 | -21.45438 | -48.84092 | 2025-09-09 04:38:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| df26d09d-440a-3139-a483-f953a2a13aa9 | -21.93031 | -49.96197 | 2025-09-09 04:38:00 | NOAA-21 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| ae7d794e-dac9-39d6-8120-b5d46791f95c | -23.43955 | -47.12856 | 2025-09-09 04:38:00 | NOAA-21 | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 4b21a727-a8ba-3e1e-b14d-f4165ec6cd07 | -22.34725 | -50.90355 | 2025-09-09 04:38:00 | NOAA-21 | RANCHARIA | SÃO PAULO | Brasil | 3542206 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b252e336-850c-3c4b-9f9f-c9859e761024 | -23.60221 | -46.35147 | 2025-09-09 04:38:00 | NOAA-21 | SUZANO | SÃO PAULO | Brasil | 3552502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| b001400a-fc36-36fe-b151-3c2d367ac3dc | -21.23931 | -49.87836 | 2025-09-09 04:38:00 | NOAA-21 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| af563a72-f929-3633-ab89-10a70a69e49a | -22.23094 | -49.72366 | 2025-09-09 04:38:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 957be263-d4e4-3421-96b3-bd5eb0f0b680 | -23.48958 | -45.43745 | 2025-09-09 04:38:00 | NOAA-21 | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 086e7d87-e441-3b9b-975d-3388b136b0de | -21.64373 | -47.03253 | 2025-09-09 04:38:00 | NOAA-21 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 0ffdee23-402f-363e-9155-59bf13271c00 | -21.6322 | -47.0307 | 2025-09-09 04:38:00 | NOAA-21 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a412be91-0b3f-363e-95d2-a03e2c8a2a88 | -22.15638 | -47.68948 | 2025-09-09 04:38:00 | NOAA-21 | ANALÂNDIA | SÃO PAULO | Brasil | 3502002 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 40787830-add8-3a34-9eac-cd124134f9ef | -23.70297 | -47.3522 | 2025-09-09 04:38:00 | NOAA-21 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c0ef949f-d3f5-334d-8f05-e85b61a88905 | -23.43961 | -47.12951 | 2025-09-09 04:38:00 | NOAA-21 | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 7e053945-4d04-3135-9551-c297fdb5d48c | -22.34896 | -50.89228 | 2025-09-09 04:38:00 | NOAA-21 | JOÃO RAMALHO | SÃO PAULO | Brasil | 3525607 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 23283d25-192e-386a-8e48-daec5700ac9c | -21.44737 | -48.83981 | 2025-09-09 04:38:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 723a537a-0fa6-3454-bf3e-8eb536e504ac | -22.23078 | -49.72432 | 2025-09-09 04:38:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 8dd77e49-43b6-3fa7-adcc-f8c1be595fb9 | -22.33139 | -48.81756 | 2025-09-09 04:38:00 | NOAA-21 | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 1903f5f6-4bac-3e49-a7fb-0a2a389b3be3 | -23.20749 | -50.8274 | 2025-09-09 04:38:00 | NOAA-21 | URAÍ | PARANÁ | Brasil | 4128401 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |


[Clique aqui para ver as próximas entradas](README56.md)
