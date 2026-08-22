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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 738d522d-3173-385f-a6b5-71f3a789b4db | -8.53209 | -55.32772 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ff035d4-ce0f-3a54-ac02-2bc51271d9d5 | -6.01344 | -57.7994 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2294abdc-6b50-3cfc-aa0c-92f42636a458 | -11.16121 | -54.01082 | 2026-08-22 05:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 18bdf1a2-1e2c-375e-a61c-ec87ec4af7ef | -6.89738 | -55.70927 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0b5b05e6-1e27-33d9-8b18-6e1cce4d4cdf | -6.16835 | -55.44324 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02d34b3c-7c1b-31bc-81a7-11e09da68f4e | -13.37465 | -41.34648 | 2026-08-22 05:04:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4a73f7d7-6693-38e8-9d2e-e2dc819a15cc | -7.25681 | -49.90166 | 2026-08-22 05:04:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26773d4d-b4a6-3266-bd6c-8097a7b2e5ba | -10.51667 | -50.77192 | 2026-08-22 05:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 01448734-af15-3e0b-955b-d1d3584369e3 | -6.77856 | -58.6651 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f3f8615-31ff-3724-8cae-daa4ab03ef40 | -9.43025 | -51.65883 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd0e2fe4-06f0-3c60-b104-c30453c690be | -9.40372 | -60.58399 | 2026-08-22 05:04:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1c75451-a4b7-3bf1-a8db-08273336c82d | -6.7601 | -58.6551 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c4177271-f5b7-355a-9159-29d9c179389f | -6.93467 | -60.08466 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09fd965c-637b-3c46-95cd-d360770fac83 | -6.37962 | -54.94371 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 403b11e9-c1f0-3dd8-a881-c7f6221342bb | -6.76851 | -59.4453 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c7aac63e-0650-3772-bf8b-22714890ce3c | -9.26834 | -45.64578 | 2026-08-22 05:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a4e7369d-cf7d-300c-8ba3-2396f57c5380 | -6.85737 | -59.42159 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 05900094-5975-3780-b54a-04488a2012da | -6.94316 | -52.78219 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f19deeec-9eee-3bca-ae37-ec79cf0187db | -7.48504 | -43.81448 | 2026-08-22 05:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| bc1dd060-4dda-39e0-b9c9-e5d4278af479 | -6.96638 | -59.0583 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 01c97469-bbfb-3029-94f3-a2c1ac3f9db4 | -7.54995 | -55.56068 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ee9aee45-9528-390e-b385-70b15cfa0060 | -10.87684 | -50.22726 | 2026-08-22 05:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 70481b50-e333-36cf-84f4-74bb9576f43a | -6.92719 | -59.31116 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 71c9fdc4-32b0-38a8-a75f-b717fbf506fd | -6.8879 | -59.43157 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 16719e06-872a-3b00-8f5f-eaeaf619f624 | -12.7903 | -48.45622 | 2026-08-22 05:04:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 21fb9636-1968-3e50-a1aa-ed5bb6ec12b3 | -8.56199 | -54.71931 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 860c1e51-dd01-39d1-899b-881c9baabb9b | -9.41557 | -60.41268 | 2026-08-22 05:04:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 98528b54-e1aa-33b7-9f3e-311b21fcbf93 | -6.54105 | -58.51759 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e9ed0a8a-ccd6-3cab-b5dd-acbcee70aace | -11.44352 | -44.53455 | 2026-08-22 05:04:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 21f98ce4-51a0-3eb0-a907-23a0b3a87d4e | -9.21684 | -60.77648 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c3cfb807-efe0-3df9-89fb-9a89b8938196 | -8.09694 | -50.03433 | 2026-08-22 05:04:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5154c20c-fdab-3466-9ca3-2ac0774f83dd | -9.43712 | -51.63708 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a8130552-131d-35e3-9fcb-0518c716b2e8 | -8.16121 | -46.71809 | 2026-08-22 05:04:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 52f26928-b9e2-38fe-a38b-85b92c861c6a | -8.17213 | -54.98839 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d4e634ca-ebbe-3c08-8f63-568716925705 | -6.22932 | -55.61813 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| fc764d73-e490-3e9a-a902-af546de209b4 | -8.53175 | -54.8193 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c7e70a5e-1aad-31ed-ad09-192dd6276e15 | -8.54182 | -55.33325 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b3e2c22b-49e3-3e61-8a5b-a6e4dbfa2b55 | -10.94881 | -51.41761 | 2026-08-22 05:04:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3be32aef-1ce6-35cc-b5b4-4ea263b022b6 | -8.62659 | -54.68517 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f1bfcfc-4fdb-3449-9e7f-e1d4e2c7ca41 | -6.93315 | -59.30314 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4ddc96b-96d8-31bf-a8f9-c75455208a0e | -12.09925 | -56.31785 | 2026-08-22 05:04:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f0113164-a9af-3043-a76b-ce8efb076385 | -6.43157 | -54.96332 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e927b3c5-0627-3e72-a854-c3515dc6a564 | -6.36914 | -62.90368 | 2026-08-22 05:04:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 720bd809-2bfd-3435-be89-d420cc7d8114 | -10.73855 | -58.90617 | 2026-08-22 05:04:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1afe33e-09ac-3ff2-b490-438ea5c031ab | -6.42014 | -52.7314 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4cf9758b-91a3-3e8f-8723-f657f90ffb9b | -11.17225 | -54.02706 | 2026-08-22 05:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c3de2524-0c55-357d-b31c-ff44998285d0 | -6.76912 | -58.70602 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 547c1587-1799-31da-b3bd-212d3468bb26 | -6.44092 | -60.07482 | 2026-08-22 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aefbc7db-9b4e-315c-801e-6d08787e9fad | -6.66613 | -56.34097 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d3ddeff-8ce7-357a-9dd4-485d433e63cf | -6.75877 | -58.66299 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 16.3 |
| ef7bbfef-8804-3293-bd50-2f8380cf28a7 | -6.79328 | -59.4358 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 6eac783f-e284-3214-be61-fa8cfbaea618 | -11.44047 | -44.55878 | 2026-08-22 05:04:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2c3b19e9-123e-3345-bd64-db66ea47dde3 | -10.24331 | -50.36352 | 2026-08-22 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cc52029f-afbc-3d45-875f-e8c37e08ef48 | -8.40662 | -62.68795 | 2026-08-22 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a2c28d0d-d8b6-3352-9863-e712e42d030a | -7.16908 | -42.74835 | 2026-08-22 05:04:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| bc3225c4-53fe-32b5-9425-1cf726c70bc5 | -6.3651 | -62.90187 | 2026-08-22 05:04:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c938693d-1bf4-3511-a8a7-e708d36c9dbf | -7.17833 | -60.6492 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 89a1af0b-c0dd-3af3-a726-5329e63b19f6 | -9.20929 | -59.77818 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 96d5b449-0ec5-3d8b-b52f-198d751221bb | -8.10683 | -51.66453 | 2026-08-22 05:04:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e15229d-4b5c-349b-8e5b-b1d264264f21 | -6.61037 | -58.38866 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b40f0c9a-eff7-3172-a2f1-e8fed496b79f | -9.11341 | -60.34015 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2e7b089c-80d3-3ea3-ba57-b503fa4c0579 | -6.79907 | -59.01006 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a067430-a709-3267-8da3-02ea49339a70 | -9.0019 | -50.71812 | 2026-08-22 05:04:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3fb558dd-7241-31c1-92be-a08d92c223ac | -9.4434 | -51.61918 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a19598e6-d847-38bc-85e9-1623ebafdd2f | -9.51858 | -51.64973 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 416f6687-9e48-3ebe-9e55-87b044bd788c | -8.61454 | -54.71679 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0f2802ab-fbde-3762-addd-5f5cdb4c2edc | -9.00064 | -50.75016 | 2026-08-22 05:04:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 287f20b4-5e95-3ce5-bfb4-1c34b262721a | -6.79112 | -59.42163 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 2382abb3-3217-3a0b-a6cf-2ab99f127d63 | -6.90849 | -59.00268 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 626e951d-2c10-3cfa-a5e9-d3f500e1facf | -6.15325 | -53.70391 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 994e3d95-9048-3278-a05e-db6ae80930e8 | -9.03873 | -60.44801 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| abd194b4-3d35-39d4-868c-3ffacc963c7a | -6.77314 | -58.6819 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 51a1d4ea-4f3a-34d9-a3f2-8943c7a6419e | -12.27618 | -43.16813 | 2026-08-22 05:04:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 5bf702f3-31db-3f31-9d12-b0c5619e223a | -6.80456 | -59.6683 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a290858f-f580-3496-a4ac-43eb75093154 | -6.79284 | -59.5999 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0c5fa301-ceb4-39bf-af54-e07c9b4bb603 | -6.86765 | -59.44176 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d5c40da6-7ec1-3423-89b7-117b542355bb | -8.80728 | -48.54857 | 2026-08-22 05:04:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 4.7 |
| bf302266-b840-354b-9af4-8a21fb1a5a12 | -6.76693 | -59.45432 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4f609d1-7107-3c53-b277-efcb7b8b5dc5 | -8.58436 | -54.75288 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e2a86de-6144-3a6b-8f61-5d975a369a26 | -13.44948 | -51.75898 | 2026-08-22 05:04:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3e643bb7-66e2-3174-935f-9722890ef7ff | -10.73607 | -50.27077 | 2026-08-22 05:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cccc377a-1fa9-37a8-a1a4-f37e162cb8ca | -6.89044 | -59.02977 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ec77afb6-5408-3920-a680-1d745f7259ab | -8.18833 | -54.97534 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ffd20f4a-d9c5-382e-b1e0-62e4800e56cb | -6.25561 | -55.41513 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 73d75cc0-89cf-31c0-a60c-53eaf72fe836 | -10.90508 | -50.2405 | 2026-08-22 05:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| da9401b1-459e-3147-bcbd-f6823200b472 | -6.23581 | -55.40902 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fda75545-8cd9-31bc-bb0c-b3aff9bc728c | -12.01072 | -53.4291 | 2026-08-22 05:04:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 645aa6e4-ba70-3c7d-8000-f6b6e3f66562 | -8.09781 | -51.65564 | 2026-08-22 05:04:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d97bc9c8-23fc-3316-98cc-770fb52ae45a | -10.757 | -50.2561 | 2026-08-22 05:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5d13e0f1-2dc1-34a2-9fc1-a64f09fbd662 | -6.79713 | -59.4136 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 079ddee3-8674-368f-9a82-1a3314967698 | -7.263 | -49.88507 | 2026-08-22 05:04:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 031941b4-1c65-38de-a223-e6ecc149f776 | -8.5982 | -54.71038 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7fc61191-20cc-3c00-a367-d89a0a673e14 | -10.24995 | -50.36889 | 2026-08-22 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0be50bb6-58ee-3550-be2b-be451e397c8e | -6.80687 | -59.4106 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8c320585-7c13-36e4-8955-eb838e223404 | -6.00937 | -57.79871 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62a0bdef-6c21-3add-9714-09744ee1ce6a | -13.45946 | -51.76464 | 2026-08-22 05:04:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8dfb2c1b-2af2-38f5-9659-e500e66df475 | -6.55405 | -56.54692 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d4250f1-2179-3f27-984b-2cb52cf2695d | -8.80409 | -48.54277 | 2026-08-22 05:04:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 583ec9da-0cee-3307-aa5b-32c2c7008844 | -6.69476 | -58.93705 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9da28268-b766-3a6c-9118-0ccfc050e06d | -8.61278 | -54.72773 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README53.md)
