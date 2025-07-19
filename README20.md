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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 111af142-8e7f-354c-861c-611add989471 | -7.0374 | -43.88425 | 2025-07-19 04:34:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2650c7df-df7f-30bd-8b44-1fb791df4b72 | -7.95774 | -43.94405 | 2025-07-19 04:34:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 16b181ec-2e2c-31ea-ae81-045c216ae8f3 | -6.75338 | -44.76418 | 2025-07-19 04:34:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b99d8123-1e06-3533-8659-b6e3adaa18a3 | -8.41517 | -46.87506 | 2025-07-19 04:34:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8b3bc9a2-5108-3f2e-8a95-d93fbcca25fe | -4.819 | -47.3168 | 2025-07-19 04:34:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d384e0f1-8401-3252-b397-24347f2690b0 | -5.53098 | -43.88585 | 2025-07-19 04:34:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a27a31d8-495d-300e-9543-067b023b2d42 | -3.10844 | -47.49352 | 2025-07-19 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3f008c78-6225-39ed-9311-047836ba0aa3 | -2.44507 | -47.32538 | 2025-07-19 04:34:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 98d5cbab-462d-3bdd-bf47-e1bdd9a8afb0 | -8.0689 | -50.07898 | 2025-07-19 04:34:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5daaace6-17cd-3fd2-bfcc-efa5c35c5498 | -14.70133 | -45.06848 | 2025-07-19 04:36:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c2871834-1124-3993-9be7-448e51644d32 | -8.25628 | -55.17986 | 2025-07-19 04:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6a6308d8-67a2-3e35-8e7d-faf8d291d856 | -15.1581 | -46.18413 | 2025-07-19 04:36:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ef4ecf0-48f1-3d61-8f7d-d1ed130d6c41 | -9.76347 | -48.74968 | 2025-07-19 04:36:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2d038666-b6f3-3f73-b579-c006f7c204ce | -12.99398 | -46.93962 | 2025-07-19 04:36:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d0d967cf-d17a-3223-b18c-ea68d84640f7 | -11.95696 | -47.01981 | 2025-07-19 04:36:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 338d6c84-de68-3236-9f1c-68a6486b8e60 | -12.36046 | -50.33699 | 2025-07-19 04:36:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0092b24a-8afd-31b0-a6e9-6a3fd5df8ac8 | -9.81043 | -48.56015 | 2025-07-19 04:36:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1949f538-f67b-36ea-8926-ccfd83a6a89f | -14.6974 | -45.06786 | 2025-07-19 04:36:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 74600c37-e916-343f-ba08-5ef824657d21 | -9.80656 | -48.56312 | 2025-07-19 04:36:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ef98fb11-6fcc-37e2-b708-50ddbd14368e | -11.46254 | -48.15846 | 2025-07-19 04:36:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f8895851-c515-3481-9731-8cde707ad677 | -15.50283 | -47.83942 | 2025-07-19 04:36:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8e8ef374-a9dd-34d2-a456-17a9b1ed3020 | -11.7351 | -48.19439 | 2025-07-19 04:36:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 36.2 |
| ac6125d6-705f-3921-b2cc-8dcf22c7c4ba | -10.63768 | -44.76329 | 2025-07-19 04:36:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bd57180a-3dfe-3c82-96b8-1a0577e9966a | -15.92193 | -43.51351 | 2025-07-19 04:36:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 26d15495-54cc-322a-8f76-c49b5fcd1d3b | -10.9853 | -49.39024 | 2025-07-19 04:36:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 48c75581-ccbd-398d-80bd-02d5ca492e86 | -11.65619 | -47.87355 | 2025-07-19 04:36:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| fdf6df75-b066-3b6b-b541-261478dc7d5d | -12.36835 | -50.33088 | 2025-07-19 04:36:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fdc0ccc1-ff05-3be6-9a79-429c1fcb08f7 | -15.50972 | -47.84057 | 2025-07-19 04:36:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 942d7d5b-a2e9-3cae-8fe4-385da7df31fe | -12.37506 | -50.33201 | 2025-07-19 04:36:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 27f91189-8789-3283-93bc-5fc121e8054f | -10.68208 | -49.67475 | 2025-07-19 04:36:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 39f22953-22f4-317a-98a0-9a54e66f1db4 | -11.95984 | -47.02416 | 2025-07-19 04:36:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7653bd3b-8a95-3349-ad61-62ba5d3c9e18 | -12.06488 | -47.34547 | 2025-07-19 04:36:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 150098fe-ee8b-3473-a471-5b09552a8c63 | -9.39956 | -48.39768 | 2025-07-19 04:36:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 15095985-7c2a-3ad1-b40e-34ccec7c9967 | -10.36616 | -57.50898 | 2025-07-19 04:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 523060cc-94d0-3e35-a236-347d2ca56871 | -14.47849 | -46.36017 | 2025-07-19 04:36:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2e5dbadb-621b-323d-89a1-d94b1b54193f | -14.71758 | -48.24433 | 2025-07-19 04:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 197911c5-b2a9-331c-bb66-47db569d8217 | -16.04203 | -43.72041 | 2025-07-19 04:36:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5b3d9935-95fc-30af-ba20-e5046566b4cd | -12.42467 | -45.37115 | 2025-07-19 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9ed060c8-28e6-3ad5-929a-3bdb909b3d23 | -11.48886 | -47.32713 | 2025-07-19 04:36:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 9ca8d28a-77a5-38f2-8fda-0c84d7051923 | -10.66699 | -49.68323 | 2025-07-19 04:36:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dbef8b64-67e9-3217-8074-6607add887a7 | -12.99001 | -46.9184 | 2025-07-19 04:36:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd3f2af9-ea54-388f-bc7b-0fd1a0d70ec9 | -10.02872 | -46.30826 | 2025-07-19 04:36:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a06031bd-4e3f-301e-af45-433f372cb56a | -11.47524 | -47.32502 | 2025-07-19 04:36:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f7117501-0bc7-341a-bda2-b5f2439a13a0 | -9.80269 | -48.56609 | 2025-07-19 04:36:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db5f4954-5085-3321-a882-01ceaf65f9c3 | -9.95304 | -48.16654 | 2025-07-19 04:36:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 22d87938-4387-3457-b97d-173f4dc238c9 | -11.70588 | -50.259 | 2025-07-19 04:36:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b1464d73-6b41-3b37-b50c-a1ce1cea1851 | -10.08923 | -47.24164 | 2025-07-19 04:36:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f50e5025-3549-311b-9003-434cf36052e8 | -11.48546 | -47.32661 | 2025-07-19 04:36:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 03bd2471-f1c6-3f44-8cfc-4ae2321f9bab | -9.43323 | -48.84682 | 2025-07-19 04:36:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 29cd9c3e-fbe3-3c0d-bc91-5fe13e2d528b | -9.81612 | -47.74382 | 2025-07-19 04:36:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b25251e5-c303-393a-b437-a6a13b423a8f | -10.6225 | -44.76854 | 2025-07-19 04:36:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| eca34adc-70a5-347a-878e-508bc27bf5d6 | -9.80988 | -48.56365 | 2025-07-19 04:36:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| dbbd54a5-baa8-3346-afb1-432561bbd6bf | -9.76402 | -48.74619 | 2025-07-19 04:36:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dc9c560e-6da1-3deb-8d86-6ed9077e3ddf | -12.90348 | -48.91996 | 2025-07-19 04:36:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5958fd14-3efd-32e4-88ec-830afc693603 | -14.83968 | -49.12637 | 2025-07-19 04:36:00 | NPP-375D | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7b769e43-b698-30a7-ab76-60e90efa61a2 | -12.08844 | -44.73276 | 2025-07-19 04:36:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ce5c2e6-7d26-3e27-84c2-2a657c48158c | -12.57129 | -44.75603 | 2025-07-19 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1f30d140-36e0-3f55-a821-2a4d629a1bc7 | -9.37789 | -47.95329 | 2025-07-19 04:36:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b1f5a173-df01-3467-bcab-5a3a64481467 | -11.739 | -48.19135 | 2025-07-19 04:36:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5085e466-be73-362e-8fcd-090d3df4182e | -9.83573 | -48.37781 | 2025-07-19 04:36:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0de94f0b-a5f2-3f2f-aa93-ba45644ee60a | -11.36957 | -54.34362 | 2025-07-19 04:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9a3d7ecf-1147-32db-92b0-8e5dbcd0484b | -13.60458 | -45.64263 | 2025-07-19 04:36:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 52a80d13-ca71-3888-ab29-a8fb3a0f0609 | -12.95735 | -46.92158 | 2025-07-19 04:36:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f2808709-43f5-35a2-b44d-75f6e301aa80 | -10.57051 | -49.12415 | 2025-07-19 04:36:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3e61892f-d40c-36ad-adba-ffd3adbaab8a | -14.48213 | -46.36073 | 2025-07-19 04:36:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 618c3276-8b4e-39a5-b7cf-429e755d10bd | -12.03627 | -48.75499 | 2025-07-19 04:36:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b61e5694-b938-3f9d-943b-50d5a5a38a26 | -14.74923 | -48.2644 | 2025-07-19 04:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0969d473-065e-3fff-8a91-e00109234eb6 | -11.56224 | -47.09752 | 2025-07-19 04:36:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5f429939-6085-3318-a7c4-ca3b53bd5497 | -10.6187 | -44.76797 | 2025-07-19 04:36:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f585a776-054d-308e-92a3-600edebfeeaa | -12.67915 | -46.83202 | 2025-07-19 04:36:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6cce2575-ba8d-369b-902b-c44716640069 | -12.38521 | -50.34077 | 2025-07-19 04:36:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e2ed05c2-9f1c-3f42-b79d-f169eed6b4a7 | -12.9649 | -46.91888 | 2025-07-19 04:36:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 10e3a4f1-d8f5-38fd-aec9-aca95959e2e4 | -12.09231 | -44.73335 | 2025-07-19 04:36:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf4e32a8-8711-3f7c-8cda-2cbe38792adc | -16.04229 | -43.72272 | 2025-07-19 04:36:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 83512467-b8ad-3546-9ce8-6a99d3e2eb76 | -11.73621 | -48.18724 | 2025-07-19 04:36:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6a9d281c-36ec-384e-8799-38d10c00d696 | -14.78 | -48.29544 | 2025-07-19 04:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 711b3335-a253-33b2-add8-53341fcd5fc7 | -12.99805 | -46.93628 | 2025-07-19 04:36:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3167cbbd-fa5d-3562-81a0-849b6da35bd8 | -13.05253 | -49.17615 | 2025-07-19 04:36:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ce9627a1-73ba-34b9-8fe8-e36068dfd2e4 | -12.42907 | -45.36712 | 2025-07-19 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 24534402-0586-3f36-b882-fbb436e52e33 | -11.73232 | -48.19028 | 2025-07-19 04:36:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 36.2 |
| ddd1d4f8-6f69-3787-b835-b82e786abde4 | -9.79937 | -48.56555 | 2025-07-19 04:36:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 518a4229-78d9-3bd1-8216-447a60bbddcd | -10.76134 | -52.76084 | 2025-07-19 04:36:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2d835839-9966-34dd-baa2-30ab33d5c708 | -10.09655 | -47.23906 | 2025-07-19 04:36:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c8e63c2d-4ca8-3f7a-ada6-7df3232c8c5b | -10.181 | -49.50581 | 2025-07-19 04:36:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5e428db7-1bfe-36f3-962a-83d434fc0b6e | -11.56512 | -47.07857 | 2025-07-19 04:36:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 47264dd3-b6e5-3679-bd25-90acd0f9c6e4 | -11.73287 | -48.1867 | 2025-07-19 04:36:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 05bd0715-25e0-31db-abc1-e6a1295e063d | -14.50205 | -43.69344 | 2025-07-19 04:36:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81dda276-bbff-3df8-aae7-137eca8123db | -11.73062 | -48.52484 | 2025-07-19 04:36:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 37cb71b0-897d-343e-8275-e69aa7863577 | -10.81868 | -49.2836 | 2025-07-19 04:36:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| db51347a-ce84-35d5-88bf-500686c48eb2 | -11.47239 | -47.32077 | 2025-07-19 04:36:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 208cba3e-f6c0-348a-b198-cb1015c14106 | -10.37897 | -49.90106 | 2025-07-19 04:36:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 088e9bfd-cfa9-3a69-aace-8f476fe39333 | -11.83092 | -48.20958 | 2025-07-19 04:36:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 277fbb06-1716-362d-8181-83edf9993f6a | -10.42091 | -48.61462 | 2025-07-19 04:36:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e067dcfb-415f-348a-81a3-8a9b773f6cc1 | -11.72897 | -48.18974 | 2025-07-19 04:36:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 23.4 |
| ec4b6f9a-97ae-3bdb-889f-89a664b071a2 | -12.42841 | -45.37172 | 2025-07-19 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d143d960-8577-3140-8a6c-245ff5b50029 | -9.39509 | -47.9524 | 2025-07-19 04:36:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| be8a5a63-fbb9-329c-bbdc-de0c19075e6a | -12.99746 | -46.94022 | 2025-07-19 04:36:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 142e9c36-dca1-3529-912e-d10838519ba6 | -9.92268 | -46.2969 | 2025-07-19 04:36:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7457e980-d98b-3ef8-b165-1ed825e33c1c | -9.81098 | -48.55666 | 2025-07-19 04:36:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a0ad3165-f45a-356e-a564-f091745fcb45 | -11.88946 | -55.44485 | 2025-07-19 04:36:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README21.md)
