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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5ddaf0b0-a998-3f89-8442-3a2257136dca | -4.37633 | -45.62869 | 2024-11-16 04:01:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5f68bdd-db86-3e0a-b68c-d381c7ed83b9 | -4.00441 | -44.33548 | 2024-11-16 04:01:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 447fe2f1-022f-395a-b3aa-425295953eb3 | -4.37468 | -40.74449 | 2024-11-16 04:01:00 | NOAA-21 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 51d883f3-a9fb-3525-afbd-c6fe74f92082 | -1.36202 | -47.17234 | 2024-11-16 04:01:00 | NOAA-21 | CAPANEMA | PARÁ | Brasil | 1502202 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7016432-25f3-379d-9513-93b1de56fdf0 | -3.41288 | -42.38505 | 2024-11-16 04:01:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 8dac7fd1-be4a-32f0-986b-0018cb7db1ed | -5.34996 | -37.35906 | 2024-11-16 04:01:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ea999453-efa3-3448-a0a8-47f45df67554 | -4.34484 | -43.8021 | 2024-11-16 04:01:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 03369e86-ca92-34aa-b22e-57750967e414 | -2.29079 | -46.45659 | 2024-11-16 04:01:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6b3a07b0-39ea-3d9c-ac1b-4abf414e0f17 | -1.70856 | -46.15975 | 2024-11-16 04:01:00 | NOAA-21 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5e149ae9-d198-35fe-8aa9-8f03258711f3 | -6.04252 | -44.03843 | 2024-11-16 04:01:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7e58b398-6683-3c77-8650-1598728e5e6f | -3.29904 | -44.17054 | 2024-11-16 04:01:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8fcc2b57-681f-3463-80ad-5d1199121698 | -4.21559 | -47.22146 | 2024-11-16 04:01:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 41863309-6b1b-314b-a427-ac2b8bfb09ce | -7.18044 | -39.1307 | 2024-11-16 04:01:00 | NOAA-21 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 901ce432-cb80-39d0-8870-698de2aee5c0 | -2.54962 | -46.88989 | 2024-11-16 04:01:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 86907589-bae2-3adf-967c-9dc9992e898a | -2.29533 | -48.18615 | 2024-11-16 04:01:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 30cb747d-0325-37db-8246-2eb94b18fec8 | -2.47826 | -46.37109 | 2024-11-16 04:01:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b082d57c-2e03-3ee8-acde-3256bbb9c315 | -4.95493 | -44.7265 | 2024-11-16 04:01:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c77db7ea-5c50-3fa0-a878-1a53a40ebffd | -5.8726 | -40.17689 | 2024-11-16 04:01:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f846c964-7cf4-3c2e-9865-2b812690fe54 | -6.97896 | -38.47514 | 2024-11-16 04:01:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d912d31d-0f8a-3aac-8c28-63a908c35c78 | -4.40114 | -43.81577 | 2024-11-16 04:01:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 08090762-d6e6-3063-804b-29a77afaaca5 | -3.0737 | -48.01521 | 2024-11-16 04:01:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d221feb4-e23d-3631-b2ef-fc13db158690 | -6.02622 | -48.03133 | 2024-11-16 04:01:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| a1847ec2-31c8-3388-9d00-d93108348cb1 | -2.88535 | -40.39297 | 2024-11-16 04:01:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 63b874cc-065d-327a-a07a-b60c125f72f7 | -3.23715 | -41.38267 | 2024-11-16 04:01:00 | NOAA-21 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| d23e5364-a1b6-3f63-8a1f-eb60931d98b5 | -7.5589 | -35.23125 | 2024-11-16 04:01:00 | NOAA-21 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 6be30d1c-4266-318e-bcb4-8d5031b1caa0 | -3.27089 | -45.49857 | 2024-11-16 04:01:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 94ddbb04-5693-3711-8817-8800eb243082 | -4.37271 | -45.62405 | 2024-11-16 04:01:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 42a65f56-c720-3d49-b148-8ea5827a93fb | -4.21645 | -47.21633 | 2024-11-16 04:01:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0562af2e-544c-365a-9a37-6f6610f683cd | -2.35562 | -49.12179 | 2024-11-16 04:01:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 644349f8-e732-3aa9-83cc-7d5c2f1be618 | -2.20184 | -48.81098 | 2024-11-16 04:01:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 42d986cd-e233-3a5a-888f-ec47c536673a | -3.2474 | -47.9044 | 2024-11-16 04:01:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 66b56909-0646-3800-9c3c-bfb838cfe5e3 | -3.94329 | -46.70749 | 2024-11-16 04:01:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ac30cd5-0f99-3bb9-b840-7e17f8ba7bec | -4.99731 | -44.3221 | 2024-11-16 04:01:00 | NOAA-21 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 08b81969-c543-3530-a83e-974603485454 | -2.63061 | -46.18947 | 2024-11-16 04:01:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c1669b4e-7f05-3da8-85e3-6536f9eff45e | -2.92249 | -40.30906 | 2024-11-16 04:01:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 50373065-32f7-3fba-9a73-80a654bb1b6b | -4.85306 | -42.47421 | 2024-11-16 04:01:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| e4f358c5-bfaf-3b61-9602-d230212edad8 | -2.65269 | -46.19781 | 2024-11-16 04:01:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c4ce414-a0b2-3fac-ae7b-992d5cc18a15 | -3.2469 | -47.90742 | 2024-11-16 04:01:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d8defb28-7293-39a5-8c27-faa266476cce | -6.94735 | -40.02132 | 2024-11-16 04:01:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 189f29fc-d694-3b2b-8363-87e912287196 | -3.28177 | -46.21083 | 2024-11-16 04:01:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9e30c77a-d965-3e4c-8b63-1dabf8afc60c | -3.68626 | -40.77774 | 2024-11-16 04:01:00 | NOAA-21 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 03a749cc-a8d0-3203-b56a-1f0946e3c838 | -4.09618 | -49.97644 | 2024-11-16 04:01:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9212adaf-6ebb-36f0-8268-8d87bccba253 | -1.99639 | -46.57879 | 2024-11-16 04:01:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 98610f65-a5ad-3586-b3de-ec982f2574e9 | -5.15638 | -47.93687 | 2024-11-16 04:01:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 160c7fbd-6c45-3222-a7cf-6290f9e91bab | -2.63891 | -45.97062 | 2024-11-16 04:01:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 70aa1e39-b248-3670-9c7b-abfd9d04865f | -2.09683 | -46.58898 | 2024-11-16 04:01:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cbcd7456-f04f-386e-b2a4-cb2e984a3e47 | -5.00201 | -44.31781 | 2024-11-16 04:01:00 | NOAA-21 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 71c6dcff-7988-33ff-bba4-ef8a7af6e2b9 | -6.3066 | -39.48418 | 2024-11-16 04:01:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 0d9ded8b-07e7-37f9-9628-329ee2707287 | -2.77863 | -48.58295 | 2024-11-16 04:01:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 3335d913-2021-3842-91dd-12a3c48edbfb | -7.34542 | -34.89201 | 2024-11-16 04:01:00 | NOAA-21 | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ef486fd0-160e-3cc8-b595-073ebe1acff5 | -2.66559 | -46.17609 | 2024-11-16 04:01:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dfe154d1-d217-3b4a-89aa-45c032c05982 | -7.45505 | -38.41305 | 2024-11-16 04:01:00 | NOAA-21 | IBIARA | PARAÍBA | Brasil | 2506608 | 25 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 92608e9c-20de-3a95-8108-b7e10ee8fae5 | -4.22242 | -50.67644 | 2024-11-16 04:01:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 82b51db0-c0db-324c-878d-ad1ba9850adc | -2.61332 | -46.17812 | 2024-11-16 04:01:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dcd52d30-ac57-3de9-8118-0e03400eb38d | -5.21692 | -43.78984 | 2024-11-16 04:01:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 72f75f00-aa77-3696-88cd-459694cd5e6c | -6.98955 | -39.66225 | 2024-11-16 04:01:00 | NOAA-21 | ALTANEIRA | CEARÁ | Brasil | 2300606 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9099e5bb-115a-3fcc-8dab-d440a17fbe6e | -3.73294 | -45.66493 | 2024-11-16 04:01:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e4c48fc6-b01f-3b2b-83aa-edb839cc9e84 | -5.78581 | -41.09635 | 2024-11-16 04:01:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d2314b39-35b3-3cbf-9c9d-cb3d2b04426f | -2.35253 | -48.42153 | 2024-11-16 04:01:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a16d149-4056-3fc2-82d4-69d29ae67e92 | -3.72928 | -45.66011 | 2024-11-16 04:01:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 57f9c8e6-4dad-3e08-a9c2-a5b745076f07 | -5.43206 | -42.88622 | 2024-11-16 04:01:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8894d4b4-9d17-328d-9b33-0cbad276bc9d | -4.31373 | -43.63361 | 2024-11-16 04:01:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5c6939aa-1809-3a37-b653-067a8b764e6f | -5.15638 | -44.08876 | 2024-11-16 04:01:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| cede8ce4-731e-3d1f-89a5-cb0950dea9e3 | -5.3381 | -40.89241 | 2024-11-16 04:01:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 370af6d6-25e2-34c7-b7a7-c8b69f34b44f | -4.03244 | -44.11192 | 2024-11-16 04:01:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ea6477c5-65e8-3525-9805-f86e09413dcb | -6.98177 | -38.47947 | 2024-11-16 04:01:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fd72a557-b3f9-3429-8a57-781990fe03ba | -5.66829 | -35.64423 | 2024-11-16 04:01:00 | NOAA-21 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 15.8 |
| dee02ecd-342f-3c1a-bb2d-b776806d08f8 | -3.96867 | -45.80252 | 2024-11-16 04:01:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b51b40a0-b60e-373c-8afd-272b8ba8b2b8 | -5.66684 | -35.65379 | 2024-11-16 04:01:00 | NOAA-21 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 32b2ba8f-5be0-3827-9bf6-a1b91a0f71eb | -4.73622 | -44.09399 | 2024-11-16 04:01:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| acae1bea-216f-3edc-912a-e98b538824ab | -7.45449 | -38.41679 | 2024-11-16 04:01:00 | NOAA-21 | IBIARA | PARAÍBA | Brasil | 2506608 | 25 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 1e7511d6-593f-39dc-844b-c9efcc8322fd | -3.07695 | -48.01315 | 2024-11-16 04:01:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5c55d194-0c35-3956-a748-0ff884b23c77 | -4.40098 | -43.81432 | 2024-11-16 04:01:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ce1b0a7c-0c90-3f9b-b616-bed1a16d3657 | 0.15447 | -51.14314 | 2024-11-16 04:01:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 37499b33-b1aa-376d-8638-c608208c2bef | -4.91094 | -44.02642 | 2024-11-16 04:01:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b15547f9-b6a3-32aa-96d9-e249e739e975 | -2.89914 | -45.34929 | 2024-11-16 04:01:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 02cf70e6-7571-358c-8e51-98d4a5c284af | 0.79703 | -50.74066 | 2024-11-16 04:01:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 299f85cc-d342-3f09-90ad-d9f499cd00ec | -4.28231 | -48.2044 | 2024-11-16 04:01:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21b4339f-b204-3979-9252-3978d6210912 | -3.76736 | -50.79383 | 2024-11-16 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 68ec23e9-63cc-37dd-8bcf-38d4d12568d1 | -4.99034 | -44.31599 | 2024-11-16 04:01:00 | NOAA-21 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| d5b2876e-5345-3d1e-95d1-bb8bb2de5e52 | -3.97232 | -45.80738 | 2024-11-16 04:01:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 24ad61bb-0c24-3231-ae4b-42de0f46b921 | -2.08246 | -48.951 | 2024-11-16 04:01:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c041d94b-3b2b-3211-99e7-ec62356da4d6 | -3.73495 | -45.65257 | 2024-11-16 04:01:00 | NOAA-21 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| de210be3-6d65-339b-940b-45de130d58ba | -6.02528 | -48.03683 | 2024-11-16 04:01:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| da12ba32-1d95-3748-8a9d-e57f57439d86 | -2.13336 | -48.7797 | 2024-11-16 04:01:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| d1757577-2c77-360c-acec-95765c5b6aa2 | -4.10406 | -46.10299 | 2024-11-16 04:01:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1bd4dbc9-4be6-3fee-bad0-8cb4973a924a | -4.28641 | -48.21127 | 2024-11-16 04:01:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1fadc58b-296c-345d-aea0-ccbdfd365022 | -4.65063 | -45.12728 | 2024-11-16 04:01:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| feca3da5-1ed9-3290-b323-332bc5c4506d | -4.74163 | -44.08498 | 2024-11-16 04:01:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 48f27bbc-d171-3d74-81c1-f148e1d6a489 | -3.7286 | -45.66425 | 2024-11-16 04:01:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 20d448c7-2b8b-31e7-802e-d6ba92b8abc4 | -5.61731 | -39.43343 | 2024-11-16 04:01:00 | NOAA-21 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8dcbba86-1b4a-3a99-ba23-984b9d28acaa | -4.35952 | -45.86598 | 2024-11-16 04:01:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0b39808e-877c-3923-b8f0-5bcdb3e12017 | -4.38178 | -48.07021 | 2024-11-16 04:01:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 034d0709-fd3d-38cc-9559-03b20f47ee07 | -2.47906 | -46.36623 | 2024-11-16 04:01:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bd316087-0313-3fe5-9f2f-4da809f1ea75 | -5.3496 | -45.57241 | 2024-11-16 04:01:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c4635758-4e91-3f8f-abcf-a11164f612ee | -3.19617 | -45.54984 | 2024-11-16 04:01:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 31.2 |
| b1827c24-8c7b-337e-a904-aee32df737ca | -6.24647 | -47.26921 | 2024-11-16 04:01:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5c4e29e5-4ccc-35ef-99c4-ce88ddfa253f | -4.00752 | -44.34119 | 2024-11-16 04:01:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 734ac716-8b5e-3e0f-9539-8c8edea4a56b | -1.85759 | -46.28194 | 2024-11-16 04:01:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7d116b10-eab6-3ec8-b8d2-115831538363 | -2.77268 | -48.58555 | 2024-11-16 04:01:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |


[Clique aqui para ver as próximas entradas](README22.md)
