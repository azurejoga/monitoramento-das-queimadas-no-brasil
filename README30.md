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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d964adc6-6c82-384e-a316-3a4ef54089f2 | -6.80008 | -58.6273 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 69744c01-94e6-34b1-9a1b-ff0f1c441096 | -13.45075 | -51.76907 | 2026-08-22 04:27:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| da88b2c1-bc3b-3dd3-a4e7-ec6b1ad8ee9d | -6.79169 | -58.63683 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9a0199d0-6011-3871-bca6-40234ae62ed9 | -6.0124 | -57.79118 | 2026-08-22 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 20fe7070-0e00-3ef3-8b4e-bc537e639de4 | -10.80041 | -50.98808 | 2026-08-22 04:27:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 949c2829-ad25-3845-8511-0d223c7b6512 | -6.93796 | -59.31929 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 32a14588-2373-3fc5-ad42-05932ac50d89 | -11.35507 | -46.34646 | 2026-08-22 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 36043a8c-b1de-3f25-a964-ab1c63d83d5a | -6.85663 | -59.43873 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2c3dce83-29fc-3b5a-be9c-c652cd0ca75e | -8.52542 | -54.82695 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 3e59a7a6-e77c-350b-b228-aeee1f826aa1 | -9.39402 | -55.98129 | 2026-08-22 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 396bfa53-10ff-335b-837c-c0d3e55e4cff | -11.95208 | -45.4907 | 2026-08-22 04:27:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f20a312b-5831-37be-afa0-63025764c230 | -6.53757 | -58.52233 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 222c8d5a-085e-387f-a5b1-c24e46684800 | -6.77178 | -58.67256 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 32870459-d3a6-3211-9e04-c28e3c6ffadf | -11.17469 | -54.0087 | 2026-08-22 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e12e3196-c390-31ce-a344-dc58df1934ef | -6.80506 | -59.41733 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| ef7f054b-c122-3521-884d-557d3b7ec900 | -14.40336 | -43.79315 | 2026-08-22 04:27:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 550a3ae1-8a58-3ec7-99ff-608ba54d5fd0 | -10.96855 | -44.31097 | 2026-08-22 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ff499a84-5168-3202-a65a-178e5e083f58 | -6.79807 | -58.63818 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 96102d32-139a-3c12-a383-3bdca96be9a7 | -11.16949 | -54.01223 | 2026-08-22 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 55253e97-3543-3238-bd53-11129e4b3601 | -6.37177 | -54.94627 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fd5990be-8bf5-37f3-bd2d-e5555d9a73f8 | -8.63031 | -54.702 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a224879b-9690-3f12-a9f4-1530213f87ec | -11.55688 | -46.9395 | 2026-08-22 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| af4f147d-1dc2-3080-ab5d-57b79f3e8e57 | -13.09047 | -43.33532 | 2026-08-22 04:27:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 5ad39e4c-c3a3-36ba-94f7-062c34023440 | -11.5602 | -46.94003 | 2026-08-22 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b5471950-cbed-38ab-a2fe-f3178bde397e | -6.7944 | -59.42297 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.0 |
| e8fc004a-ecf7-3b43-97f6-08149db16a0d | -12.00966 | -53.43211 | 2026-08-22 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ddb658d-eaf1-34a7-91d0-33e12bab33b5 | -9.00177 | -50.73583 | 2026-08-22 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b6d31d8d-50fd-34a1-9406-080276022d78 | -11.16267 | -54.02466 | 2026-08-22 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a151a9e-5e28-3f59-a025-da4df66b30a8 | -7.37007 | -55.69194 | 2026-08-22 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 68233c00-3e6b-3f1c-8e70-3582d9804362 | -10.53025 | -50.78272 | 2026-08-22 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 72afeaed-6832-3fe2-b6e3-7743dfe7ec01 | -7.71627 | -46.14708 | 2026-08-22 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 27b02ea5-d6c0-3ae2-8bd7-b05aaad8d2fd | -6.96979 | -59.05114 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 503bacae-8abe-3c17-a016-827ecbf544ab | -10.30406 | -48.22909 | 2026-08-22 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 314d3392-8e55-3d6b-b1ae-4e5116e392d7 | -12.77612 | -48.38595 | 2026-08-22 04:27:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 94ad7ba8-dd66-39c3-a331-46dd0793cf61 | -6.78814 | -59.43302 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 2e1ca4ba-91ee-37c3-bd7b-181cfd2eba16 | -11.44825 | -44.53764 | 2026-08-22 04:27:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8d1ca828-1755-3506-801c-bb284183dc9f | -9.21241 | -60.76469 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 426366bf-93dc-38db-a2e1-58cb95173d60 | -6.76022 | -58.69602 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b9f9d5ca-4b2d-35ef-8fc7-d81a62610c2a | -9.43581 | -51.61531 | 2026-08-22 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e22bc427-cc8b-397e-a01b-21d1220de9eb | -9.16291 | -59.47025 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| bcffaa6f-cba7-355d-bf27-5f5ce710fabc | -13.48007 | -44.04144 | 2026-08-22 04:27:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c7ced3a9-aeee-324e-8883-3e2b560ba24e | -6.7933 | -59.42896 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.0 |
| af2cc7b6-0c89-375e-9098-612bcce9740a | -9.39003 | -55.97822 | 2026-08-22 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 798d2534-b385-32dd-807a-5012c384b206 | -6.79655 | -59.41132 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.9 |
| e2e82588-064e-3762-8ba7-a2b9f59d7c1e | -8.54195 | -55.32454 | 2026-08-22 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7cc3e269-a5bb-37d0-b97e-51ace859c0e8 | -6.8022 | -59.41838 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.9 |
| e05c0416-0c7d-39bf-a8ac-8eb4047b83f9 | -12.2669 | -43.1256 | 2026-08-22 04:27:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 3bfc7b2e-1936-3c86-8bbf-aa0b54e139df | -6.61005 | -58.38744 | 2026-08-22 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 14c9ad3a-3fd7-390b-9d54-4a15884f0de2 | -8.16776 | -54.98789 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9262c44d-d473-3331-a698-38c2423b6b81 | -6.75248 | -58.66908 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 56f2ccaf-7ac1-34f6-ad0b-141fbff1843f | -11.2072 | -55.04412 | 2026-08-22 04:27:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5055095f-f832-3dd2-bf0e-18b716407eb9 | -10.86461 | -51.05178 | 2026-08-22 04:27:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b0b8a330-a982-34c7-80d4-df3cb4084de3 | -8.09307 | -51.66423 | 2026-08-22 04:27:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a92242f5-cc66-3451-bf93-f1fd557482cf | -6.93359 | -59.30603 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 27bc6fac-4fb7-31e8-b3ff-fdebac1c957a | -12.58904 | -47.88843 | 2026-08-22 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 55628018-7f5f-37ae-9945-f3c059091713 | -8.58795 | -54.74408 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d458a658-074f-36e6-8d3a-d9aa48bce110 | -6.75348 | -58.66372 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 11ebe04a-ed7e-3b4a-b9a5-f7d55b8d0a69 | -8.9997 | -50.71426 | 2026-08-22 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6151b74e-6621-323b-b96f-ead519f3335e | -14.40268 | -43.79806 | 2026-08-22 04:27:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9b505178-6648-3560-ab51-eb16bd76141a | -14.13194 | -48.06778 | 2026-08-22 04:27:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5d3178b5-3755-37c6-9659-783b74805315 | -6.25121 | -55.41716 | 2026-08-22 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c85b9439-db42-38c3-9e73-e909a96d7b8a | -6.77327 | -58.70042 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f1b07c87-60c9-3e7d-a70e-ed87e06fccb4 | -6.7531 | -58.66161 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 15.1 |
| d8570ba8-eba3-36c5-8248-d1c19a39b04c | -9.17025 | -59.46524 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 09f2a57f-e941-39c1-b608-8249494f298f | -7.36123 | -55.6803 | 2026-08-22 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 40824b98-dfec-3240-8459-4786082357b7 | -12.01102 | -53.42426 | 2026-08-22 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 302218fd-9c78-300e-a345-650d9c1254b2 | -11.16329 | -54.02537 | 2026-08-22 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 41bd0146-a68a-32db-bc1b-616415c61e23 | -11.1656 | -54.0121 | 2026-08-22 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b0ff41ad-544f-37d0-8937-9f1f77a06abc | -9.52307 | -51.64772 | 2026-08-22 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a3958fe1-9eea-3c4e-a0b2-f08961f0779c | -6.25009 | -55.39294 | 2026-08-22 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a9060e94-6413-3b89-bd56-63134105d9ca | -8.0266 | -51.80313 | 2026-08-22 04:27:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f2822d3-8a65-3493-a417-78f445770ef4 | -11.73872 | -45.58376 | 2026-08-22 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 14a7e311-300d-30d5-ba9b-836efb64fed0 | -9.44231 | -51.60066 | 2026-08-22 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 47112c3f-8488-30fa-8ef8-39e05b822817 | -9.00568 | -50.74783 | 2026-08-22 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 52fbe834-0b1f-3234-8cda-3c205215142f | -6.97534 | -59.0579 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 01b26aa4-f035-3bd4-bc89-3dfcbc4639a9 | -12.85177 | -48.44551 | 2026-08-22 04:27:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7918a9a3-d685-3dec-9768-20fb59e10dd2 | -12.76462 | -47.10559 | 2026-08-22 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8783112d-278d-34f2-b7e5-34760f385e1e | -12.79714 | -51.47952 | 2026-08-22 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6d94d72f-5de3-3c00-9de1-98ec3ce4dd89 | -8.59279 | -54.74499 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a8063593-d6cd-353e-aaac-3f66d0156728 | -6.77223 | -58.70602 | 2026-08-22 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e57a793e-c180-35ef-ab00-501f9e52756f | -6.81945 | -59.6744 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 60135d3d-6dcf-3359-b51f-027ed94df436 | -8.99157 | -50.7406 | 2026-08-22 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6cb253a5-30d2-3631-8ab6-fae876ef3d82 | -12.76728 | -48.39888 | 2026-08-22 04:27:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e26c7148-456d-3ce4-ba79-7ff05bc0bdb8 | -14.00132 | -42.47678 | 2026-08-22 04:27:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 31fa0ecb-5da3-3363-916b-e4b056dd10e5 | -6.21101 | -55.64228 | 2026-08-22 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 44c838b4-e143-3b23-b965-211bfeb4c8dc | -12.76339 | -48.40194 | 2026-08-22 04:27:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7d498791-63ac-3220-82e0-a5954723fbb1 | -6.78875 | -59.41597 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 117.8 |
| c16002d3-56d2-3bfd-a2e0-5f6d286124e9 | -8.52637 | -54.82146 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| a363f9a4-47f1-36a6-bf66-a87e637f80c4 | -12.28304 | -43.15289 | 2026-08-22 04:27:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 60b7454d-7a51-36b9-9f1f-4940889bf792 | -6.43576 | -54.95852 | 2026-08-22 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 53f6565c-d7e1-3518-ab8a-80fbff374827 | -6.25764 | -55.41159 | 2026-08-22 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6503cd4d-a9df-3e16-9a0c-40e056da5287 | -12.82573 | -48.45955 | 2026-08-22 04:27:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 615c39a8-14f8-30a2-8d54-14dd7b4a0a2d | -6.79722 | -59.42197 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| df98221d-9a8a-3775-85d6-2c74a79f6137 | -9.44713 | -51.64297 | 2026-08-22 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 076d55d0-d207-37f7-9a55-7573055d7156 | -10.30797 | -48.22606 | 2026-08-22 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b6adb07a-bee4-3436-9c93-bac69e5e64ae | -14.1391 | -48.06531 | 2026-08-22 04:27:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 889c8c66-ca35-3f00-9259-6721414399ca | -9.17675 | -59.46638 | 2026-08-22 04:27:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 85074b98-c9f2-3626-a5b1-0abea4b7c099 | -6.88573 | -59.43169 | 2026-08-22 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cead29b1-c816-3009-93fd-e52dd76638b0 | -16.50104 | -55.19017 | 2026-08-22 04:29:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| a79a41bc-6b8f-387d-8644-6a76c51d3464 | -20.43911 | -46.48218 | 2026-08-22 04:29:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README31.md)
