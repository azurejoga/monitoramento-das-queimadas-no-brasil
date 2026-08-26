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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6537716d-2bea-3b98-9e62-c98f29295715 | -11.01272 | -45.06586 | 2026-08-26 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6c5f4f4a-e502-38d8-b3b9-85b71a63b950 | -12.03183 | -46.04061 | 2026-08-26 04:08:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c6545866-05a4-35ec-8597-88ea99841a07 | -6.27365 | -53.36925 | 2026-08-26 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1878c767-9533-3de3-b25e-550b61a1c452 | -13.38613 | -48.22325 | 2026-08-26 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5d58c69d-e4ae-3638-8ce8-0b6ecd1672ae | -11.79382 | -47.64089 | 2026-08-26 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0dc2802a-24b3-3843-b848-39090caaabae | -7.29071 | -44.08622 | 2026-08-26 04:08:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 946eb5e0-01be-3592-a161-316d77c2dc48 | -13.36346 | -48.1994 | 2026-08-26 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6f2f32f8-3813-31ba-8294-c66a071a8a82 | -11.81447 | -47.67594 | 2026-08-26 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cdeac703-18db-3230-ace2-759bd34107db | -12.76343 | -46.46452 | 2026-08-26 04:08:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b176ee32-2139-3c11-8593-08f0aef23df5 | -8.7665 | -49.97301 | 2026-08-26 04:08:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 48df839b-4dac-3605-9b46-c2d89c7e4aa7 | -8.16896 | -46.19809 | 2026-08-26 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 46c1379f-e516-3edb-bed0-e384b48c2bf7 | -8.00991 | -51.81256 | 2026-08-26 04:08:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a4391d8d-fd21-306e-99db-daeeba5ec0d6 | -7.29443 | -44.08683 | 2026-08-26 04:08:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4b031388-e811-325a-bb12-df1df2b7a0e1 | -7.08763 | -42.17963 | 2026-08-26 04:08:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ece1f21c-19a0-3cb0-b08c-f5bd7b98a967 | -7.13699 | -42.77619 | 2026-08-26 04:08:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8b926302-43da-3f99-82a1-fcceb2d9e82e | -8.01439 | -51.81911 | 2026-08-26 04:08:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 36c1abb7-a382-320b-af27-2a80b2189fe1 | -8.0091 | -51.81372 | 2026-08-26 04:08:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e5dfa88e-6466-3ac9-b250-e4c0337759af | -8.06905 | -47.52632 | 2026-08-26 04:08:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3dbd26e6-fc8a-3bfa-aec6-d01835eab45f | -10.01981 | -46.4203 | 2026-08-26 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 89566646-d7cf-34a5-b049-3d28b914d8a8 | -9.66473 | -55.08407 | 2026-08-26 04:08:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1cf47e25-8b90-35c2-8520-5b583a83b584 | -11.15463 | -54.00499 | 2026-08-26 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 93d96bb9-3608-3638-821b-71d731633108 | -10.76496 | -54.04433 | 2026-08-26 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 2c45a22e-88d6-3def-9c6e-f1bb5cc7f98d | -7.31704 | -42.98102 | 2026-08-26 04:08:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| c6186b7e-4b91-3ca8-8583-e841062d06ed | -6.26444 | -53.38046 | 2026-08-26 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9f811351-6ff5-3cb3-99f8-09bafbb1d600 | -9.16928 | -49.9828 | 2026-08-26 04:08:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3da0379d-f2dd-3492-8aa8-583d541bc049 | -7.14177 | -42.76899 | 2026-08-26 04:08:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0f7f922f-c9e9-3e2d-b9ba-acd4478e2756 | -8.16823 | -46.20226 | 2026-08-26 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 69bca7a6-894f-34a0-ad69-71b555d83460 | -9.18334 | -49.99589 | 2026-08-26 04:08:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f203201-32b8-342e-a3ed-6afd417be5bc | -11.27733 | -47.07608 | 2026-08-26 04:08:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8c661335-8efb-39d0-b589-c1a031de0f2c | -7.75801 | -44.76633 | 2026-08-26 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| cf29f6bf-dc2b-39e6-81c2-fe74bd4c3e91 | -8.02891 | -51.81198 | 2026-08-26 04:08:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5a82dd08-1fc2-36cf-b746-ffd897c0438e | -8.01355 | -51.82367 | 2026-08-26 04:08:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c491430a-b710-36e9-ad46-272347df4a02 | -7.04602 | -44.90236 | 2026-08-26 04:08:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e98287c3-5559-3975-91a0-becac8960e68 | -12.69403 | -48.41188 | 2026-08-26 04:08:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 29df1a5d-2fe5-3dd2-bcbf-3f1613fba0a2 | -6.87113 | -43.74413 | 2026-08-26 04:08:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 593c5e43-7e7c-3df7-8bdd-c78840d89a77 | -12.66969 | -48.41765 | 2026-08-26 04:08:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| a6974931-382d-328f-b94f-55480b2ebf71 | -6.91285 | -44.66892 | 2026-08-26 04:08:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8a2a39fb-e399-3a3d-ada4-541e5c03f4e4 | -10.02871 | -46.418 | 2026-08-26 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bfb651fe-137c-3586-9df5-722ad5890515 | -7.76122 | -44.75909 | 2026-08-26 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 88a18953-2ecd-3699-a0e8-3861da1c7f46 | -10.56145 | -50.43851 | 2026-08-26 04:08:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 03a408d0-25d8-37d2-b303-5fcefa9ab7da | -8.07783 | -47.5035 | 2026-08-26 04:08:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 75911ef9-beef-3b2c-9cb7-71376826ea06 | -12.69985 | -45.82943 | 2026-08-26 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6ac64dd8-e5ff-3ceb-ac19-4f68632e2672 | -11.42323 | -44.55245 | 2026-08-26 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7eaeb5b1-cf80-3cae-bd4d-6089ca4bc78d | -10.03472 | -46.40792 | 2026-08-26 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 70752c45-05a2-3405-a94d-5a8c010b406f | -8.75501 | -44.24881 | 2026-08-26 04:08:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 095e8b44-b605-3d93-99db-93bb9f7ad963 | -11.37673 | -45.16023 | 2026-08-26 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1e2fcf5a-d0b8-3b08-b528-9a82e6fa571c | -10.75833 | -54.04297 | 2026-08-26 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 25.6 |
| ffffb758-eb9d-3fee-b1ea-290cb8c0a4c7 | -12.77137 | -44.26216 | 2026-08-26 04:08:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3beed43d-c7d5-3897-a219-30e46eef699a | -12.75366 | -46.47367 | 2026-08-26 04:08:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b3244ada-ea47-3f75-833a-b254aac83eb5 | -6.91192 | -44.66698 | 2026-08-26 04:08:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a5e231c8-68c4-3fda-a6c0-03c22e1b15c6 | -12.68673 | -48.40117 | 2026-08-26 04:08:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 326c1b45-7677-3c3b-b8a4-2bb665007cea | -12.15787 | -50.6006 | 2026-08-26 04:08:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f0837f45-4a4b-33d0-bc8f-6ca896602c44 | -7.75897 | -44.74879 | 2026-08-26 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 31d28c3d-aab9-3ab9-9d99-e6dfbbe0d141 | -12.16094 | -44.84718 | 2026-08-26 04:08:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c64dcbc3-b334-3725-a963-9006ef526c80 | -13.33237 | -48.22101 | 2026-08-26 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d9c582f-eb24-39a3-a614-75d006916f16 | -12.80535 | -42.72906 | 2026-08-26 04:08:00 | NOAA-20 | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| b6bea0eb-23f8-350c-8b48-71648ebfe756 | -13.33066 | -48.23045 | 2026-08-26 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bf2e6a1f-3273-3634-b3aa-bcec84eaa501 | -6.2668 | -53.36587 | 2026-08-26 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d2dd99ad-79c6-3618-a71a-e3e504cd46d8 | -6.8748 | -43.74472 | 2026-08-26 04:08:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bb9b363e-25a9-38a0-a90a-86f8bc76add5 | -8.63293 | -54.75739 | 2026-08-26 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2822d075-b707-3884-a129-7dfaf9651257 | -7.45095 | -43.09242 | 2026-08-26 04:08:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 08ffd13f-e004-3ee7-b230-2cefae723213 | -8.077 | -47.50819 | 2026-08-26 04:08:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19b41fe4-5dbf-3778-b49c-96537b28fc1d | -12.72755 | -48.38125 | 2026-08-26 04:08:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 34b6e889-e557-36fb-acef-b4c7b073d831 | -8.75429 | -44.25309 | 2026-08-26 04:08:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5392b1df-1fec-3c2e-8b02-d463baedf265 | -8.02887 | -51.80889 | 2026-08-26 04:08:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c5505ba-7358-379c-a92a-cdc4bba06520 | -11.48617 | -45.08865 | 2026-08-26 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3f13ff6f-f0cf-3b86-8452-75684a1ec552 | -8.75574 | -44.24449 | 2026-08-26 04:08:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7ac603cc-8b91-3e80-a62a-5926a7b4a4ad | -11.84618 | -47.68006 | 2026-08-26 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 29eec74f-3752-3d31-b7e9-9f9fcae96cf2 | -13.36368 | -48.19782 | 2026-08-26 04:08:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dea03f9c-0a69-3ce3-a4bd-c276afc49b1b | -9.71143 | -49.33374 | 2026-08-26 04:08:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 69aae23b-01d6-3ec0-b7b4-962baf799aaa | -6.26321 | -53.38699 | 2026-08-26 04:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 22ea3113-2c22-335e-9001-43c7b865d152 | -12.68217 | -48.4007 | 2026-08-26 04:08:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 197b876e-7fe0-3e40-a0b3-cd75018f17b0 | -13.42293 | -46.73927 | 2026-08-26 04:08:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7abffe4d-6068-3dbb-baba-f3f7f57fa36d | -12.64224 | -48.40654 | 2026-08-26 04:08:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e09a8a35-e3aa-3786-a510-33c31962ee92 | -10.7596 | -54.0384 | 2026-08-26 04:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 130.8 |
| 5a64c991-84ad-3d47-8f5d-d080fe78eb8a | -6.2676 | -53.3768 | 2026-08-26 04:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| c36ee6d0-2d11-3931-aaae-82121774d1f8 | -6.6595 | -58.498 | 2026-08-26 04:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| f694a6b3-625b-3d51-a2f2-3286cbf7c3ca | -7.5104 | -61.3832 | 2026-08-26 04:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 128.7 |
| 6438be8a-b04a-307a-a7a0-02251d18804e | -8.1482 | -47.5218 | 2026-08-26 04:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 54.9 |
| b2cdf3fc-f15d-3560-8580-4c368ea0fb73 | 1.4734 | -55.9839 | 2026-08-26 04:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| c8b8d336-efd3-35d3-b808-99f1a5ae5b1e | -7.0612 | -59.2358 | 2026-08-26 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 2a49f1cc-b0b6-32e3-85c1-1a27557ac421 | -7.0797 | -59.2157 | 2026-08-26 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| a3cf9f3a-2306-3268-8c49-98bdcf4e17aa | -6.6409 | -58.5181 | 2026-08-26 04:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |
| a2f4c13a-cb7c-31f0-90dd-6b062b1ebcf3 | -6.641 | -58.4987 | 2026-08-26 04:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 116.9 |
| f46d0e8a-f26c-3d38-bf04-9e5058894caf | -7.0613 | -59.2165 | 2026-08-26 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 94383a1b-871a-35a3-b009-be288abf0835 | -8.1484 | -47.4998 | 2026-08-26 04:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 90.8 |
| c9625ea1-6d73-3c41-8bf1-f7cfcf05192a | 1.4734 | -55.9642 | 2026-08-26 04:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 5b73eb8b-165f-3f80-9268-0680a5299968 | -6.6226 | -58.4995 | 2026-08-26 04:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 93a940de-a3a5-392d-8c99-e39f8fcab98a | -8.1296 | -47.5015 | 2026-08-26 04:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 2c014cb9-e8c6-3380-97ce-a4ea2decb555 | -9.6024 | -55.1078 | 2026-08-26 04:10:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 86.7 |
| ab8e7bd2-4083-3bce-94b6-be80ae96cc8e | -10.7598 | -54.0179 | 2026-08-26 04:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 100.3 |
| fc9db972-f13e-327f-8db7-2668c8a7325d | -10.3727 | -45.0537 | 2026-08-26 04:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 58.2 |
| ba9c0246-8ee1-3e69-b645-4423539ff8e3 | -7.5289 | -61.3825 | 2026-08-26 04:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 162.2 |
| c20d84b4-8d1d-3c86-97cf-ec3c85687ee6 | -14.75911 | -48.78772 | 2026-08-26 04:10:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ac06657e-ec3b-3d0c-bf2d-5b555b0f445f | -13.2413 | -51.40695 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 32e76fd6-0f03-3b2e-aff9-87276a1dd137 | -18.21248 | -41.57554 | 2026-08-26 04:10:00 | NOAA-20 | FREI GASPAR | MINAS GERAIS | Brasil | 3126802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b3be8721-74f3-3835-8557-a09f6109ce94 | -13.2473 | -51.52017 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7327b95a-4990-36c8-9da9-801c7c15c78c | -14.28782 | -51.13042 | 2026-08-26 04:10:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6a896ed3-0820-3756-ad0f-476fcfdcce35 | -14.28718 | -51.13367 | 2026-08-26 04:10:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f67f7c1b-103c-3c14-8b22-96c0ec3875fd | -13.60635 | -48.99255 | 2026-08-26 04:10:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README23.md)
