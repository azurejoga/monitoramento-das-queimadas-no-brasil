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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8b2becf5-21d3-3746-88a3-a0c1f2a5eb9f | -22.69809 | -48.69558 | 2025-09-12 04:29:00 | NOAA-20 | LENÇÓIS PAULISTA | SÃO PAULO | Brasil | 3526803 | 35 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 246562d3-64db-3c83-b725-c6bdc2c972e5 | -20.00633 | -47.653 | 2025-09-12 04:29:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 08bec67c-0e9d-399c-8cd4-e24e1a74ee4b | -19.97633 | -47.59608 | 2025-09-12 04:29:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0609c2c2-b756-3880-a0d6-ddac0f426471 | -23.72968 | -47.21967 | 2025-09-12 04:29:00 | NOAA-20 | IBIÚNA | SÃO PAULO | Brasil | 3519709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b798b44e-aefa-3d6a-8d09-a7245046f4fc | -22.18552 | -49.72979 | 2025-09-12 04:29:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 74efa852-629b-319b-9da0-1d18af0533b5 | -23.37856 | -47.23143 | 2025-09-12 04:29:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 41b8cacd-5fe5-32a1-ae6c-5c47362daeae | -23.14359 | -48.25219 | 2025-09-12 04:29:00 | NOAA-20 | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 4fd9b720-56c7-32a2-8fa4-1c85b906bdd4 | -22.78108 | -47.12778 | 2025-09-12 04:29:00 | NOAA-20 | PAULÍNIA | SÃO PAULO | Brasil | 3536505 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2872a00a-b997-36f8-b0f4-44abe628912b | -20.35681 | -49.95534 | 2025-09-12 04:29:00 | NOAA-20 | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4bb23520-598e-313e-a338-571084fd71aa | -22.18768 | -49.73783 | 2025-09-12 04:29:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 290.9 |
| e420a8a4-75bc-3fa7-9496-19c96e0d6982 | -20.23273 | -49.25791 | 2025-09-12 04:29:00 | NOAA-20 | FRONTEIRA | MINAS GERAIS | Brasil | 3127008 | 31 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 26ec55c4-cace-3219-a9bb-7cb8558932ff | -23.34709 | -47.19492 | 2025-09-12 04:29:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 8d1974f2-3f3e-3722-a273-0010f06222d6 | -20.35349 | -49.95474 | 2025-09-12 04:29:00 | NOAA-20 | ÁLVARES FLORENCE | SÃO PAULO | Brasil | 3501202 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fcf4c8bc-75f3-3477-8056-ab0d21d3c802 | -21.76843 | -47.27883 | 2025-09-12 04:29:00 | NOAA-20 | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 37938b99-f01b-3a39-b5a4-73c2b9cb0c41 | -21.96975 | -47.55816 | 2025-09-12 04:29:00 | NOAA-20 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e4991a81-e054-32d1-baa2-3500776df702 | -23.37796 | -47.23576 | 2025-09-12 04:29:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 83dcb75b-db28-3867-a0ef-48bcfe795cbf | -21.94776 | -47.56287 | 2025-09-12 04:29:00 | NOAA-20 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e4918c70-a902-32e7-872a-aa82d4dcbf9d | -24.80238 | -50.22752 | 2025-09-12 04:29:00 | NOAA-20 | CARAMBEÍ | PARANÁ | Brasil | 4104659 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 32f53a94-010d-37cb-81ed-73deec361b3e | -22.79648 | -47.80499 | 2025-09-12 04:29:00 | NOAA-20 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 08c187ae-8a4e-3000-ad86-cc16834fb402 | -21.44866 | -56.15685 | 2025-09-12 04:29:00 | NOAA-20 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 71e6a000-f8af-387c-836d-36bae3fd4b94 | -21.9181 | -47.91298 | 2025-09-12 04:29:00 | NOAA-20 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 496f311a-9d1d-3f6d-923e-677f7d52c771 | -24.16394 | -51.04157 | 2025-09-12 04:29:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| bd4eaccf-f0bf-3c22-9f82-83e05720619d | -23.15093 | -47.47013 | 2025-09-12 04:29:00 | NOAA-20 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| c0a7a557-8770-35e0-b603-f89fb668e536 | -20.01427 | -47.6465 | 2025-09-12 04:29:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 406f08af-039c-352c-975f-dafb6ec048b0 | -20.23605 | -49.25849 | 2025-09-12 04:29:00 | NOAA-20 | FRONTEIRA | MINAS GERAIS | Brasil | 3127008 | 31 | 33 | nan | nan | nan | Cerrado | 24.4 |
| d601cba5-62bd-3081-8f62-d1dd4c141de5 | -21.18513 | -47.52444 | 2025-09-12 04:29:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c5b3452e-b5d2-3475-9a90-c497dda02b08 | -23.31219 | -47.34442 | 2025-09-12 04:29:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 14d6f0bc-84c0-3d1d-9737-545eb70ff681 | -23.14309 | -49.65805 | 2025-09-12 04:29:00 | NOAA-20 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 2896bbf6-f38f-3fbe-ad85-aa0ad5f032fb | -20.35058 | -48.39899 | 2025-09-12 04:29:00 | NOAA-20 | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 54b2952e-dc9e-32e0-b496-3f2ab563d11d | -19.9933 | -47.64673 | 2025-09-12 04:29:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1e650327-c790-3ef8-acec-f0339319ab6e | -22.7959 | -47.809 | 2025-09-12 04:29:00 | NOAA-20 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 18712234-bc44-3a71-b802-9b7c834b6a08 | -22.70119 | -46.22065 | 2025-09-12 04:29:00 | NOAA-20 | ITAPEVA | MINAS GERAIS | Brasil | 3133600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6787e025-cec9-314f-acf7-2fdd3198b81b | -23.13265 | -47.49773 | 2025-09-12 04:29:00 | NOAA-20 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8afd926a-6f6d-3f08-aa6b-de0560171bd7 | -22.5184 | -44.71294 | 2025-09-12 04:29:00 | NOAA-20 | QUELUZ | SÃO PAULO | Brasil | 3541901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| be27d1e2-09ee-3245-b4ba-82ea71494533 | -20.66566 | -44.25776 | 2025-09-12 04:29:00 | NOAA-20 | DESTERRO DE ENTRE RIOS | MINAS GERAIS | Brasil | 3121407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 38ba92da-66cf-3b43-b0b9-ca99667041b3 | -20.66174 | -43.14204 | 2025-09-12 04:29:00 | NOAA-20 | PORTO FIRME | MINAS GERAIS | Brasil | 3152303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 506e3275-c779-3598-b769-af4e7c86bccd | -22.7054 | -48.6929 | 2025-09-12 04:29:00 | NOAA-20 | LENÇÓIS PAULISTA | SÃO PAULO | Brasil | 3526803 | 35 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b63413f6-b349-34f2-a7b1-a730bd118738 | -22.18163 | -49.73291 | 2025-09-12 04:29:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 02462b0f-8fc0-39b6-a922-0ddee82d9727 | -23.39743 | -46.70846 | 2025-09-12 04:29:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7bc3822c-a04a-3173-8030-67ce94fb589a | -22.62324 | -53.09201 | 2025-09-12 04:29:00 | NOAA-20 | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| e40b8bcc-4a69-368f-bf76-0362d1c4e69e | -23.38601 | -47.01597 | 2025-09-12 04:29:00 | NOAA-20 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 6c46ac9f-baa9-393b-ba4c-bdf282dd9480 | -21.84587 | -46.51394 | 2025-09-12 04:29:00 | NOAA-20 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 31dcd04f-93fe-36cc-9aed-144a0d4ad9af | -20.56779 | -43.74448 | 2025-09-12 04:29:00 | NOAA-20 | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 5e075832-af6e-33a2-ac30-8c460cc9c2a2 | -19.99476 | -46.92119 | 2025-09-12 04:29:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 49c200e9-e015-3514-a61c-062b5a9e1f93 | -19.99953 | -47.65178 | 2025-09-12 04:29:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7970f59e-1fdb-3da5-af30-d9efcbd1016b | -21.94083 | -47.56166 | 2025-09-12 04:29:00 | NOAA-20 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3523a607-dd79-3ff3-a020-8c2db1167714 | -22.61153 | -47.22956 | 2025-09-12 04:29:00 | NOAA-20 | COSMÓPOLIS | SÃO PAULO | Brasil | 3512803 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4b33db21-a716-3179-a8fa-1ee574af01c0 | -22.19589 | -49.59757 | 2025-09-12 04:29:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7b0d0bc8-0227-3c6e-b3a4-7ff3eb662d33 | -20.00173 | -46.92238 | 2025-09-12 04:29:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 13143230-0791-39e6-b760-a9931ef2fc0d | -22.69888 | -46.22191 | 2025-09-12 04:29:00 | NOAA-20 | ITAPEVA | MINAS GERAIS | Brasil | 3133600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| b92bb70a-09b0-34dd-8fb8-6df6796033d7 | -23.13712 | -47.15106 | 2025-09-12 04:29:00 | NOAA-20 | INDAIATUBA | SÃO PAULO | Brasil | 3520509 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 2866a649-fb23-3c01-9aba-026e9e9530c5 | -21.97322 | -47.55875 | 2025-09-12 04:29:00 | NOAA-20 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 07eac10a-8336-3cce-8255-ae65cbbe422e | -22.39822 | -46.74709 | 2025-09-12 04:29:00 | NOAA-20 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 692c28c7-aa42-3a0f-b993-4879cf692ec4 | -20.89487 | -55.17602 | 2025-09-12 04:29:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 677d8bc0-f540-3677-96a0-26949f57fbd8 | -27.87733 | -51.95929 | 2025-09-12 04:32:00 | NOAA-20 | FLORIANO PEIXOTO | RIO GRANDE DO SUL | Brasil | 4308250 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b4a65d57-21d3-321b-a7b1-7b2278428ffe | -27.68893 | -48.74982 | 2025-09-12 04:32:00 | NOAA-20 | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ae58d166-06df-380a-90c7-1e44eda06e4b | -29.67518 | -55.50595 | 2025-09-12 04:32:00 | NOAA-20 | ALEGRETE | RIO GRANDE DO SUL | Brasil | 4300406 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| fc5aa47b-2722-3d4c-9648-afe6d29f5294 | -27.68543 | -48.74923 | 2025-09-12 04:32:00 | NOAA-20 | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 394d8e37-019e-3d3c-a37f-27a7c210d882 | -30.80453 | -51.52679 | 2025-09-12 04:32:00 | NOAA-20 | TAPES | RIO GRANDE DO SUL | Brasil | 4321105 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| bfeb6766-45a8-337e-9b54-9f41d5f0ebcf | -27.8767 | -51.96319 | 2025-09-12 04:32:00 | NOAA-20 | FLORIANO PEIXOTO | RIO GRANDE DO SUL | Brasil | 4308250 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 40fb70a0-f929-3399-9c65-e06d8c3254de | 2.50539 | -61.03197 | 2025-09-12 05:14:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7aff9743-d4d4-36c4-9667-8c77532c6768 | 3.36913 | -61.22433 | 2025-09-12 05:14:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d8efb543-5d71-379d-ab42-b0742458ed05 | 2.50575 | -61.02924 | 2025-09-12 05:14:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 70e0aaf3-5729-3f16-8f48-a80d1ba2c50d | 4.11417 | -59.97536 | 2025-09-12 05:14:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 7f0cac99-bcae-3b28-b483-09ce71328308 | 4.11714 | -59.97052 | 2025-09-12 05:14:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 03c0ecb7-47af-31bd-bbc6-c6b1918d9891 | 4.11779 | -59.97479 | 2025-09-12 05:14:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4cba276f-cdcb-393c-9ccf-2372f2fa10f8 | -5.48565 | -60.13386 | 2025-09-12 05:16:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1b7e6755-a88d-355c-86f5-b31eaf5423c5 | -4.53431 | -55.68459 | 2025-09-12 05:16:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c74886eb-17f1-37a1-afc6-71bf93883ea4 | -5.27997 | -49.29469 | 2025-09-12 05:16:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c4694978-cf24-3df5-ac65-1931df424b4a | -6.81865 | -51.89163 | 2025-09-12 05:16:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0c7e1d3c-a59e-3d01-a69d-017d47320214 | -3.32304 | -50.07949 | 2025-09-12 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 89a487d0-68e5-3392-9a57-8d902df408d9 | -6.15377 | -53.68533 | 2025-09-12 05:16:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6e984d99-7990-3603-9c5d-e6edc22e88e1 | -3.07498 | -48.82028 | 2025-09-12 05:16:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5dac0a75-c941-3888-9162-28d98790f089 | -5.27947 | -49.29826 | 2025-09-12 05:16:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee7d103e-4f5d-35e0-b45b-e9f31dcdffd6 | -3.67869 | -47.49605 | 2025-09-12 05:16:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 94aef5c8-ea3d-3674-a3d0-1f175df552a5 | -6.108 | -45.93807 | 2025-09-12 05:16:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 17556966-8ad3-3b5f-a2b8-4ddd534ab7be | -2.95445 | -51.66606 | 2025-09-12 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 376b65ee-9730-3c70-945a-bb9435d78a8c | -5.64793 | -51.8672 | 2025-09-12 05:16:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a0195f7d-9753-30e6-86b3-27ac6704192c | -3.59538 | -49.45845 | 2025-09-12 05:16:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef4512e9-6458-3991-b121-efd5727f922d | -5.69902 | -49.19901 | 2025-09-12 05:16:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6cf97e59-c893-3819-9c3a-fe260dafcea4 | -3.40256 | -60.39424 | 2025-09-12 05:16:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d7a48203-01fa-3a71-9adb-a576b99f5940 | -2.92178 | -48.63181 | 2025-09-12 05:16:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e6ee870-0d1b-3ff8-918b-6bc5e2536211 | -4.92858 | -55.78121 | 2025-09-12 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d5d4d85c-d0c8-3b1c-820c-abe9e5f40557 | -6.17324 | -47.28593 | 2025-09-12 05:16:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 53f51618-7027-3a9a-9ced-a373da912f10 | -5.94316 | -52.05924 | 2025-09-12 05:16:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de4bacf7-51b8-388e-b1a9-c45fec66459c | -3.22259 | -47.12605 | 2025-09-12 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 4b13b7e5-a4f2-3442-91d5-a7d4d234e647 | -3.69391 | -49.10535 | 2025-09-12 05:16:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7df7c5de-c0dd-3304-9cf3-129deb7166fd | -1.46358 | -54.12246 | 2025-09-12 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c95ce5ee-8306-3fd9-b66d-de71d79bf740 | -3.26214 | -48.46334 | 2025-09-12 05:16:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c59cde56-ce60-3d29-b18e-723f4b051802 | -4.88798 | -56.0459 | 2025-09-12 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a97ab211-c24b-3381-b842-4438e0cc554c | -3.07431 | -48.81985 | 2025-09-12 05:16:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| da87eeae-8049-3213-974a-1749782d8b29 | -3.21576 | -47.12982 | 2025-09-12 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b6c4f535-61f0-32b6-93fb-d3fde46618f9 | -3.26322 | -48.45589 | 2025-09-12 05:16:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| db9a57ce-8f3f-3d9c-976a-2d6f17ae77cf | -3.53233 | -59.57595 | 2025-09-12 05:16:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f4b9e943-6dc0-3a5e-b979-dfad043da0ae | -5.69857 | -49.19879 | 2025-09-12 05:16:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b1aca872-8fac-3cea-9a7c-e2967feae786 | -4.39749 | -48.91713 | 2025-09-12 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| badfaf89-eff9-35bd-9739-1c85993f4070 | -3.32346 | -50.07658 | 2025-09-12 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 89235216-363d-334a-bda6-25918c7296f5 | -4.16408 | -56.14019 | 2025-09-12 05:16:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c7f318fd-8884-329c-89e9-adb9ac0b5a9d | -3.26268 | -48.45963 | 2025-09-12 05:16:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8295278b-1bad-37d4-8402-79f9e01b916a | -6.78442 | -52.27732 | 2025-09-12 05:16:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README98.md)
