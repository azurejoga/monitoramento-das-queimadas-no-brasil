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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0d5078b2-c977-3ead-a00e-b363d0214ec3 | -14.83023 | -48.18064 | 2025-09-06 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eb208d06-c170-3ffb-b06a-b84b7567c2f4 | -11.21864 | -55.02211 | 2025-09-06 04:40:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5fbabec3-8383-38d0-a32a-ed1cd05f7366 | -13.60227 | -43.12575 | 2025-09-06 04:40:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 119b904c-c7d9-3fd3-b219-cd350755605e | -12.63574 | -56.98815 | 2025-09-06 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c2d64043-3921-39b1-ab2c-01bf87bead2f | -15.14137 | -52.34188 | 2025-09-06 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 06fc8965-650a-3d22-8cf5-0a7ca1a6b3cd | -12.19185 | -53.89789 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 677add3c-c63e-3f88-91ed-1e51b1c4e84d | -15.18577 | -47.98801 | 2025-09-06 04:40:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1a92b14a-736b-3ee6-8d87-affc70b95bd5 | -12.99992 | -54.81128 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 968436ec-2f26-3df2-aff0-48675062bd62 | -12.95816 | -54.80125 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bd67fc74-e12d-30ef-88e9-761652385e27 | -13.00263 | -54.83997 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ec843063-13c4-33a7-9302-161b1ab05420 | -10.31568 | -46.40881 | 2025-09-06 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c714f2a1-52c5-32a2-98da-28942c48ce51 | -9.4629 | -60.5214 | 2025-09-06 04:40:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b23a948-ae72-3c2c-857a-5ae5ed4b3924 | -12.48651 | -53.86767 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 103d32b5-5c36-3c3d-b658-c6fd63bd422e | -9.71311 | -49.49467 | 2025-09-06 04:40:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| a764e194-3f5f-3a23-841f-b19a0b340ca3 | -12.50291 | -53.85767 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1d2a08ef-c3e4-30f5-8395-490b3844bbe7 | -15.70177 | -53.58538 | 2025-09-06 04:40:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1db7d277-015f-3682-9ace-7c755b1e6f64 | -12.96406 | -54.81177 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 610f5619-21ee-3a09-a899-985c54c64b6c | -10.44446 | -53.60823 | 2025-09-06 04:40:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98436ba8-014e-38c4-b867-6320c74493d3 | -11.64411 | -52.22553 | 2025-09-06 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77278e26-074e-3017-95fa-e9c75c62c2ee | -14.70328 | -50.24498 | 2025-09-06 04:40:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fadac765-7782-388a-8156-8306eb3e565c | -11.58864 | -47.74337 | 2025-09-06 04:40:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ff91fcb-e511-310c-bee2-5984cb3eebe5 | -12.95447 | -54.80774 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 69b2162c-10cd-3df8-8e07-cce12ab2f2d8 | -13.75039 | -46.92644 | 2025-09-06 04:40:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c473c311-0718-3e14-9b5c-f80ca95f4a13 | -15.25106 | -53.80366 | 2025-09-06 04:40:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 31c70d6b-e977-3ea0-b000-18357a45870b | -10.86441 | -47.27555 | 2025-09-06 04:40:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5412ff64-ef9a-3750-b756-e51763a7d55b | -17.96486 | -44.41526 | 2025-09-06 04:40:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7554eb4e-d5ea-316c-8c65-c2b4bbf64a62 | -12.96124 | -54.78305 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a2038afe-13d0-3d60-8f17-f766f78eebe1 | -10.4727 | -53.63902 | 2025-09-06 04:40:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa44491a-fdad-31bb-9871-0f4115660b54 | -13.84594 | -46.26693 | 2025-09-06 04:40:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 92960e8a-a489-383e-8db3-d14e36cf2ccd | -13.85275 | -46.26085 | 2025-09-06 04:40:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0d996aa6-d84b-3e8b-80ca-3529ca028368 | -15.84484 | -52.27934 | 2025-09-06 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d592bded-7fbc-3113-8c21-ed5fd0e9f886 | -11.60553 | -52.18504 | 2025-09-06 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 72faa213-75e5-3af1-aea9-198debe91561 | -12.7499 | -53.98879 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d7548542-2752-3d30-b252-15a8e2b97f90 | -12.9625 | -54.82099 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 44f922ea-0f20-3b13-8648-19a606143de6 | -16.31702 | -52.93572 | 2025-09-06 04:40:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea639b66-3365-397d-ae84-72a961b4fee2 | -12.89595 | -48.01154 | 2025-09-06 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 36d9d402-4f31-3ad7-904a-471c79c4b955 | -13.79776 | -52.74672 | 2025-09-06 04:40:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d068cf1b-cf5b-35ee-a973-6726b4947cf2 | -15.21122 | -52.3758 | 2025-09-06 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 04dea84f-5dcb-39a3-837c-1c6b35a9ad67 | -13.04146 | -56.85973 | 2025-09-06 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| c5bf6c00-caf3-356f-9fa6-372adb87b2c7 | -10.06758 | -48.06495 | 2025-09-06 04:40:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f8782981-af70-3b21-a4ca-5d5791fb65f1 | -10.77924 | -47.75076 | 2025-09-06 04:40:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ec24f32-071e-36ab-a3bc-ca20c9965558 | -12.50648 | -53.85829 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2080fc9a-3749-3143-80b2-28f95b120370 | -13.01461 | -54.83735 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d47ffed7-c7f9-3346-97c3-abc1d7b5d154 | -13.30283 | -51.75408 | 2025-09-06 04:40:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3995709d-bdb1-3ee7-9eb8-4ffdf37ee9fe | -11.17812 | -55.0434 | 2025-09-06 04:40:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82b208e8-f89e-3e4e-8f3d-7766223352e4 | -13.90087 | -48.02599 | 2025-09-06 04:40:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5ab0e244-6209-3f55-93d5-5d5c487e07e2 | -15.54071 | -48.4024 | 2025-09-06 04:40:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b8907605-4c2e-3c11-aefc-27f7b50652ee | -12.98027 | -54.83595 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 458fe73f-b8bb-33f0-8571-d4f3a7c53417 | -12.60358 | -56.99478 | 2025-09-06 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 02480416-26b0-3c30-a297-74504a4d59ad | -12.7837 | -48.16175 | 2025-09-06 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cfdac4a8-9a86-3f35-8c9d-009cc656eb65 | -13.01676 | -54.84717 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 329dc94b-08bc-3c9a-a2b8-3ba2e53ad674 | -9.20936 | -57.09492 | 2025-09-06 04:40:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a2e920b-e784-3ed8-8838-2b11b24e3d88 | -16.92364 | -45.75751 | 2025-09-06 04:40:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| b9107b7a-ca6b-33fd-b6f0-4088f6ab1330 | -9.80436 | -48.30214 | 2025-09-06 04:40:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6631ed0d-27a8-3ee6-a2a3-66c62e0352c8 | -13.00671 | -48.06856 | 2025-09-06 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 60d2227a-ec8a-32bf-96dd-90b516a4e31a | -12.98441 | -56.91196 | 2025-09-06 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 65a010e8-b6f8-38c7-b84c-68c6dd444b3a | -14.82962 | -48.18488 | 2025-09-06 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6865b426-895c-3d92-868e-92c59547a068 | -11.6817 | -52.23525 | 2025-09-06 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e039cc5-f1bb-3db6-9d2e-d6aec3763b5a | -12.99034 | -54.80014 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 033a05b8-dd20-3075-997a-3c3b281b4bbd | -15.84035 | -52.28607 | 2025-09-06 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8a61235c-02c7-3a0f-a875-6a82fb604171 | -13.70911 | -46.88735 | 2025-09-06 04:40:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fac17e5f-1121-306d-b010-0fe3df86cfc9 | -15.73191 | -53.59471 | 2025-09-06 04:40:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 765bf543-9832-3df7-96d2-d98ba0f69adf | -12.9917 | -54.81441 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 606b725f-6487-314d-aac1-1a31799a0279 | -10.31058 | -46.41748 | 2025-09-06 04:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f5bbdd97-bc7d-3f24-8351-1becda77df34 | -9.97382 | -51.66691 | 2025-09-06 04:40:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d7cfd29-96dd-33cf-b5ff-fc09dc24966b | -12.9752 | -54.82093 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 66beaed2-183a-3c9b-bfbd-53876792cd1b | -12.96111 | -54.81365 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| bf6214a3-e2c2-3be6-bf55-a211aa2f98a8 | -10.8818 | -55.72894 | 2025-09-06 04:40:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29fa4300-13a9-3fdb-a0b3-628718d531da | -12.98186 | -54.82683 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7469516f-3222-3ff6-a764-26b9b71860a7 | -11.64808 | -52.22244 | 2025-09-06 04:40:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 658640ec-b434-319a-a06e-cd2757c994bb | -10.08826 | -48.09219 | 2025-09-06 04:40:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0763b5eb-27e2-3d4b-8d27-d98e72708059 | -15.17263 | -52.40276 | 2025-09-06 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d970d0a4-16f8-38ca-8844-7e3cef958901 | -12.99191 | -54.79111 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1a28dd07-d38b-3a6e-91e0-559fa0f4a5e7 | -14.54109 | -53.13419 | 2025-09-06 04:40:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| acc2f23f-1b9d-3563-9ebb-01bbf4a1de7e | -15.68748 | -53.58659 | 2025-09-06 04:40:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 084b2f8f-57ec-3586-afde-610403c44a72 | -10.60396 | -44.33525 | 2025-09-06 04:40:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 7a3aec8c-796f-3885-b972-f681c0182d4b | -16.29244 | -45.68621 | 2025-09-06 04:40:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 13c6cd6f-170f-3ea6-b34b-3f239599ca79 | -12.48506 | -53.8546 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2cfa2604-b3fa-3c99-8856-5a2777d80753 | -13.04568 | -56.86048 | 2025-09-06 04:40:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5fb82a9b-ceb2-3aef-b0f5-6c4b99628637 | -14.42958 | -52.9799 | 2025-09-06 04:40:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e29b4e99-218c-309d-97da-4af6eddb8bd6 | -13.33884 | -54.38939 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 584fd7dc-5715-3718-99e9-cc747cd1c30c | -16.31149 | -45.69585 | 2025-09-06 04:40:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 02f5620a-ff55-32cf-9953-d74b1455f1e8 | -9.32316 | -55.22372 | 2025-09-06 04:40:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fc2333d3-c33c-366b-9e82-fc47bdf55c5c | -12.72616 | -45.09626 | 2025-09-06 04:40:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9d3e2dce-fccd-315a-9ad6-a2daef2f205c | -12.87866 | -48.00508 | 2025-09-06 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d4c782fe-6758-3298-9f49-e3c6c340ec2a | -10.31704 | -51.45355 | 2025-09-06 04:40:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06859623-e30b-3792-a873-422e350a4d37 | -9.55777 | -53.59259 | 2025-09-06 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f2d14922-874d-3004-baa4-9933e19b3b79 | -12.46565 | -48.04221 | 2025-09-06 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1da42d8c-c6cf-3bf6-8b01-844ae4608180 | -12.96695 | -54.8242 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bb3152be-5751-37b8-be92-f04393dafbd6 | -12.84862 | -48.01778 | 2025-09-06 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f8326433-002d-3d51-840a-b09375608b73 | -17.69627 | -44.5062 | 2025-09-06 04:40:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9e16b1e8-0c69-3801-99f5-ecb565040c1e | -15.21803 | -52.35477 | 2025-09-06 04:40:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 66ebf87a-71e2-3eb6-ac6a-1d9484895c2b | -14.57838 | -48.01007 | 2025-09-06 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8b48b67f-ca66-3664-954d-fa68ec654249 | -15.07134 | -48.11111 | 2025-09-06 04:40:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 72270fcf-4d6e-3f21-a047-3f3a7d55c299 | -10.243 | -50.55496 | 2025-09-06 04:40:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 40e8898e-e0ca-36c7-9442-0f5c241f728c | -14.89334 | -55.80909 | 2025-09-06 04:40:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f51cfbb5-efb3-35a1-a660-4d45ccca9879 | -14.34165 | -60.33142 | 2025-09-06 04:40:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1b26de1-26c1-3efa-b3f1-f1ad6d6721f5 | -12.9997 | -54.83473 | 2025-09-06 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dc663510-7cc0-3177-9efb-1b03932c7437 | -12.50005 | -53.85291 | 2025-09-06 04:40:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4a23b66e-f94d-3ad0-9f52-bf7473558479 | -14.9081 | -55.08452 | 2025-09-06 04:40:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README74.md)
