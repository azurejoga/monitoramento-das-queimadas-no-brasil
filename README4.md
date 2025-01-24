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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 986d0e99-76ea-388e-a1ca-d4f71e5abb5d | 0.87998 | -60.15165 | 2025-01-24 04:53:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 49e09733-84b0-3db0-90cd-a595e4bd33b8 | 0.98717 | -59.49287 | 2025-01-24 04:53:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 63ae605d-b45f-3581-9bdc-9286a4fed1b9 | 1.10918 | -59.46222 | 2025-01-24 04:53:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 09232b88-4bb0-38f8-9c8a-bd5ad7c0494a | 0.88561 | -60.15617 | 2025-01-24 04:53:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c7002aa2-e03d-37ef-9d72-d68d55724350 | 0.88505 | -60.15398 | 2025-01-24 04:53:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 89c204d1-6d8d-3a6b-b7a7-c04f97b04445 | 1.10937 | -59.46491 | 2025-01-24 04:53:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d7d5aca3-2b6a-3490-9cce-39dabee5c914 | 0.88584 | -60.1592 | 2025-01-24 04:53:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 17284307-4601-34e5-b96e-76f704f6b730 | 0.88479 | -60.15096 | 2025-01-24 04:53:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c0548cc3-e942-3332-b842-bebfb2ebba9f | 1.10866 | -59.46021 | 2025-01-24 04:53:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b06a1267-82ec-313f-ac9a-e16791d5256b | 1.10844 | -59.45753 | 2025-01-24 04:53:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e0fd16d6-ff15-340b-9306-558bbaee5166 | -6.64206 | -47.3521 | 2025-01-24 04:55:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0a3a7693-55b4-3903-b6d2-b39f9ff75a43 | -5.28423 | -56.02045 | 2025-01-24 04:55:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25880a87-9bb1-324f-b26a-c363563700bf | -3.31443 | -52.44099 | 2025-01-24 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b9ef4a6e-8a2d-32a4-b55c-5ff0e46341fe | -6.23069 | -55.63108 | 2025-01-24 04:55:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 21433fdb-ebde-32ae-92f4-8e382db167f9 | -15.27046 | -51.46899 | 2025-01-24 04:57:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 206c59b6-9aad-36ba-bc35-247a966dd071 | -15.23909 | -60.22317 | 2025-01-24 04:57:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 1857df9f-cf2d-3344-afbd-3f164eeca3dd | -15.97833 | -56.37292 | 2025-01-24 04:57:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 6ad36aab-37c6-381f-b892-555fd25b4741 | -15.21525 | -56.1513 | 2025-01-24 04:57:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8893f207-70c0-365f-bec9-a3f7cb6edf6f | -11.6517 | -58.20759 | 2025-01-24 04:57:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a8c80559-adbb-3a96-9da0-42841934e55c | -15.54984 | -55.23608 | 2025-01-24 04:57:00 | NOAA-20 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 11509b68-57f3-387b-b46c-664bdedf5fbd | -9.26173 | -60.31544 | 2025-01-24 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e5bf482a-0d60-3dbc-a7b6-f1abaeefccc9 | -15.24283 | -60.22385 | 2025-01-24 04:57:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 996d2cd5-3070-30e0-8dd6-acda3ab8c185 | -12.77076 | -44.84252 | 2025-01-24 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 03c90ce4-6af1-3708-b5d7-43335669ca3d | -9.25696 | -60.31845 | 2025-01-24 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 880b1656-bd77-3b82-9cab-414566b8f286 | -11.02243 | -45.05949 | 2025-01-24 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4a62767b-f041-3189-93a2-d6838bc24c61 | -10.35023 | -47.90897 | 2025-01-24 04:57:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fc6177ba-c6bf-3647-8b28-b2b3eb0ea328 | -11.65589 | -58.20417 | 2025-01-24 04:57:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 521b997a-643c-307e-92be-6ad6d1e5fe63 | -15.24031 | -60.22095 | 2025-01-24 04:57:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e53c8d0d-1eb5-3e86-a29a-2d8840047e94 | -12.94853 | -61.3418 | 2025-01-24 04:57:00 | NOAA-20 | CORUMBIARA | RONDÔNIA | Brasil | 1100072 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7c81b494-75db-3ffa-9a82-e437adc8d148 | -11.02291 | -45.05553 | 2025-01-24 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9fc8cf8a-5ae6-3ae9-9cac-b028b279ff45 | -15.23081 | -60.22646 | 2025-01-24 04:57:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d2b6cb88-3b0b-3765-90a0-5f26450c8941 | -12.3754 | -64.00648 | 2025-01-24 04:57:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0d7f9fe-bc17-35a0-92e2-b9ab6f4284c2 | -11.65236 | -58.20355 | 2025-01-24 04:57:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db15d565-83e1-31f9-a22b-8f148b3b9b6e | -15.23456 | -60.22712 | 2025-01-24 04:57:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2c4ea11d-1df7-3e3f-b18c-2698afc48b27 | -17.03675 | -50.21033 | 2025-01-24 04:57:00 | NOAA-20 | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2622d5c6-5d4d-364f-97cb-5282963d47ed | -15.26903 | -51.47939 | 2025-01-24 04:57:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 40522a59-9bc0-35a2-91a8-0266aecca45b | -12.76534 | -44.83741 | 2025-01-24 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0903497d-d3e0-3be5-9b9e-656fcd9855cd | -15.23949 | -60.22555 | 2025-01-24 04:57:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 45e29ff0-3514-3e01-ab55-a6d5d629cd50 | -15.2383 | -60.22778 | 2025-01-24 04:57:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| e91edf8b-1ceb-398a-a743-1655dba77df0 | -12.37485 | -64.00941 | 2025-01-24 04:57:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 349a1a81-d067-319b-9b4d-893f6286ab5c | -12.37476 | -64.00883 | 2025-01-24 04:57:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ca00359d-3dbd-3f0b-b45e-d80619a6a936 | -9.26108 | -60.31916 | 2025-01-24 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3ba064c9-cd37-3580-95ed-b5af17add938 | -10.35088 | -47.90415 | 2025-01-24 04:57:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 521247db-507f-3741-9113-50995326bfa6 | -12.74708 | -44.83941 | 2025-01-24 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 207f35e0-faca-3e41-b28e-ae3b2925f929 | -12.24619 | -63.84206 | 2025-01-24 04:57:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d8098c3b-2be6-300e-bd8c-820e6dcdec14 | -11.65017 | -58.19487 | 2025-01-24 04:57:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 025aa740-6a0e-3535-9403-ce1a3fb594de | -15.26974 | -51.4742 | 2025-01-24 04:57:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e9a4840f-6fe2-32ee-a8d5-dbe48eef43ca | -11.63885 | -61.63636 | 2025-01-24 04:57:00 | NOAA-20 | ROLIM DE MOURA | RONDÔNIA | Brasil | 1100288 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cdf7c906-8411-345f-a13e-d87fb7f648fa | -15.24405 | -60.22163 | 2025-01-24 04:57:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3cd82c9b-322a-37d4-a2ff-2b1703d749ea | -12.74166 | -44.83424 | 2025-01-24 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 493cfca0-a805-346b-9018-38a065a3ddb0 | -10.34623 | -47.90337 | 2025-01-24 04:57:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 395cca7a-8d66-31f9-9fac-def7b739e14d | -12.74116 | -44.83857 | 2025-01-24 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 84eab18b-5e41-3fb1-a58b-4a51f90dc34f | -15.24323 | -60.22623 | 2025-01-24 04:57:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3e7e474c-0aa0-324b-ad21-f7c74d76aa42 | -11.02815 | -45.06018 | 2025-01-24 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7d61925c-ba53-3a64-a645-7af44a3397f1 | -11.65303 | -58.19952 | 2025-01-24 04:57:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a613ce8d-7da3-3652-8490-4a9966971e11 | -15.23535 | -60.2225 | 2025-01-24 04:57:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| adec9ad1-6c58-32e4-8441-e88a2c0e2fa7 | -9.25762 | -60.3147 | 2025-01-24 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| cbc36176-e2f0-3ca3-95c2-69d2f7eab82d | -16.17532 | -60.14338 | 2025-01-24 04:59:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 661f4125-b75d-315a-a2ea-5211b8009052 | -16.30805 | -58.46289 | 2025-01-24 04:59:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 31134ea0-d4b5-3611-9d75-bcf712b20784 | -20.54778 | -55.84548 | 2025-01-24 04:59:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 92f0cac1-27cd-3b9f-b90b-4080cc107752 | -16.10172 | -60.07168 | 2025-01-24 04:59:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b063f8d0-c7a6-31a5-b770-6a683d3db55e | -16.17087 | -60.14718 | 2025-01-24 04:59:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cf1dbab6-a9c4-3acd-9565-5881691d3b63 | -19.50768 | -55.31327 | 2025-01-24 04:59:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 6a01e447-e12b-3e96-88cd-e21df00fc676 | -18.44749 | -54.54747 | 2025-01-24 04:59:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b3c63f74-6715-3dc9-8777-7230403b7bf7 | -20.54438 | -55.84491 | 2025-01-24 04:59:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d41903f7-86d3-3562-a901-339c215e178f | -9.259 | -60.309 | 2025-01-24 05:00:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 69f4a236-dce2-311e-92a2-096385a3abd2 | -9.259 | -60.309 | 2025-01-24 05:20:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.3 |
| eb8e1c77-d54c-3890-bf89-27c0b08c7b20 | 4.26736 | -60.63531 | 2025-01-24 05:46:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c19b0e7a-9496-3475-bd1e-4a88f8586e74 | 1.38422 | -60.79732 | 2025-01-24 05:46:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b051b725-190e-3637-ac5b-c2ce9a6634cf | 1.05606 | -59.90226 | 2025-01-24 05:46:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 30afbb0c-3c1d-3ec9-8eb2-6298ba0292a8 | 1.10676 | -59.4582 | 2025-01-24 05:46:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3459873f-eb34-3099-870b-a2c6202d032f | 0.88285 | -60.15287 | 2025-01-24 05:46:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 221b4c08-5f93-33d3-847b-407771d54796 | 4.27479 | -60.63401 | 2025-01-24 05:46:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 17a36add-9dc3-3862-b62a-90e9cfe846f4 | 4.27108 | -60.6347 | 2025-01-24 05:46:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33172253-a476-3a01-b7e4-36f42c22324c | 1.10737 | -59.46206 | 2025-01-24 05:46:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2e29b42a-7a75-3ee6-bd0b-4b46d67eefbe | 1.3281 | -60.03944 | 2025-01-24 05:46:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c3249176-de1c-3fa2-a06f-95e19af385c8 | 0.98646 | -59.49165 | 2025-01-24 05:46:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| abfaa2fb-9f71-3edc-b594-ddf59ae852d2 | 0.87883 | -60.15354 | 2025-01-24 05:46:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8298e24f-cd56-3909-9f41-45069341e7a1 | 1.38581 | -60.7996 | 2025-01-24 05:46:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb688e0a-417d-3a02-9663-275beff179b0 | 0.87938 | -60.15703 | 2025-01-24 05:46:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| cebc5c3b-9a8b-38e7-9bbd-11815724a9ca | 0.70535 | -59.33083 | 2025-01-24 05:46:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cb04dbf3-33f6-384c-8dbd-e2997bf147c9 | 0.97472 | -59.83578 | 2025-01-24 05:46:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c077214-3927-3900-aaa2-40143271fba9 | 0.8834 | -60.15638 | 2025-01-24 05:46:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e0c4c09a-0628-3896-b60c-37e5f693ac4d | -2.98212 | -60.98157 | 2025-01-24 05:48:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d8cc6c8f-85ff-3733-8aa9-3c416e36868b | -15.236 | -60.22789 | 2025-01-24 05:50:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a43d422a-7964-37c1-981a-9e21386b650f | -15.24144 | -60.22554 | 2025-01-24 05:50:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 304d3e63-1d5c-3c9b-9e80-15f906a3b8d2 | -15.23129 | -60.22402 | 2025-01-24 05:50:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c7ef6561-9149-338c-9206-c6288a3f5292 | -15.23672 | -60.22169 | 2025-01-24 05:50:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9e6d5d7a-7625-3c15-a0ed-a1871f9920c2 | -12.24377 | -63.84255 | 2025-01-24 05:50:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5dd630dc-c461-3807-a8e5-c2a36c984703 | -11.65394 | -58.20655 | 2025-01-24 05:50:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 16579918-cf62-36c0-97be-a353c3e07cd9 | -9.25856 | -60.31175 | 2025-01-24 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 965e42fd-4b37-3023-a3f9-c5dcb71773bf | -11.65485 | -58.19906 | 2025-01-24 05:50:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa893444-28c3-36bf-94df-1ac8afa6d56c | -12.37465 | -64.00801 | 2025-01-24 05:50:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fab50645-8020-3841-b847-b1a4473177a9 | -12.04193 | -63.73922 | 2025-01-24 05:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 926ea1f0-64a5-3cd9-92eb-d6e6f723a09a | -12.37845 | -64.00857 | 2025-01-24 05:50:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0600486-620b-3c80-a467-251dd14278ee | -12.14779 | -63.81173 | 2025-01-24 05:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b80b6310-c495-3a51-8d24-71ede1f1872a | -15.23636 | -60.2248 | 2025-01-24 05:50:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ea6b8c7e-49c4-35a4-a50d-7ea0b998a2b6 | -9.17697 | -61.94643 | 2025-01-24 05:50:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5ec5efbc-90bb-396b-b1ca-0c8f10f381bc | -15.2418 | -60.22242 | 2025-01-24 05:50:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3edf6db1-1cb0-3aa4-b71f-2474951af80d | -15.24216 | -60.21928 | 2025-01-24 05:50:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README5.md)
