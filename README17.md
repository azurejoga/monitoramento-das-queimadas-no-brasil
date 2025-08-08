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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 971a44ec-c751-3f14-a85b-8f1ab982299d | -20.57105 | -41.72354 | 2025-08-08 04:36:00 | NOAA-21 | DIVINO DE SÃO LOURENÇO | ESPÍRITO SANTO | Brasil | 3201803 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 69a50210-2afb-36bc-a41c-0f4a3de47b12 | -18.22517 | -45.62866 | 2025-08-08 04:36:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ba6c1e8b-66dd-3b00-8265-49afd5b57e2d | -13.04103 | -56.86852 | 2025-08-08 04:36:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 15.9 |
| a6d3f21a-70c9-328e-a35b-44d343e9ced2 | -18.47349 | -41.40529 | 2025-08-08 04:36:00 | NOAA-21 | SÃO JOSÉ DO DIVINO | MINAS GERAIS | Brasil | 3163300 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 933a996d-579b-3c09-adb7-89845086a8ec | -13.05214 | -56.86038 | 2025-08-08 04:36:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d58fa7da-72fd-3ee4-896f-acbd315993cf | -14.78397 | -47.99429 | 2025-08-08 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6200c41e-e40d-30f5-ae0d-c6bba2ff8adf | -13.04842 | -56.85469 | 2025-08-08 04:36:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 707b5d3c-d4d9-3652-877b-e37e416e4160 | -17.7602 | -47.25647 | 2025-08-08 04:36:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 96b0068e-5b25-3358-9d65-e636ee297fb9 | -18.61697 | -44.26657 | 2025-08-08 04:36:00 | NOAA-21 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b1ad433a-88b5-393c-93eb-362116abf16e | -18.78261 | -47.46757 | 2025-08-08 04:36:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f2e62de7-1eae-30ab-9c75-6c4cf62e34d0 | -13.03731 | -56.86287 | 2025-08-08 04:36:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5c1e9cdf-8c68-398a-85f5-7afecb4202a2 | -17.40256 | -46.55136 | 2025-08-08 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 709176e0-7432-3358-be91-782999d599b7 | -17.6131 | -46.71389 | 2025-08-08 04:36:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 41855f05-b5c7-3ae7-8773-4432d97527cc | -19.23102 | -46.58357 | 2025-08-08 04:36:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fa2d9f17-3d2f-345d-9c54-e054498a29e6 | -20.4911 | -42.52971 | 2025-08-08 04:36:00 | NOAA-21 | JEQUERI | MINAS GERAIS | Brasil | 3135506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5dde4874-39d7-35c4-ab6c-98341e64f6eb | -13.0475 | -56.8596 | 2025-08-08 04:36:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 30b784e5-b671-3038-b082-89173e7b4360 | -20.12369 | -43.80459 | 2025-08-08 04:36:00 | NOAA-21 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 97e35076-6be9-3fbd-86e3-a250dcb56b91 | -17.61684 | -46.71447 | 2025-08-08 04:36:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 190f8597-3b2f-39e0-b45f-be7c5b835155 | -14.35697 | -51.10056 | 2025-08-08 04:36:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a22d237e-bb45-3145-b169-3bdae68a9a50 | -19.22655 | -46.58775 | 2025-08-08 04:36:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b75394de-5bf8-3492-ad47-672e62ab63a5 | -15.84076 | -41.85019 | 2025-08-08 04:36:00 | NOAA-21 | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6d97ed03-d90c-3efc-8d66-65b41b5add27 | -14.78227 | -48.00579 | 2025-08-08 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a3b60508-49a1-3579-a7ae-fb285a88af4c | -18.22116 | -45.62802 | 2025-08-08 04:36:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0a1f7313-3d35-349e-b696-36be6ba636e2 | -19.18778 | -45.05303 | 2025-08-08 04:36:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 45892a77-e6e3-3ec9-8ddb-b9557e3c9c80 | -18.38686 | -52.11249 | 2025-08-08 04:36:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5acef56c-3965-33ea-82cd-cc46b2c190fe | -18.95314 | -50.02709 | 2025-08-08 04:36:00 | NOAA-21 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5bdcd3cf-15cb-3b5b-8682-33ae34e91061 | -17.22865 | -39.28321 | 2025-08-08 04:36:00 | NOAA-21 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c7f0db17-ea1c-3020-a7c9-2f81f5cf5f70 | -18.47218 | -41.40702 | 2025-08-08 04:36:00 | NOAA-21 | SÃO JOSÉ DO DIVINO | MINAS GERAIS | Brasil | 3163300 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| e494067b-9230-36d2-aaad-0c3b247a791d | -18.91981 | -47.55728 | 2025-08-08 04:36:00 | NOAA-21 | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1f0fe092-b425-3698-aa06-b6e40ea9a797 | -15.5503 | -43.26845 | 2025-08-08 04:36:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cab63cbf-cfc6-3284-8a61-8215363ab281 | -18.85927 | -45.13385 | 2025-08-08 04:36:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fd6772b3-a00f-34a3-9dd4-64f46ff766e8 | -17.75927 | -47.25869 | 2025-08-08 04:36:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7e78aa50-38b3-3a12-b41b-23cd42a56721 | -17.6892 | -48.63678 | 2025-08-08 04:36:00 | NOAA-21 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 69904eca-d375-30d2-bc7e-5c12886587b2 | -19.71941 | -50.20935 | 2025-08-08 04:36:00 | NOAA-21 | ITURAMA | MINAS GERAIS | Brasil | 3134400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4e69c0b5-38e0-3a22-8069-ea093d10dadc | -13.0586 | -56.85143 | 2025-08-08 04:36:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b3afe9bd-b11c-3869-bc2e-6055e5d0c95f | -15.348 | -46.08082 | 2025-08-08 04:36:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9e9986ab-876f-3e02-89d0-027cb261260e | -16.7404 | -49.36725 | 2025-08-08 04:36:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 38badc1a-8adb-3fc5-a87e-564028113219 | -14.36644 | -51.10588 | 2025-08-08 04:36:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e9de500d-63aa-3be9-a0f4-0110dee7b9e9 | -17.57805 | -49.0817 | 2025-08-08 04:36:00 | NOAA-21 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 56b164cc-708b-3d6a-bf0c-05e8223982b4 | -19.22717 | -46.58305 | 2025-08-08 04:36:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cd02ef39-e363-3778-a0cb-dfca6d9fa4cc | -13.04659 | -56.86446 | 2025-08-08 04:36:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2e8a46f1-a44b-3711-b91d-098132504dd9 | -20.06416 | -47.5856 | 2025-08-08 04:36:00 | NOAA-21 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 12.1 |
| d17439d6-8b7c-38fa-a098-e95374f70999 | -15.55524 | -50.13658 | 2025-08-08 04:36:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4a46aca2-97b5-31fb-9128-07c138ace950 | -19.23039 | -46.58826 | 2025-08-08 04:36:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 86c07556-6fc9-3bcf-b569-33adbbe79a93 | -15.65735 | -48.24376 | 2025-08-08 04:36:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 13db541b-0ddf-3b98-893f-29f0e02c0d17 | -16.3418 | -43.51737 | 2025-08-08 04:36:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b5625c1e-d2c8-33a2-9726-40571917a5c8 | -15.34863 | -46.07613 | 2025-08-08 04:36:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2f65d88f-4056-341f-a77f-18e9c3962e07 | -19.95035 | -45.17975 | 2025-08-08 04:36:00 | NOAA-21 | ARAÚJOS | MINAS GERAIS | Brasil | 3103900 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 114a3ca1-9a6b-35bb-9f5d-819a9b38bd22 | -19.77243 | -46.56975 | 2025-08-08 04:36:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c77fdab6-3027-3375-aa60-d6567d871c1d | -16.72591 | -49.13064 | 2025-08-08 04:36:00 | NOAA-21 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 9d2f60c1-d0ab-335c-ab11-7d56bbae6b35 | -14.81402 | -48.40646 | 2025-08-08 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e9c46e27-ca96-33d8-a029-8513cc63450f | -13.03823 | -56.85799 | 2025-08-08 04:36:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f0f0da6d-78ae-3948-b5b5-f93871dff261 | -23.8444 | -50.19519 | 2025-08-08 04:38:00 | NOAA-21 | IBAITI | PARANÁ | Brasil | 4109708 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 859467a3-2582-3ea4-8520-21d1c5b381e8 | -22.18041 | -47.12971 | 2025-08-08 04:38:00 | NOAA-21 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 70e0f5b1-cfba-348a-b011-cf681fdd94fe | -22.24652 | -48.54179 | 2025-08-08 04:38:00 | NOAA-21 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| e006b66d-ebb6-3397-b3e7-b4f0ba936bed | -23.3679 | -47.34228 | 2025-08-08 04:38:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| d16ae39e-ce5c-36ad-a713-3bdbeaa8fde2 | -23.34289 | -52.31639 | 2025-08-08 04:38:00 | NOAA-21 | FLORAÍ | PARANÁ | Brasil | 4107801 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 002d4ef4-2261-3a51-a216-094e3a0a30d3 | -21.39198 | -48.67633 | 2025-08-08 04:38:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cf97a22a-0b75-3690-8c82-4f7e1ff5557e | -22.22172 | -44.72941 | 2025-08-08 04:38:00 | NOAA-21 | ALAGOA | MINAS GERAIS | Brasil | 3101300 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 67e35bba-0aa4-359a-8990-74079cd806fc | -24.54869 | -49.05174 | 2025-08-08 04:38:00 | NOAA-21 | BARRA DO CHAPÉU | SÃO PAULO | Brasil | 3505351 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 89637c21-ef21-33a0-b801-cc9ebb149123 | -22.17721 | -47.124 | 2025-08-08 04:38:00 | NOAA-21 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f916092b-6def-3387-bfd0-eb51daf3d111 | -21.21356 | -44.99205 | 2025-08-08 04:38:00 | NOAA-21 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 06f2d008-87dd-30c5-b863-d138c19db1e7 | -23.36853 | -47.33708 | 2025-08-08 04:38:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 0c0560f0-7d43-3f72-b32d-6d40be66a354 | -23.39831 | -46.77308 | 2025-08-08 04:38:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 81dcbed1-1cc1-3775-8ccd-67939e373e4b | -23.2637 | -51.15966 | 2025-08-08 04:38:00 | NOAA-21 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| ce98086f-37ce-3bac-9a9d-c60a250367a1 | -22.18108 | -47.12458 | 2025-08-08 04:38:00 | NOAA-21 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 080e4b1e-4978-3cae-b7c9-44d22c262b58 | -24.49003 | -49.01248 | 2025-08-08 04:38:00 | NOAA-21 | BARRA DO CHAPÉU | SÃO PAULO | Brasil | 3505351 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f7c5b099-0e11-387b-85cb-2aa0f2f68f1c | -21.78642 | -43.33492 | 2025-08-08 04:38:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 24a3e8ba-a676-3a86-9ece-a4bc8c552328 | -21.11548 | -48.6415 | 2025-08-08 04:38:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 53f597d0-0212-3b6d-90c5-26023e44198d | -23.56898 | -47.00344 | 2025-08-08 04:38:00 | NOAA-21 | ITAPEVI | SÃO PAULO | Brasil | 3522505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 77a6f694-5386-389a-a2a5-28aad3dab53f | -23.36679 | -47.34113 | 2025-08-08 04:38:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 84ae1b4d-42e8-31fe-a4b8-8992b3161975 | -22.89015 | -50.70929 | 2025-08-08 04:38:00 | NOAA-21 | FLORÍNEA | SÃO PAULO | Brasil | 3516101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ebffda52-111d-364c-80d9-95ad701862df | -23.40486 | -45.11513 | 2025-08-08 04:38:00 | NOAA-21 | UBATUBA | SÃO PAULO | Brasil | 3555406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 290c1941-e96e-36b3-89c2-8918df71877c | -24.5451 | -49.05117 | 2025-08-08 04:38:00 | NOAA-21 | BARRA DO CHAPÉU | SÃO PAULO | Brasil | 3505351 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 63fa9d60-b282-3ba8-afd7-ee2971516333 | -21.38844 | -48.67575 | 2025-08-08 04:38:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 32ef5945-517b-3dce-93be-a98f859d9288 | -22.34572 | -49.08349 | 2025-08-08 04:38:00 | NOAA-21 | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f7f37ccb-eb45-3595-80a2-4973eba82390 | -23.43065 | -47.57942 | 2025-08-08 04:38:00 | NOAA-21 | IPERÓ | SÃO PAULO | Brasil | 3521002 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a7cad4fe-d9b0-3e5b-bcb7-9468e763a9aa | -24.0782 | -48.54935 | 2025-08-08 04:38:00 | NOAA-21 | CAPÃO BONITO | SÃO PAULO | Brasil | 3510203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 08ec681c-2e9c-3c6e-9389-635388907fac | -20.062 | -47.5663 | 2025-08-08 04:40:00 | GOES-19 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 50.3 |
| cd2a0594-5245-3e71-9f5b-4c874e3c177a | -7.043 | -59.1787 | 2025-08-08 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 262bc75f-dde6-37ef-b20a-009b962c546b | -17.5765 | -49.0874 | 2025-08-08 04:40:00 | GOES-19 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 40.5 |
| e01a9842-b91d-356b-8d12-779e25f9ff9f | -20.0613 | -47.5897 | 2025-08-08 04:40:00 | GOES-19 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 25af7ebf-b4c3-3250-b5a9-a2ded2a1f70a | -20.0613 | -47.5897 | 2025-08-08 04:50:00 | GOES-19 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 85.7 |
| d0f4427a-5a51-332a-8663-629a7cc43146 | -20.0409 | -47.5944 | 2025-08-08 04:50:00 | GOES-19 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 54.5 |
| af7c46b1-ee39-3879-8d46-0542030af9b9 | -3.96847 | -47.8806 | 2025-08-08 04:57:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1fcc1f9d-4a85-33a9-8884-e4f969a1ff76 | -6.12291 | -42.95863 | 2025-08-08 04:57:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| f9a0e1a2-e65e-352e-982a-09d560ab1e28 | -6.12352 | -42.95417 | 2025-08-08 04:57:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| bda092db-515d-3b69-9c82-dd961037b3bd | -3.96796 | -47.87926 | 2025-08-08 04:57:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9dd17d0f-a81a-30d9-8e85-75aa78efa13e | -3.36059 | -43.17093 | 2025-08-08 04:57:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 31e8532a-213b-3acb-9419-5ce1b48d6aa3 | -3.25268 | -43.26447 | 2025-08-08 04:57:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68d4cd33-fca5-3375-8348-526c8689ee2c | -3.66438 | -41.75852 | 2025-08-08 04:57:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5c999cf2-f614-3ba2-b458-94c69e5ab8b9 | -3.25041 | -43.27004 | 2025-08-08 04:57:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bcebc979-4c3f-3f21-8ddc-81d494aecd38 | -3.99904 | -47.09155 | 2025-08-08 04:57:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 549d13e8-0246-32f5-b22f-ff52a536f9fb | -4.00351 | -47.09217 | 2025-08-08 04:57:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 54fb9eb0-fdc2-31a7-80f0-6eaf456f3b07 | -3.251 | -43.26613 | 2025-08-08 04:57:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9d135c7c-9740-3243-9658-3cd73faba0ec | -3.25212 | -43.26839 | 2025-08-08 04:57:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4c35e775-9bd6-3040-99c5-720ef37949e7 | -3.35542 | -43.16602 | 2025-08-08 04:57:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 68f44b01-a4e5-304b-967e-d2730c35d55e | -5.42285 | -47.1515 | 2025-08-08 04:57:00 | NPP-375D | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bcd6e916-a339-3fe3-82b3-97a5a8b77343 | -3.35481 | -43.17006 | 2025-08-08 04:57:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7406126a-8c2d-3bf4-9d1c-67a42942ec13 | -4.9197 | -46.73172 | 2025-08-08 04:57:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README18.md)
