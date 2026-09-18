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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 02acf698-ac1b-3b92-8742-9fa99b98c1a6 | -13.62022 | -48.30886 | 2026-09-18 05:18:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 72812410-13cd-34bf-906f-aa294ba726f1 | -9.53872 | -45.46131 | 2026-09-18 05:18:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8b32c908-7d45-3fea-9076-4f97e355a7b2 | -12.30871 | -50.74331 | 2026-09-18 05:18:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e3d0deae-0054-3d2b-8033-66ad5ce0dd56 | -10.90543 | -53.991 | 2026-09-18 05:18:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a6c197f-71fd-3cd5-8131-5304c82e9a45 | -11.07239 | -48.29781 | 2026-09-18 05:18:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 92b51f4a-2b8d-3997-86b1-62cd3706949a | -13.68568 | -48.59706 | 2026-09-18 05:18:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 99653afe-0704-387e-8b98-30dbf8182446 | -11.06739 | -48.29876 | 2026-09-18 05:18:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 944ca79f-fc83-34b1-b2dc-a260b26718d8 | -8.48912 | -46.88513 | 2026-09-18 05:18:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f68e2c76-dad7-3c30-a62c-e2b5e917caf0 | -10.65189 | -50.23967 | 2026-09-18 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4b435d8e-6c69-3410-bc52-5f8401878fbf | -9.9234 | -46.58091 | 2026-09-18 05:18:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8b6fa537-6bbe-30e1-88ce-5273bd7e694f | -10.66385 | -50.26505 | 2026-09-18 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f9e61816-156b-3bd3-9811-28c37f00c4f0 | -12.39848 | -50.68069 | 2026-09-18 05:18:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8151a790-a829-34ad-8dce-16619615b595 | -10.11683 | -46.29804 | 2026-09-18 05:18:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7560d85e-5daa-3b0e-b785-0597c0b93689 | -12.29307 | -50.74704 | 2026-09-18 05:18:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3a0f6701-42cf-3da8-be2c-778543433256 | -10.83376 | -54.1025 | 2026-09-18 05:18:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 21534de5-5b04-36b2-b025-5d256ed226e7 | -10.94297 | -53.05967 | 2026-09-18 05:18:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 27a8613f-68b6-325d-a4bc-42c078dc0fd7 | -10.51581 | -46.73982 | 2026-09-18 05:18:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 25a674b8-2456-36a7-87ff-24c96d403f97 | -10.51266 | -46.7422 | 2026-09-18 05:18:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4eb35229-f2f7-3b87-a3a8-26db4c295dbd | -12.47855 | -50.69084 | 2026-09-18 05:18:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3b039200-49dc-3ddd-95d2-e592fd3c850b | -11.52362 | -46.8857 | 2026-09-18 05:18:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c889b6c8-cd88-3d63-a235-74df3017209e | -9.93494 | -46.53922 | 2026-09-18 05:18:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7bbdd1d0-ec51-3e1c-9760-9e6ef8809b05 | -10.65498 | -50.25496 | 2026-09-18 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| f48fe11f-3db1-302d-8466-6cf3f48d6e43 | -9.71036 | -47.0949 | 2026-09-18 05:18:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4daeaa50-f498-3662-8fa7-5894efc1c547 | -10.79773 | -46.66409 | 2026-09-18 05:18:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 690ce8a0-6d6d-34db-8ca4-cc4c2cc1e446 | -12.25856 | -47.14336 | 2026-09-18 05:18:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7bb49c79-0792-3089-91c6-0375a6e1ab5e | -10.48369 | -46.31511 | 2026-09-18 05:18:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8a981dec-7813-311c-9850-ead6e85ab03e | -11.31363 | -46.76693 | 2026-09-18 05:18:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 31ed7f70-39fb-3c35-a881-0e41f1b97660 | -8.88644 | -45.88383 | 2026-09-18 05:18:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| be766135-4125-3ecd-b09e-3011526860e1 | -10.6677 | -50.27447 | 2026-09-18 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1c38994d-dbc7-357c-a974-348b51436710 | -11.8052 | -58.17345 | 2026-09-18 05:18:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7c91875b-14e0-3819-9b02-7dedf2a8396b | -11.52424 | -46.88054 | 2026-09-18 05:18:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 90b4bee7-5d21-3bfd-a7b5-db9e9acccc52 | -8.90502 | -45.02133 | 2026-09-18 05:18:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7fb4f63c-df68-320e-8421-8f9ec38039be | -12.16939 | -46.97406 | 2026-09-18 05:18:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b48b0632-3c4e-3bf0-a406-7f5e2ab64720 | -8.90417 | -62.3981 | 2026-09-18 05:18:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e91d83b7-8dc8-3d6b-9eef-7f309c62dd27 | -9.91634 | -46.51002 | 2026-09-18 05:18:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c6f176d0-5ba4-3585-b938-73dc56a533f6 | -9.56664 | -48.43733 | 2026-09-18 05:18:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d825fb01-d9a7-3b0c-9fed-bb3c4daa813d | -10.71389 | -54.01654 | 2026-09-18 05:18:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f62c5ca0-ed77-3215-81d7-de59754818a4 | -11.87584 | -47.5868 | 2026-09-18 05:18:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8dd61a8c-dd9d-35f6-8fb5-d88d3fea1f36 | -12.2675 | -50.74945 | 2026-09-18 05:18:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 7321641f-3648-3790-9c90-e14455715cc9 | -9.68861 | -54.33784 | 2026-09-18 05:18:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3bc783eb-0dfc-3ed6-81f1-73628759fb19 | -9.7104 | -54.81655 | 2026-09-18 05:18:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| c3b30454-361e-387c-b531-f1a0af51c3aa | -7.7521 | -54.74855 | 2026-09-18 05:18:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 61a40001-49b1-3f06-a24a-75349b1df35b | -13.68499 | -48.60041 | 2026-09-18 05:18:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a6404779-ee7d-37ae-a907-9d78d47aba8b | -14.22599 | -48.51451 | 2026-09-18 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 07a55789-ff89-3d67-99d5-9526771b952e | -10.71311 | -54.01951 | 2026-09-18 05:18:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c6c3556b-043d-3f97-9c51-716267fcdfc9 | -9.90929 | -46.56492 | 2026-09-18 05:18:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d6586f7f-12aa-35a8-bdb8-908c4ab6389c | -11.8751 | -47.58361 | 2026-09-18 05:18:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 668214f9-f26a-35ee-bd8b-35a57ede436d | -10.66819 | -50.47021 | 2026-09-18 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 72dd564c-420a-35e7-948c-20c68ce85d71 | -12.55862 | -50.74444 | 2026-09-18 05:18:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0048ee10-c336-327f-91ca-a04a2ee25b54 | -9.84225 | -48.39447 | 2026-09-18 05:18:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6533fefc-0213-3254-9b36-516543559d14 | -12.55149 | -50.71991 | 2026-09-18 05:18:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2096c2d1-8337-3d54-ae4f-e6d138404339 | -10.51954 | -46.73812 | 2026-09-18 05:18:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7e7c3632-512c-3517-8351-c2e156977b15 | -12.20994 | -53.2182 | 2026-09-18 05:18:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 3c167604-d657-3da2-914f-ec0480746e5b | -12.31004 | -54.12611 | 2026-09-18 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9322b24f-cb06-3673-8421-3c51d2f70306 | -8.5626 | -64.05553 | 2026-09-18 05:18:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9267a711-3732-309d-968d-cce103404a8e | -10.67043 | -50.25407 | 2026-09-18 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 305f9714-a380-3451-9cd7-7c5c7ee48b5d | -9.83313 | -49.23386 | 2026-09-18 05:18:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 28e962be-a894-3341-939f-ca29e0b4839f | -10.11372 | -45.65298 | 2026-09-18 05:18:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1787973c-ed6e-30ea-8433-c093b04996f5 | -10.67311 | -50.27222 | 2026-09-18 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 820ddc12-8a12-3db6-a131-9e9f3931c723 | -10.79836 | -46.65897 | 2026-09-18 05:18:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7078980d-c46f-3014-8edc-01de74d0f1bb | -9.75803 | -46.09458 | 2026-09-18 05:18:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c1a824ca-95e4-39ad-b2a6-65757a1ed0f9 | -10.94735 | -54.09004 | 2026-09-18 05:18:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6509d096-455b-329a-9245-2a2591d56d05 | -12.1704 | -46.99509 | 2026-09-18 05:18:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3db563fc-63ad-3e16-bc25-c85e16409515 | -9.83188 | -48.34202 | 2026-09-18 05:18:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1f191f0b-d037-360e-8297-dd04453fa688 | -10.99703 | -57.05998 | 2026-09-18 05:18:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 22a8e3c2-125b-3a49-82c1-7bc8d9cc38ab | -10.66809 | -50.27155 | 2026-09-18 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 96772e1b-f0a9-3bad-ab71-07db07f79238 | -9.72291 | -47.14418 | 2026-09-18 05:18:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0d582ae9-d50d-3e53-ae39-62a705511f7b | -10.12946 | -56.76128 | 2026-09-18 05:18:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df2f66fb-c5ad-33b5-a60a-df4f1584f8bd | -10.66396 | -50.46387 | 2026-09-18 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c8b12384-6f56-3710-953c-3312537e24d1 | -8.77975 | -46.90818 | 2026-09-18 05:18:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a8516b34-27a9-3082-8d75-389a0131cb92 | -9.90969 | -46.53524 | 2026-09-18 05:18:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 57921104-9da4-32e9-a00a-3b0c26c12ab8 | -10.80548 | -50.19933 | 2026-09-18 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 547f8675-be53-3001-bbea-2b8260c0622c | -9.1904 | -46.76729 | 2026-09-18 05:18:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0425254c-7049-30c4-8197-0c730024bddc | -12.55131 | -50.7182 | 2026-09-18 05:18:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f47ccaf2-1df6-3644-8240-7fe4f8ae7512 | -7.49568 | -55.00997 | 2026-09-18 05:18:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7096fd10-2fdb-3da8-a721-8e0619f7c30c | -14.12997 | -48.72809 | 2026-09-18 05:18:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 70ab5f75-c360-3f3d-b49e-fb77d21d2040 | -9.60476 | -55.10228 | 2026-09-18 05:18:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 59b3fdb1-ca08-3f96-9386-0ec3516635a8 | -11.02584 | -54.15194 | 2026-09-18 05:18:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5d0f737-4c26-34f9-a331-48e1e1345e1e | -9.48259 | -54.4822 | 2026-09-18 05:18:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 24c54a1d-ea96-3101-8ae3-af5eedee1e01 | -13.24918 | -46.9111 | 2026-09-18 05:18:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| deb9dbcf-482d-3a95-a946-8c34751e589f | -10.48431 | -46.30997 | 2026-09-18 05:18:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8e7a1aa2-daa1-3579-890a-e4398498010b | -12.62071 | -50.89242 | 2026-09-18 05:18:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a02971a9-48e7-31e4-8cc3-1520445ee14a | -9.94453 | -45.2923 | 2026-09-18 05:18:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7c1346e7-672d-3bf8-8690-6fce1acaa59c | -10.64648 | -50.24191 | 2026-09-18 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 4a174fb8-22fb-339a-96e2-b250b87acca8 | -10.67192 | -50.46886 | 2026-09-18 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4590b8f3-9f05-3922-b46b-d1b67e0d4365 | -11.02262 | -54.15393 | 2026-09-18 05:18:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8b071431-7350-3fe0-9cdb-2037e31d3207 | -9.7514 | -46.09694 | 2026-09-18 05:18:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b7e15fa0-d078-3e4e-832d-57b91f8af519 | -8.90255 | -62.40766 | 2026-09-18 05:18:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4a66b214-f772-351b-97a4-93d7914c580a | -11.88231 | -47.57512 | 2026-09-18 05:18:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 86d1263c-f05c-3866-b33c-f9482604acc5 | -9.75869 | -46.08939 | 2026-09-18 05:18:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 08ea1502-899e-3779-85cd-399f3352c953 | -9.75073 | -46.10008 | 2026-09-18 05:18:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1bd67065-93a6-38a7-ba21-ee6559c164ea | -9.95187 | -46.60999 | 2026-09-18 05:18:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d5afe490-72d7-3165-aad8-e0ae6349b1f0 | -8.11903 | -54.81301 | 2026-09-18 05:18:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c5aab9f-a2c4-31c7-8868-cedfad9feeb1 | -10.64686 | -50.23899 | 2026-09-18 05:18:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| ed554a2f-c762-3a73-9fca-7e44c4c8e521 | -12.39104 | -48.47474 | 2026-09-18 05:18:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b0cb9765-1313-3a7c-ac4b-e7df2d3749d8 | -12.46211 | -50.70045 | 2026-09-18 05:18:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b677e2c1-9f36-32c0-b34d-5fa6e28e582b | -12.65693 | -54.71964 | 2026-09-18 05:18:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c064bcb1-212f-33dd-953b-bdce303b907b | -13.74495 | -48.79406 | 2026-09-18 05:18:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6f267e78-464a-3a06-8e3a-c660d40b7cd0 | -8.50958 | -48.49774 | 2026-09-18 05:18:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e6aec2e2-e617-323c-a579-7aca9198abc9 | -9.71683 | -47.14334 | 2026-09-18 05:18:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README86.md)
