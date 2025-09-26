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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0f4ca044-1a7d-3a26-a4b1-4273d5626c59 | -3.80447 | -47.59099 | 2025-09-26 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0a9d3afa-bdc3-33b0-8f34-0706b6a73eab | -5.22258 | -44.49202 | 2025-09-26 04:14:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7ce0fc81-7fbb-36ac-b215-81da8ef02984 | -10.39469 | -46.13771 | 2025-09-26 04:14:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 847d78ca-08a6-3df2-bb74-369c1db546f0 | -7.64279 | -45.98935 | 2025-09-26 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d4e90a84-111b-3f8c-829e-f8d5f17ff44a | -9.80463 | -45.72484 | 2025-09-26 04:14:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d10b2d57-17a2-384b-94ed-1441457705b4 | -5.64228 | -43.92902 | 2025-09-26 04:14:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 36af4371-2bd6-38ea-bfe5-02d55368e6df | -3.05742 | -48.71063 | 2025-09-26 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d3211f9c-07e9-390c-80b7-9b98e7b39532 | -4.25551 | -48.59792 | 2025-09-26 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31e9e2cd-14f2-3e87-99b6-ccbac9df7b37 | -8.83717 | -46.26564 | 2025-09-26 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 6368d355-d5ad-3ee0-beca-9682c7f63fd3 | -6.82705 | -44.16457 | 2025-09-26 04:14:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1372b2c2-b185-3c89-b572-bc1b5ebae84c | -10.4059 | -46.15511 | 2025-09-26 04:14:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 06f35566-6fe8-3f44-a160-ef0fe55a8e9a | -5.75131 | -44.96458 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 7aa89990-7264-3930-8314-085ca8e76394 | -6.11955 | -44.22475 | 2025-09-26 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 084a1b5a-ffbb-3b6f-a964-614d4cf4b67c | -5.47062 | -43.07203 | 2025-09-26 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e0076802-a20d-3c08-8865-4f47baad239d | -7.27213 | -42.97938 | 2025-09-26 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 752c8cfa-e7c0-3e9a-9b31-1cd4d20897ce | -10.938 | -44.29723 | 2025-09-26 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5ad0ab9a-cf1c-34ae-806d-861e07e12baa | -5.73013 | -44.98788 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 118ec011-0def-3b16-86de-1dda4ae5d8b1 | -5.74155 | -44.98206 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d7c6af9f-b445-303c-a736-dd36a1dd5f93 | -5.21318 | -39.85402 | 2025-09-26 04:14:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 25897081-6c87-33fc-96f3-9f0e8a688a14 | -6.2588 | -42.49364 | 2025-09-26 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 99139ddd-c850-3d82-b905-ca3572004679 | -5.42991 | -41.32177 | 2025-09-26 04:14:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 07d8270f-209b-38db-b1f9-b7c476c9fe66 | -7.3806 | -44.45126 | 2025-09-26 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 272b4fed-8235-325f-ae12-2977551e86ae | -5.73316 | -42.63432 | 2025-09-26 04:14:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 1ac369a8-d6e1-31d8-96fd-fe3f552aa3b8 | -7.68092 | -46.00672 | 2025-09-26 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b85a1820-efd3-3a20-a201-031c09005881 | -9.70654 | -48.25084 | 2025-09-26 04:14:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5e7132ca-a8d9-3e3b-82d3-c81acb2cdeea | -6.87879 | -44.50467 | 2025-09-26 04:14:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| cdc80195-c885-3827-8df9-46b9f0413f75 | -10.92864 | -44.29216 | 2025-09-26 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3f611aef-7985-3219-8485-f8d3f769dd76 | -4.80189 | -43.04023 | 2025-09-26 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| c663b059-daf9-324a-8b89-fcc587835c5d | -5.78025 | -42.81453 | 2025-09-26 04:14:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0d04bd37-ef32-31bb-8426-26ce4ddc5df4 | -4.79569 | -42.82115 | 2025-09-26 04:14:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c6bf5812-974e-335e-b393-875f310667f8 | -10.57022 | -44.08063 | 2025-09-26 04:14:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a42b9191-c2d5-3a98-86a8-2b522c4f39f3 | -6.42668 | -43.07528 | 2025-09-26 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 90159fbf-7b14-36ea-af9b-208fdff4cd72 | -6.96254 | -43.23819 | 2025-09-26 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| acc657a5-cc07-314a-bc6e-bc6b322d5520 | -5.83268 | -43.90926 | 2025-09-26 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c93a8f43-1def-37d6-8d09-7050003c7757 | -9.76127 | -49.31548 | 2025-09-26 04:14:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e989ceda-c410-32c0-a4c0-d6f384f1c2b1 | -5.93065 | -42.91613 | 2025-09-26 04:14:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c3ce0c18-5f6c-327e-b100-119713e91ff6 | -10.0148 | -44.1728 | 2025-09-26 04:14:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd4a7ab7-804a-38ba-bdbe-4ef21712dfdf | -5.46786 | -43.06808 | 2025-09-26 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 912d1f1c-22d1-3abd-bc73-36610e0888c9 | -5.37314 | -36.81252 | 2025-09-26 04:14:00 | NOAA-21 | ALTO DO RODRIGUES | RIO GRANDE DO NORTE | Brasil | 2400703 | 24 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 97c61497-7c4f-3687-94c8-512432b224ed | -5.73755 | -44.98524 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 49edda28-c4c2-317c-81cf-d52fcb72e8d9 | -5.79015 | -42.81609 | 2025-09-26 04:14:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d1c498a3-4a90-31a7-b9ff-0abaaf6aaa7e | -10.57406 | -44.07767 | 2025-09-26 04:14:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bba1b9bb-603c-3da6-a2ff-46d921a12505 | -5.42879 | -45.13627 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d24f486a-d4a8-30b5-900d-11a3594fa0b0 | -4.79623 | -42.81771 | 2025-09-26 04:14:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 590e2906-46fa-30d2-b1fc-9ed9e4d51ebb | -10.58744 | -44.0619 | 2025-09-26 04:14:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c73cc928-0a6c-3979-af9c-cd3f91884fcc | -8.67047 | -44.0242 | 2025-09-26 04:14:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fee27c73-760f-3930-9f45-31d2b3452457 | -7.66824 | -45.9967 | 2025-09-26 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a2285725-d1e6-3e63-aad6-edaa238a6639 | -6.47569 | -41.90085 | 2025-09-26 04:14:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f3a1ffec-2838-32de-b177-9278b39b5677 | -9.9862 | -49.24976 | 2025-09-26 04:14:00 | NOAA-21 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7703b1ad-99be-3ee2-bd60-bc70c0c2788f | -6.13574 | -44.87034 | 2025-09-26 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d9ca81f4-ed30-3af8-8424-e7231f07754f | -4.74972 | -43.26474 | 2025-09-26 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 969d5bfe-ff48-3811-bda4-de2e68d561db | -8.51173 | -44.61818 | 2025-09-26 04:14:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 701ecc6a-16b1-302a-af3f-b064dfb84915 | -10.57131 | -44.07366 | 2025-09-26 04:14:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f30a138f-b78f-3cca-8557-3961efb6e103 | -8.19161 | -46.39095 | 2025-09-26 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 51f5b496-c84f-32cc-997b-2ad1d4b162fb | -3.45274 | -44.12979 | 2025-09-26 04:14:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d390a0c2-8f0c-3202-8749-ea7bdbfaac63 | -7.31972 | -45.76759 | 2025-09-26 04:14:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 62906f28-7be2-34c6-9056-d70a801c42ae | -5.82163 | -43.8718 | 2025-09-26 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3ab8986f-3e16-38c0-9529-5ba111fb393b | -4.2573 | -46.24632 | 2025-09-26 04:14:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f7dcd47-c774-35ac-9bf8-31e4567681a5 | -3.80101 | -47.58686 | 2025-09-26 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1ceb9bb0-252d-3ba1-b677-ce45620358a3 | -9.61779 | -48.60229 | 2025-09-26 04:14:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7cb9037a-46cc-3673-95f1-5e5c6bf4fc28 | -6.85381 | -41.49221 | 2025-09-26 04:14:00 | NOAA-21 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 11f329f2-9645-34ee-91bd-bb9bd433f48d | -5.30379 | -42.76781 | 2025-09-26 04:14:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 108079aa-a4b1-3c6e-88de-ce6a08082119 | -5.63952 | -43.92499 | 2025-09-26 04:14:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 7dfdb9fb-aeda-3a6e-9647-a8ac6cd4e578 | -5.3932 | -45.84853 | 2025-09-26 04:14:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4a9de7d5-e69e-385d-b2d9-2368e7e9bd28 | -5.31357 | -43.14257 | 2025-09-26 04:14:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 348d26b2-682a-35fa-95d6-14765341098d | -5.78792 | -43.32671 | 2025-09-26 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 3f711e10-cdc7-3f80-9f2e-0a929342928f | -5.77642 | -42.81747 | 2025-09-26 04:14:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 99445a26-5311-3c1f-a8b8-a75c48bd3404 | -6.2195 | -42.85587 | 2025-09-26 04:14:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1d31ceb8-2e48-3ffe-9958-9fb50a53cac5 | -5.31411 | -43.13913 | 2025-09-26 04:14:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ec0a16cb-42e7-37ca-adc3-c0b173448023 | -9.20637 | -48.86499 | 2025-09-26 04:14:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7875f8ed-bf2e-3f8d-926b-d72f9357a6c7 | -5.7083 | -43.0746 | 2025-09-26 04:14:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 86f21c2f-3710-3d28-a564-eccc3243ec72 | -6.49007 | -43.27943 | 2025-09-26 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0d928aad-77de-3fcb-bda0-ad9e4e3d9e66 | -7.1828 | -42.23487 | 2025-09-26 04:14:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3871b153-1340-32d7-8e37-5cc1ceba9f7c | -4.75302 | -43.26526 | 2025-09-26 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0d10919c-c045-3616-9cef-14d73af21bce | -9.44388 | -40.37907 | 2025-09-26 04:14:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a05d58e7-185e-3bda-b708-16f87fc2d221 | -6.4292 | -43.55946 | 2025-09-26 04:14:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d62cc734-09e2-3b7a-ba9c-81e91a583042 | -10.11408 | -45.30788 | 2025-09-26 04:14:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 206eb605-b8df-3431-97ae-18b105b0705e | -4.81793 | -42.7437 | 2025-09-26 04:14:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 7e15d3f3-ecfa-30c5-8257-c96f5ee5e4ef | -5.24388 | -43.0859 | 2025-09-26 04:14:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 33180942-8d19-3f51-992a-6a4ec7e70083 | -8.08412 | -55.22486 | 2025-09-26 04:14:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dffd00d9-be5b-3061-9e3d-92e084e1c9aa | -9.98152 | -49.25266 | 2025-09-26 04:14:00 | NOAA-21 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7d40f1a3-eb6b-36ad-9633-100512ab4b06 | -9.87229 | -45.91455 | 2025-09-26 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7df7dbe0-4dab-30cf-a3ca-a584cfc04f9d | -3.45331 | -44.12618 | 2025-09-26 04:14:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc9771f0-fe3e-3cb9-a2fb-2b7d89bc7dcc | -6.93502 | -44.64143 | 2025-09-26 04:14:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a4c120ff-bd28-37d9-93c0-d426368064d0 | -7.30743 | -43.81661 | 2025-09-26 04:14:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 646ceb5c-9dd9-33e3-adf3-d0dd6daccfbd | -7.11461 | -39.40825 | 2025-09-26 04:14:00 | NOAA-21 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 46776311-e0de-3f05-9619-f564b6cf087a | -10.00986 | -44.18271 | 2025-09-26 04:14:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f878ed4b-12a2-395e-9f7b-7f9d109fe7bc | -10.25389 | -44.9659 | 2025-09-26 04:14:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c4955a6b-c067-3969-8d4b-31a6e0be4b81 | -5.73235 | -44.99593 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6d20076f-878b-3224-9e7c-5659faea03d9 | -6.26307 | -48.05755 | 2025-09-26 04:14:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dca7d894-d0bd-3c20-8090-637d439c9b15 | -7.77747 | -47.39542 | 2025-09-26 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b532852f-372b-3bb2-9209-18e274efae7a | -5.7648 | -42.5614 | 2025-09-26 04:14:00 | NOAA-21 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| dcc0bd88-b39e-35b8-b2bf-96917c0c2190 | -6.34621 | -43.352 | 2025-09-26 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 840b13f8-2144-3756-9c43-2c10a1f4d0ce | -5.63288 | -43.92393 | 2025-09-26 04:14:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9bb160e9-33b9-30af-a4da-fef80c32de2a | -5.37087 | -42.29419 | 2025-09-26 04:14:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f9c22c43-ee8d-3802-869f-f407ec01c794 | -9.86244 | -45.93199 | 2025-09-26 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 21f03b09-7947-3412-98f9-70211e044060 | -8.71337 | -50.05195 | 2025-09-26 04:14:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 02248472-e52c-313b-95f7-a3583f9ac2a3 | -8.16507 | -46.35404 | 2025-09-26 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f1e5fc3d-c6a4-3abf-a624-e262e073d8f2 | -5.79345 | -42.8166 | 2025-09-26 04:14:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5801fe74-b4be-3535-9974-eb337a921bc5 | -9.42972 | -45.58435 | 2025-09-26 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README15.md)
