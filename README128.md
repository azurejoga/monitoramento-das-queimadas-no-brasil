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

## Dados Diários - Página 128

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d9311eaf-0043-38cd-90f0-1a3dda8037f1 | -17.08246 | -56.78644 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 80b8de52-72ee-3426-9ec4-637e86261722 | -17.0815 | -56.79172 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 31fa73dd-36cb-3a19-b122-0feb45298ded | -17.08053 | -56.797 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| ed10d83d-9484-3035-96a1-b259989229f8 | -17.07851 | -56.78566 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| b9338cd6-32f5-30bc-9a7e-53e170b99a69 | -17.07755 | -56.79094 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| b8426da0-278c-3905-85ae-a5497c331036 | -17.07658 | -56.79622 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| a980075c-1da9-3ed1-b0eb-7c9256db4a8e | -17.07562 | -56.80151 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 755db44a-54a0-3868-b4cd-a0180e1b5b26 | -17.07167 | -56.80073 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 27a0fb61-0d95-3bf4-a9bc-5bd0853ba774 | -22.37029 | -47.93802 | 2024-10-05 04:42:00 | NOAA-20 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9184fdb1-7433-342b-87b9-78ea98699db2 | -21.89508 | -48.47695 | 2024-10-05 04:42:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1df35aab-10cb-3dd2-a0aa-e9f2849ab4ba | -21.85029 | -48.42866 | 2024-10-05 04:42:00 | NOAA-20 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 88ccf4dd-ba99-3292-8978-982a8a15887e | -21.84708 | -48.423 | 2024-10-05 04:42:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aa39bb0b-f4ee-38ae-966c-2798e1ecac6e | -21.84644 | -48.42809 | 2024-10-05 04:42:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| edc28896-35a0-34e8-83ce-0caf2d20a17d | -21.84258 | -48.42751 | 2024-10-05 04:42:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3f731eb1-c8ff-3434-858a-78befb944ced | -21.77958 | -47.04575 | 2024-10-05 04:42:00 | NOAA-20 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| cfeb0511-b0ea-35e1-841a-5721bde67075 | -21.77886 | -47.0434 | 2024-10-05 04:42:00 | NOAA-20 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6f0ad239-c5ec-3eb7-b65c-950cbf48ae7c | -21.77836 | -47.04741 | 2024-10-05 04:42:00 | NOAA-20 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| afcf2a94-83fb-356d-9ab2-a0db65c01edc | -21.77467 | -47.04285 | 2024-10-05 04:42:00 | NOAA-20 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f52b2d57-8350-346a-842a-c34e06b2845f | -21.77417 | -47.04689 | 2024-10-05 04:42:00 | NOAA-20 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b1b650b9-3a42-357f-b580-e489d74a2dc9 | -21.77048 | -47.04227 | 2024-10-05 04:42:00 | NOAA-20 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 047c3d25-00ec-30e5-b23e-fadebf2091da | -22.83635 | -48.41467 | 2024-10-05 04:42:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a8bba39e-b4dc-30e5-b0c1-29800032f4fa | -23.65128 | -47.42826 | 2024-10-05 04:42:00 | NOAA-20 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f4de92be-a527-3e7c-9085-5d8c1a3e385c | -23.65079 | -47.43234 | 2024-10-05 04:42:00 | NOAA-20 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 32b5850f-2050-3ca9-b6eb-e81ab7076206 | -22.39138 | -49.27394 | 2024-10-05 04:42:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 2575bda1-9471-37d1-80a4-dd3d86673610 | -21.80602 | -48.74396 | 2024-10-05 04:42:00 | NOAA-20 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c2d9a8f6-05cb-39c8-8968-62628e28193f | -21.80538 | -48.74888 | 2024-10-05 04:42:00 | NOAA-20 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8d4e58c4-5d46-3c3d-a304-3cd9f581512f | -21.33344 | -48.88728 | 2024-10-05 04:42:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 60e618e7-32d0-37fe-b442-201992525df4 | -21.33183 | -48.88932 | 2024-10-05 04:42:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4a03f9a9-a3e9-363a-831a-e72b57714a9a | -21.80981 | -48.7445 | 2024-10-05 04:42:00 | NOAA-20 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 00317e1a-7791-3d43-89dd-24af3875407c | -21.80917 | -48.74943 | 2024-10-05 04:42:00 | NOAA-20 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 06a87583-b855-33b1-8ed7-8537b447a947 | -21.80853 | -48.75436 | 2024-10-05 04:42:00 | NOAA-20 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8c8b80e1-33fa-3305-b5f7-86bd3d05ae40 | -21.33282 | -48.892 | 2024-10-05 04:42:00 | NOAA-20 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 74621dd6-699c-3916-9f55-83bb236a41ee | -23.78247 | -49.92174 | 2024-10-05 04:42:00 | NOAA-20 | TOMAZINA | PARANÁ | Brasil | 4127809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 2fe5246a-922d-3911-a9a5-8ba643dd0e40 | -23.78207 | -49.92363 | 2024-10-05 04:42:00 | NOAA-20 | TOMAZINA | PARANÁ | Brasil | 4127809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 954dd7b2-2992-3a6c-9ea7-985a11b8afbc | -23.77844 | -49.92302 | 2024-10-05 04:42:00 | NOAA-20 | TOMAZINA | PARANÁ | Brasil | 4127809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| d81a7a2c-2b46-32af-8e72-6f473ff83735 | -22.53938 | -48.81346 | 2024-10-05 04:42:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 21ba9974-0b78-3a4c-a90f-b60893440229 | -23.47299 | -49.18481 | 2024-10-05 04:42:00 | NOAA-20 | TAQUARITUBA | SÃO PAULO | Brasil | 3553807 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b335fce5-0516-3194-b735-2fbbc1753ff9 | -21.90112 | -50.72056 | 2024-10-05 04:42:00 | NOAA-20 | BASTOS | SÃO PAULO | Brasil | 3505807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| dc6e2835-3a0e-3546-9e91-b7db9a39db43 | -23.30533 | -51.12765 | 2024-10-05 04:42:00 | NOAA-20 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 65cac9e9-7d95-3078-8a65-5ff2832271cc | -20.99496 | -51.79214 | 2024-10-05 04:42:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f313e790-7a5e-3da9-a162-913d3b293762 | -22.77037 | -53.36822 | 2024-10-05 04:42:00 | NOAA-20 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| de99dd8b-8aa6-3978-87fb-498369dc06d3 | -22.76823 | -53.3602 | 2024-10-05 04:42:00 | NOAA-20 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 189f5b61-8abf-3614-acab-4ff9e8a0b28e | -22.76765 | -53.36388 | 2024-10-05 04:42:00 | NOAA-20 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7d8b7097-49d9-33d0-b063-7c47ad4f9d61 | -22.76006 | -53.34717 | 2024-10-05 04:42:00 | NOAA-20 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3b5e0a6e-f608-330c-8ae6-b55dee1d2507 | -22.70888 | -53.24239 | 2024-10-05 04:42:00 | NOAA-20 | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ed5487b5-9286-303f-8c4f-9191d28daf55 | -21.25701 | -53.16409 | 2024-10-05 04:42:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 427e6eb1-4f54-3f48-8911-2084ab538ad3 | -20.47169 | -55.53066 | 2024-10-05 04:42:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d5f00cd4-8d0f-31fe-ba8c-56859644971a | -22.04061 | -55.93292 | 2024-10-05 04:42:00 | NOAA-20 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a7bb8fe8-29fd-343b-be51-c9c806431d62 | -21.65745 | -54.82684 | 2024-10-05 04:42:00 | NOAA-20 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6797a440-b850-3c54-965e-c23fe27d6b81 | -21.36541 | -55.69909 | 2024-10-05 04:42:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5e7773da-29f3-36ce-9944-fbcecb3edf13 | -21.66085 | -54.8275 | 2024-10-05 04:42:00 | NOAA-20 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 22f3263f-88c7-3924-8e96-283a83e2cdda | -22.58125 | -54.99469 | 2024-10-05 04:42:00 | NOAA-20 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 143914ea-62ef-39b1-bacc-32361f3c9d3b | -30.14846 | -52.0271 | 2024-10-05 04:44:00 | NOAA-20 | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 0.3 |
| 473c1dfc-75d4-3169-a671-f7a37901091a | -29.81259 | -51.17768 | 2024-10-05 04:44:00 | NOAA-20 | SAPUCAIA DO SUL | RIO GRANDE DO SUL | Brasil | 4320008 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| bd0076ec-9bc7-31de-9ece-276e76ffbe03 | -30.8818 | -52.49138 | 2024-10-05 04:44:00 | NOAA-20 | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 375dea6d-cf55-30c2-8d84-1b0e0cccfb0e | -30.87829 | -52.49076 | 2024-10-05 04:44:00 | NOAA-20 | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 7fc1da34-4c0e-3ce4-9782-61bf97687200 | -28.92558 | -55.59521 | 2024-10-05 04:44:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| 032cc140-2887-3b8f-9300-d1fb32f7a1f1 | -28.92494 | -55.59918 | 2024-10-05 04:44:00 | NOAA-20 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| b9186423-fbe5-3da9-bfdd-7be1db5e48fc | -6.9514 | -59.0666 | 2024-10-05 04:45:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 7b445d86-e03c-32d0-bc4c-f3604e2ba329 | -9.8802 | -59.5008 | 2024-10-05 04:46:02 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 41.9 |
| cca95ca9-197f-34d3-8746-c04ad583546e | -11.2566 | -60.5825 | 2024-10-05 04:46:10 | GOES-16 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 54.5 |
| ed33e193-33ea-35b2-8611-47459aa4bf9c | -11.8768 | -56.957 | 2024-10-05 04:46:14 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 202.2 |
| a309fb99-cdb5-37ac-b272-066ffd5d21e6 | -11.896 | -56.9354 | 2024-10-05 04:46:14 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 05b3eddc-8a60-3b68-9d15-2cfc8b81e583 | -11.8957 | -56.9554 | 2024-10-05 04:46:14 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 171.6 |
| dee86aea-fc97-362b-9cad-97ba4041dc25 | -11.877 | -56.937 | 2024-10-05 04:46:14 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 1ca11540-e791-3b2f-93c9-30b9a83b581a | -1.07075 | -47.92838 | 2024-10-05 05:06:00 | AQUA_M-M | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| a9dfc8b7-6627-3494-b21a-85f4bd1084cb | -6.65684 | -42.00351 | 2024-10-05 05:08:00 | AQUA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| d621ab41-6696-38d7-b126-2c6f63ef6038 | -8.38664 | -43.65342 | 2024-10-05 05:08:00 | AQUA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| e77f202c-8979-3253-9dbc-72204448c05e | -7.81372 | -43.10495 | 2024-10-05 05:08:00 | AQUA_M-M | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 5e1ca087-fa2a-396f-bc80-7279b28f41f0 | -7.81238 | -43.11395 | 2024-10-05 05:08:00 | AQUA_M-M | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 0c31c67e-6202-371e-83dd-5b289f34fd47 | -7.76686 | -43.0522 | 2024-10-05 05:08:00 | AQUA_M-M | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 22d01142-4fc7-3afd-b270-be22a25fc216 | -7.76553 | -43.06121 | 2024-10-05 05:08:00 | AQUA_M-M | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 16f02402-55b7-398e-9084-94579f5494ea | -7.76421 | -43.07019 | 2024-10-05 05:08:00 | AQUA_M-M | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 8907ea7c-7661-33d6-9a77-8cccc154dcf7 | -7.71158 | -42.98289 | 2024-10-05 05:08:00 | AQUA_M-M | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 05bf22cc-5f37-3829-a04a-bdfa48f23a4d | -7.51848 | -44.83127 | 2024-10-05 05:08:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| a67e99af-4a43-3ece-842e-4e1947b60661 | -7.45873 | -44.73295 | 2024-10-05 05:08:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f0ac9626-55a2-393f-aaed-89a6ad20ee14 | -7.45736 | -44.74201 | 2024-10-05 05:08:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e64fc371-909e-3bed-8f11-5f357cd75657 | -7.13901 | -42.61409 | 2024-10-05 05:08:00 | AQUA_M-M | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 5817c2d7-81f2-3b3e-bba4-ffd5fdb0b860 | -6.85995 | -42.82121 | 2024-10-05 05:08:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 6534b7d3-1839-3a23-bc34-76ad0f910bdd | -6.85029 | -42.8139 | 2024-10-05 05:08:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 9d8fe3c4-402b-3d2e-91a2-9f46a52beeaf | -6.84894 | -42.82293 | 2024-10-05 05:08:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 384fcef4-478b-3079-800d-27ccecfadc75 | -6.65823 | -41.99396 | 2024-10-05 05:08:00 | AQUA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 16.3 |
| c0c35a9a-f39f-340f-9f98-95770bf38567 | -6.30382 | -43.02322 | 2024-10-05 05:08:00 | AQUA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9931f018-b5e0-3f30-8cad-2762b8ada2f9 | -5.70241 | -43.16076 | 2024-10-05 05:08:00 | AQUA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 26fc720a-4a11-310d-b43c-e823db2772b2 | -4.96314 | -43.77628 | 2024-10-05 05:08:00 | AQUA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| d006c363-68ca-3318-8752-dda003ceed09 | -4.9618 | -43.78517 | 2024-10-05 05:08:00 | AQUA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 4350927c-b72f-33a5-ae0f-f4b910ba6613 | -4.95286 | -43.7772 | 2024-10-05 05:08:00 | AQUA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 5cdf7e12-3fb9-38b9-bd59-2a21160dd4e7 | -4.03678 | -43.24665 | 2024-10-05 05:08:00 | AQUA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 5d45221c-926b-39f6-a93c-86dc08de4e80 | -4.03546 | -43.25546 | 2024-10-05 05:08:00 | AQUA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0c7be26a-a0b8-3917-bdd2-85bd163f4d9a | -4.02794 | -43.24536 | 2024-10-05 05:08:00 | AQUA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 7368442e-7f7b-3179-9b26-b37024f0e39b | -4.02662 | -43.25417 | 2024-10-05 05:08:00 | AQUA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6247c652-d22f-31b3-8770-973dd5418911 | -3.49215 | -43.36412 | 2024-10-05 05:08:00 | AQUA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ca7da33e-b94d-3d6b-aa10-5bdb8c3e6998 | -7.20265 | -47.83715 | 2024-10-05 05:08:00 | AQUA_M-M | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| bc77f9f9-5dfd-3a00-8670-3763d5e8d293 | -7.01062 | -45.73462 | 2024-10-05 05:08:00 | AQUA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| dbe0f55e-7397-3afc-ab55-b0773d21336e | -6.36024 | -45.69351 | 2024-10-05 05:08:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| c59a26a3-3313-33d7-aa19-16847d7429f4 | -6.35869 | -45.7035 | 2024-10-05 05:08:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 12ea7174-6d83-316f-9f15-7105352adac2 | -6.19647 | -45.43521 | 2024-10-05 05:08:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 38.1 |
| f3e3744a-c277-3fd0-8b71-b947d1655e45 | -6.19495 | -45.44501 | 2024-10-05 05:08:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 81f9f830-d510-3017-b3ab-51f46fc99db8 | -6.09676 | -44.70612 | 2024-10-05 05:08:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6dd1181a-6f29-3b9c-ad2c-55fb9660937f | -6.08775 | -44.70478 | 2024-10-05 05:08:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |


[Clique aqui para ver as próximas entradas](README129.md)
