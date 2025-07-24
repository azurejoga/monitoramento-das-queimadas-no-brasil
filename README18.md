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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d5bb1ff1-2c67-3417-82b8-4a6835ab2845 | -11.11039 | -50.48792 | 2025-07-24 04:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 926c4e21-8074-3e70-94db-ad6b8cd5da11 | -9.76117 | -41.88036 | 2025-07-24 04:42:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 4fca5a90-a49c-38c9-8ff4-8871e68a0c8d | -10.66022 | -47.26205 | 2025-07-24 04:42:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a8b5e8b2-6272-3389-ba31-ca1d8013ee34 | -9.52987 | -63.63318 | 2025-07-24 04:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b16c8d75-24b6-37eb-aea4-71b6c2d68891 | -8.92757 | -47.34079 | 2025-07-24 04:42:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 392b462f-b5ef-33f7-a9a3-174d98af2dd4 | -10.62926 | -45.238 | 2025-07-24 04:42:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 62fa7355-663d-303c-9e55-9e06b7d6cbbe | -11.77393 | -47.40437 | 2025-07-24 04:42:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6021190c-b3f5-360e-8e81-e0e118c80eac | -13.70179 | -45.68684 | 2025-07-24 04:42:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0415b028-c8e0-3f60-b3de-10218402c899 | -7.25099 | -60.18775 | 2025-07-24 04:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e308219-f3dd-3180-855e-abded8df6d20 | -11.46086 | -48.163 | 2025-07-24 04:42:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fb1a3471-595f-38a5-afa7-5b0bf1e42fa4 | -10.00355 | -48.12502 | 2025-07-24 04:42:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 722cb8ba-27ea-38df-a01a-6c7d767aa535 | -8.0946 | -50.0826 | 2025-07-24 04:42:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 050017ed-4d94-31b4-baff-bec8e2ffebb7 | -13.7059 | -45.68744 | 2025-07-24 04:42:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1399d519-1a88-3972-b167-497daf51e0ab | -11.94839 | -58.76438 | 2025-07-24 04:42:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 286b52f2-766d-33ea-975e-4c9eade07a9d | -11.79204 | -57.24525 | 2025-07-24 04:42:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f44fb01-d6c6-3a7c-b842-5cf1b0124bec | -8.49363 | -47.23399 | 2025-07-24 04:42:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3b0cf62a-4890-32b1-b961-5cecb9a1a191 | -12.42403 | -45.37965 | 2025-07-24 04:42:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 66e08c12-970c-3172-bc5e-3fa0727940a4 | -10.62613 | -49.45329 | 2025-07-24 04:42:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d3155cf1-4bb6-3ec0-a9de-608a1174068d | -10.71648 | -49.48192 | 2025-07-24 04:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 64755de2-11fc-3c33-8847-395762bf75af | -9.34651 | -49.91511 | 2025-07-24 04:42:00 | NPP-375D | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| da9634f1-0820-3fe6-87ed-5e173d2ec41f | -11.77756 | -47.4049 | 2025-07-24 04:42:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3f01ee3c-c726-3606-8610-cc550bcc8e7b | -12.49962 | -57.77264 | 2025-07-24 04:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c274626c-5ae2-3c22-a876-27ff63a9a387 | -10.71593 | -49.48548 | 2025-07-24 04:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb01e55f-5304-3efc-b7ce-8d6915555861 | -13.64731 | -46.81709 | 2025-07-24 04:42:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f087757-cd36-3a54-80c4-6d6ba5d29122 | -8.72249 | -51.13437 | 2025-07-24 04:42:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 541fa2b6-14cc-330d-8108-7589c93c66ef | -10.05022 | -48.66226 | 2025-07-24 04:42:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ad5dd815-6ba6-3e94-b5d3-c6f4b941ba66 | -7.45154 | -57.66529 | 2025-07-24 04:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 83e618cc-a647-3819-9234-23795725b4f3 | -13.64822 | -45.72584 | 2025-07-24 04:42:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 911270d4-44ab-35bc-af0e-4c5770c4c753 | -13.21636 | -51.08011 | 2025-07-24 04:42:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e87529bd-7830-3278-a4eb-4a9a11313809 | -10.62572 | -45.23381 | 2025-07-24 04:42:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| fde0fc69-f31d-372b-a46b-2d3e40e37053 | -12.25701 | -44.78288 | 2025-07-24 04:42:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6b06eb62-2b99-3da5-aad2-495c62eadb3b | -13.69965 | -45.67116 | 2025-07-24 04:42:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9f2645d4-e2a4-3fbd-aaa3-60b014b3d4eb | -9.05793 | -45.06342 | 2025-07-24 04:42:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 80eed95a-953a-3e14-b52d-15cbce8c9b54 | -10.3626 | -48.23528 | 2025-07-24 04:42:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d5fba0da-a7ee-361c-87ee-c02c5474f4a8 | -14.17952 | -45.35197 | 2025-07-24 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f25ed063-4a2c-3e93-897c-698ff3b76355 | -9.31938 | -44.84926 | 2025-07-24 04:42:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 49054a13-6f1a-37fd-b28a-3ae8e9e3ecf5 | -10.63083 | -45.22709 | 2025-07-24 04:42:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b61f0571-d95e-307c-936f-4f37a1e9a588 | -10.70716 | -48.85963 | 2025-07-24 04:42:00 | NPP-375D | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fb1af2d0-d6ce-3378-8889-b3e8e4fc24e9 | -10.62624 | -45.23018 | 2025-07-24 04:42:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ff411f66-88bf-31e9-a5ef-677274e68bf3 | -8.72999 | -50.25921 | 2025-07-24 04:42:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d05b6b08-a4b6-3ed6-bef6-8d04441c98dd | -13.70477 | -45.68064 | 2025-07-24 04:42:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 45b45b0d-cc7c-39fb-8202-135e181394b5 | -13.74484 | -45.92355 | 2025-07-24 04:42:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 751ead43-3bc2-39fd-9b72-414afa27179f | -13.7074 | -45.67614 | 2025-07-24 04:42:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 899b2e7d-d696-31eb-831d-3e9d446a3828 | -9.20617 | -59.67853 | 2025-07-24 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2663aead-4a37-3fb5-b1ff-9daa33be202a | -11.11482 | -50.48143 | 2025-07-24 04:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3f20a1bd-6256-3522-94c5-1d2041a69578 | -13.69916 | -45.67493 | 2025-07-24 04:42:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8aa0b0ad-6ffd-30a7-9373-9f0b191e891b | -11.46435 | -48.16353 | 2025-07-24 04:42:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ec0ee6b7-3605-3822-8a5a-521996727041 | -13.70377 | -45.67176 | 2025-07-24 04:42:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 40ed4c59-2ed8-3dea-848a-46cb11d72951 | -8.36839 | -51.07716 | 2025-07-24 04:42:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a7e09717-3565-3984-b284-756910b33171 | -8.09737 | -50.08661 | 2025-07-24 04:42:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c0c39df9-4427-3f6b-b00c-4142ed8470a6 | -12.50785 | -57.77921 | 2025-07-24 04:42:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a5e94230-a61a-3066-be3e-5e80ab58d750 | -11.73487 | -48.18662 | 2025-07-24 04:42:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 3b70f6f4-d142-3cc5-9efd-9d2788ba5b7d | -13.70687 | -45.66556 | 2025-07-24 04:42:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 60113f40-cc5c-3bc5-9515-902d8b05396b | -11.11814 | -50.48197 | 2025-07-24 04:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aec922bb-f10f-39d4-b374-e671f2659882 | -10.18116 | -50.22358 | 2025-07-24 04:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9441e495-78e9-3df9-a8c0-51b4ae46cbbc | -13.21524 | -51.08719 | 2025-07-24 04:42:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| bba22b2e-416a-35a0-a86a-273d4ee3d184 | -9.06195 | -45.06404 | 2025-07-24 04:42:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 880c3743-6170-3547-b302-4c74dc140c24 | -11.10707 | -50.48738 | 2025-07-24 04:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ef578b52-0c5a-3ad4-9fcc-cc661bcd6348 | -13.70015 | -45.66738 | 2025-07-24 04:42:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 97012daf-0a8e-3274-b025-3df642ab8f54 | -11.73545 | -48.18266 | 2025-07-24 04:42:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 843d142a-5866-3b35-80a0-eb69953dad97 | -11.87553 | -48.63074 | 2025-07-24 04:42:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35c5586c-7d11-3233-b85f-fd131194b3bf | -9.19938 | -59.68458 | 2025-07-24 04:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e4630147-41f8-3def-8d3a-489a302cae96 | -10.66796 | -47.78389 | 2025-07-24 04:42:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d7c8b353-733b-3331-90d7-d6395a798a22 | -10.62217 | -45.22964 | 2025-07-24 04:42:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7b9b2ec2-3e80-3c58-903d-6b4300023046 | -13.09687 | -52.13905 | 2025-07-24 04:42:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 005bb929-54d4-3357-a060-393783566183 | -8.92636 | -47.34872 | 2025-07-24 04:42:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 43924bac-e9b7-3f44-bcca-003620b3d700 | -10.67323 | -47.79677 | 2025-07-24 04:42:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 00ef3118-702d-3550-9c69-9cc347e6cd48 | -10.06822 | -46.83956 | 2025-07-24 04:42:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 55343ab5-2a66-3944-aafe-3994a7afcccd | -13.69444 | -45.69449 | 2025-07-24 04:42:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d44eb34-5330-3d4e-9bc6-190a980dde48 | -12.66028 | -45.03594 | 2025-07-24 04:42:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ddbac2c8-be59-3741-a58e-824d001fbdb5 | -10.04528 | -59.09791 | 2025-07-24 04:42:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd215874-ef9e-3c4f-9b50-c07d12354678 | -14.78977 | -42.44048 | 2025-07-24 04:42:00 | NPP-375D | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0221c8da-4870-37d0-bc9a-97a50f1a82d6 | -13.64873 | -45.72212 | 2025-07-24 04:42:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 121f9b38-66b7-333b-94c0-f0e26e1bcb18 | -11.94725 | -58.77043 | 2025-07-24 04:42:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 17.8 |
| b4c7a22d-509d-306f-be59-eb3332f26aae | -7.45699 | -57.6674 | 2025-07-24 04:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9d04a3c6-d10c-30aa-b6f5-3ca7a1447568 | -13.69961 | -45.68756 | 2025-07-24 04:42:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 89179dd4-7570-3e73-98af-548a6801ec82 | -13.54339 | -44.50181 | 2025-07-24 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3938c4f2-c379-3d1b-9083-9aeb34f2b297 | -9.58587 | -46.32557 | 2025-07-24 04:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f21c2ccc-bc3d-3472-9806-79d8c0ab0c26 | -12.42763 | -45.38401 | 2025-07-24 04:42:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 29cd89a7-f7e1-30cf-ac06-850c3a4ba9a5 | -8.47942 | -49.55559 | 2025-07-24 04:42:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1839d9cc-4319-3b65-98ea-97eec1839dc1 | -13.69811 | -45.66813 | 2025-07-24 04:42:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5aed4daf-304f-3e38-9508-7b497ab82260 | -13.68082 | -47.73794 | 2025-07-24 04:42:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f8c5e7cf-71f3-398d-8b90-65467777349a | -9.66699 | -49.89762 | 2025-07-24 04:42:00 | NPP-375D | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ce347106-62f7-39a9-85e4-875ea65f2749 | -8.72191 | -51.13796 | 2025-07-24 04:42:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 72b47705-c47f-3c14-b09a-366a20db7a54 | -12.70991 | -47.79485 | 2025-07-24 04:42:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0b569888-e2ac-3267-bf9e-8105b49f1f5f | -13.7064 | -45.68367 | 2025-07-24 04:42:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ef39434f-837b-391c-b64b-90166260ef28 | -10.06757 | -46.8439 | 2025-07-24 04:42:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f0881c75-ae55-3c7f-b664-fc7e8290a588 | -13.54502 | -44.50008 | 2025-07-24 04:42:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b856cdb-1870-30fd-964a-188aa5e5b326 | -11.77818 | -47.40066 | 2025-07-24 04:42:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 47eda15c-921b-397d-af4d-1baabcb0545c | -19.36673 | -52.03971 | 2025-07-24 04:44:00 | NPP-375D | INOCÊNCIA | MATO GROSSO DO SUL | Brasil | 5004403 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4fefe492-0bd9-3196-a6be-bcf2227ccfe9 | -22.69888 | -43.35102 | 2025-07-24 04:44:00 | NPP-375D | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 3eb7fa0d-700c-37ef-ac2f-6fcc7faeaea2 | -14.77126 | -48.27336 | 2025-07-24 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 09277847-0841-3506-8dda-8964c035a0fb | -18.83372 | -41.98195 | 2025-07-24 04:44:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| af7246b4-f1a1-3c54-a6da-a8009ddb999b | -14.34069 | -52.07209 | 2025-07-24 04:44:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 93663f98-44f6-3438-bf5f-bcb270d8b0c5 | -15.75771 | -43.37344 | 2025-07-24 04:44:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 87025223-cc78-3434-9280-ba6b4a13114c | -21.36542 | -48.5297 | 2025-07-24 04:44:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3bf5b8e8-b9fe-3820-bf79-8a7a21badfbb | -18.44575 | -54.67523 | 2025-07-24 04:44:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 14e414ae-c9a5-32c4-87ac-3cd30709ae3d | -18.85349 | -47.96318 | 2025-07-24 04:44:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| ab5fdad7-e41c-3fc2-9f8d-fbe34077e61a | -21.19526 | -49.29662 | 2025-07-24 04:44:00 | NPP-375D | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 33670f5c-ed3e-3653-ab39-33e5e38a3cf4 | -18.26879 | -51.14155 | 2025-07-24 04:44:00 | NPP-375D | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README19.md)
