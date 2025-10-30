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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c6c7ca6e-9adf-3e0b-adce-464ad050ffc5 | -9.80952 | -47.5805 | 2025-10-30 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d24361c1-a4cb-3b56-befa-5786085b479d | -7.95908 | -46.73555 | 2025-10-30 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3e3b2991-13d0-346e-9052-f08daf11a1a9 | -7.96568 | -46.71528 | 2025-10-30 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2aa6128d-dd42-393e-ad57-6d56e49b02af | -4.68417 | -46.53745 | 2025-10-30 04:25:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 32a0a24a-f866-34eb-b679-b6b22f8934dd | -10.77593 | -47.82761 | 2025-10-30 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 440fd204-8334-3530-b5f9-324539ef6cd9 | -7.62305 | -43.61389 | 2025-10-30 04:25:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0576fab4-eea7-3703-b114-becddd5d9925 | -7.76334 | -46.49107 | 2025-10-30 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 717b6d73-096d-3d55-ade6-1cc3f945eaac | -7.0177 | -46.43657 | 2025-10-30 04:25:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f4c9da06-dfda-3620-b269-18a36a780763 | -5.43401 | -45.33953 | 2025-10-30 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 94af6785-c74d-3433-bf6c-4e10a9628ae4 | -5.38065 | -47.20329 | 2025-10-30 04:25:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 48507272-7ef6-3d15-9876-2734dc0c138e | -5.80187 | -40.82048 | 2025-10-30 04:25:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f0699b25-5170-3d81-a21b-a89804fc3adb | -9.82526 | -47.69483 | 2025-10-30 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 93d45756-68d0-39ab-a643-31f1b1f1f2c2 | -4.8922 | -45.71811 | 2025-10-30 04:25:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e313a512-cf2a-323a-98a9-07ec7354cc20 | -6.13089 | -41.70596 | 2025-10-30 04:25:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e964db3d-392b-38ce-a3ab-429bcf2ba68b | -8.32741 | -47.93715 | 2025-10-30 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a0f7f404-906e-3a95-9979-8068a8c2351f | -11.1186 | -42.25961 | 2025-10-30 04:25:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9806ad1d-470e-33c2-93c4-2350f030ec14 | -8.52071 | -48.94428 | 2025-10-30 04:25:00 | NOAA-20 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b5efab03-85f0-3e3b-afa0-58770a8d2e26 | -4.69692 | -45.8351 | 2025-10-30 04:25:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4ba2562e-5902-3adb-9b6c-ed33666e3758 | -5.72865 | -39.03742 | 2025-10-30 04:25:00 | NOAA-20 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 946dc46b-1378-3f29-ae18-7cf5c07bd945 | -5.03389 | -43.61113 | 2025-10-30 04:25:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7c96bb28-abaf-34af-88ff-27c898ca543b | -7.29178 | -44.96314 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4447e819-8412-323c-99b1-e4000767bebe | -11.00622 | -41.68201 | 2025-10-30 04:25:00 | NOAA-20 | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8fca0c50-dec5-317e-917f-d2d8f74224b5 | -7.79133 | -46.42097 | 2025-10-30 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 666f1c99-6a47-373b-bbc5-14eaed1e4dfb | -7.61724 | -43.5799 | 2025-10-30 04:25:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3fd403c8-2891-3266-88e7-1dd28bb3002f | -7.77765 | -46.48624 | 2025-10-30 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 90242057-70ee-3f35-ae62-4e0377ae0b21 | -9.51868 | -47.86992 | 2025-10-30 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| acfcdf8a-3c93-39c7-b1a2-066f8b3fcc2d | -10.59674 | -47.92887 | 2025-10-30 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dcd746ee-ca6f-34fb-b270-666a2d0bbd3d | -7.35048 | -47.65556 | 2025-10-30 04:25:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4020142c-3eab-3195-abfe-9a10f4c2a6a5 | -5.84406 | -42.76471 | 2025-10-30 04:25:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 7c3d825e-e350-359a-851a-f6af775ef73b | -5.43733 | -45.34004 | 2025-10-30 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 26.7 |
| effdd69f-f5a8-3d51-9d9e-d82ccd777529 | -7.3455 | -47.64372 | 2025-10-30 04:25:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 053f0614-6dc4-3700-82b2-585ba7bb9cc2 | -4.43394 | -48.01358 | 2025-10-30 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9a894e4-6042-33c1-bcfe-f47808543350 | -6.31241 | -42.10434 | 2025-10-30 04:25:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5b4aec7f-3765-3ca3-842a-e7e52d899835 | -10.88117 | -45.07291 | 2025-10-30 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c3db8525-bc30-3a20-9573-cf706c515e59 | -10.76052 | -44.74007 | 2025-10-30 04:25:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0f02332a-9b45-31e5-a68a-7dd05d3cfa55 | -11.05703 | -47.5351 | 2025-10-30 04:25:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0e8a8276-40bf-309d-b0e5-985011317c50 | -7.28035 | -46.06387 | 2025-10-30 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dbab374c-dd94-33eb-b4bd-47182de2463b | -7.29122 | -44.96676 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 09697efe-e661-3f92-9788-429bf7b63456 | -5.03921 | -45.17123 | 2025-10-30 04:25:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0b8e5242-f1d2-3311-aefe-3c82ac5bf8c3 | -6.14188 | -41.71199 | 2025-10-30 04:25:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 6e57b2ed-1b87-3dd4-8bd5-ed978f1b6e74 | -8.32056 | -47.9252 | 2025-10-30 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d4abe918-aec9-3cf7-b39a-d9292fec7c3c | -8.32334 | -47.92933 | 2025-10-30 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 9d2f576d-a959-3e63-8777-16118ffd8b07 | -9.89888 | -47.91342 | 2025-10-30 04:25:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9c182399-6f45-3958-9145-95a2a9955fe3 | -6.17864 | -41.6776 | 2025-10-30 04:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c255b8d5-8b78-39d6-a9e1-82b76b237cbd | -4.25019 | -49.85856 | 2025-10-30 04:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e62b27e-6379-3649-9290-6f9840bdcd65 | -7.81424 | -46.40719 | 2025-10-30 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e5669195-fe5b-32ca-8550-62d74037b12f | -7.61838 | -43.59658 | 2025-10-30 04:25:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6ea3569e-d6c3-320f-a6ca-7133010e548d | -3.81214 | -51.6983 | 2025-10-30 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e5a47144-9ee3-3908-8dbe-b3caf4acd33e | -6.12986 | -41.70325 | 2025-10-30 04:25:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| a21847cd-b4d7-3d0e-9bf6-f1f685142b4f | -4.60423 | -48.74963 | 2025-10-30 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6472e2b0-24fb-378c-ae00-0c78be4f05ec | -8.02198 | -42.51672 | 2025-10-30 04:25:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b586411c-889a-3ada-abc2-4fde43a9a0f4 | -7.32771 | -42.47582 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| e744acd3-5c1a-3623-954a-2261817780e0 | -11.20437 | -47.57014 | 2025-10-30 04:25:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 397133f7-588b-3672-bbd2-47c8a10fbcc6 | -7.30214 | -45.66472 | 2025-10-30 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b172ddf1-bf00-3fd2-a11b-dd4c97ae8b79 | -9.0854 | -47.90202 | 2025-10-30 04:25:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 72ae21d7-8434-32de-a571-e27bf9e6f456 | -7.135 | -44.70521 | 2025-10-30 04:25:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ec351f63-8e77-342c-80c5-f16e9d114968 | -6.40346 | -47.07265 | 2025-10-30 04:25:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c88fda07-48c4-3e58-9a00-b41a7e157ca3 | -7.25983 | -44.93621 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1954c7ff-af60-348f-be15-ed9c95fa8998 | -5.90573 | -47.65461 | 2025-10-30 04:25:00 | NOAA-20 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e8ea6e8a-56f2-369c-857e-ef788378a053 | -8.32916 | -47.92637 | 2025-10-30 04:25:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8f3e39b8-c143-3147-b73c-e3bdb0a2ed4e | -5.76393 | -44.5309 | 2025-10-30 04:25:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 813df5c7-2735-375f-83f3-5bb97976f873 | -10.27631 | -44.577 | 2025-10-30 04:25:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e41f33c9-7e5d-30c2-9a6a-dc45018f03fe | -5.70389 | -43.15599 | 2025-10-30 04:25:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 4.6 |
| e8f4538a-233a-3516-830f-9c59f922c103 | -10.99229 | -47.87741 | 2025-10-30 04:25:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 95d46f5f-27b1-309e-a393-2f1f0280f19b | -5.82571 | -43.09022 | 2025-10-30 04:25:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| c7d21b27-0d91-3c33-a6a9-7311346942d1 | -9.88876 | -47.44603 | 2025-10-30 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e934ccdc-3c33-3a73-88d5-9ec36da0c180 | -6.58027 | -47.5398 | 2025-10-30 04:25:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d5e4b2f0-0bd6-3123-a278-32d900f86c73 | -7.62426 | -43.60582 | 2025-10-30 04:25:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 80ba6403-599c-343b-8009-d0d727a11469 | -10.27573 | -44.5809 | 2025-10-30 04:25:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6a64712e-ef11-3f0c-9f82-bed7f5ccf937 | -6.48468 | -42.21848 | 2025-10-30 04:25:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 9bdb6569-a594-3997-b2ed-565eecbb675e | -4.40888 | -48.95352 | 2025-10-30 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af4b0bd7-ec6e-304c-989c-811362a9bdbe | -7.61019 | -46.7939 | 2025-10-30 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b6f9f617-063e-3843-95a3-3e6b3ad024f7 | -6.09581 | -42.43735 | 2025-10-30 04:25:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 72c058f4-66ce-3bd4-93f8-13e135b8956c | -10.36448 | -44.12737 | 2025-10-30 04:25:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8eb020e8-8be3-39c3-b53d-f0054b1c83d1 | -5.7673 | -44.53144 | 2025-10-30 04:25:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 28e19ed8-99f7-305d-b471-5f6f78448e79 | -4.68797 | -46.36378 | 2025-10-30 04:25:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9a90ba8c-eeb9-35d7-9b4a-5fb8102d81ad | -7.16046 | -39.46378 | 2025-10-30 04:25:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cb8d2a8c-6620-310d-a371-14499254c139 | -7.91761 | -47.27543 | 2025-10-30 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 00d6ebb7-c7a7-38a0-8ddf-1479fd4bc91d | -7.50738 | -46.26272 | 2025-10-30 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e8b8e3c1-4780-364d-a497-1fa4b5fefc2b | -8.5434 | -48.97956 | 2025-10-30 04:25:00 | NOAA-20 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8e2e134b-8b7f-3821-92b4-3a5b1ca9002a | -8.17881 | -45.7048 | 2025-10-30 04:25:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2e52342d-df8b-3d6f-89a3-eff6552f1bd4 | -7.78636 | -46.40953 | 2025-10-30 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 37de00c7-0a1d-312d-98c5-bcad979d25a0 | -6.46317 | -41.65059 | 2025-10-30 04:25:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c1a4e004-fabc-3f1c-9836-7e2ac3ba1c2c | -10.65032 | -47.89078 | 2025-10-30 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8ed252e5-31ac-3de7-8817-9ac12589d5c2 | -11.13526 | -51.07624 | 2025-10-30 04:25:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| ea1ff5e2-a581-3c66-86a3-f4020a164621 | -7.92529 | -45.50198 | 2025-10-30 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5fd4669f-f41c-313e-9322-08c7ecc5a02a | -5.04022 | -43.61599 | 2025-10-30 04:25:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| c66448ed-e552-3337-9506-cae5b712a0a9 | -11.00857 | -47.77553 | 2025-10-30 04:25:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 647044ca-06b7-3ea2-87ab-f8996459d657 | -7.44153 | -47.3396 | 2025-10-30 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 46560d4a-c931-3b13-b9c3-7dd4776a1dff | -7.62375 | -43.58502 | 2025-10-30 04:25:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0909b1da-d034-37d7-9715-49d68750bc81 | -6.44373 | -46.79972 | 2025-10-30 04:25:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b1287a2b-02e7-3f31-9f82-cbda627f1d67 | -5.62211 | -46.15126 | 2025-10-30 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aa555225-e802-3dc6-bc5e-d6a5926bc91e | -4.33062 | -47.89283 | 2025-10-30 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 68ddcb1d-d86f-3a59-b8f8-3ee83fd6d9e4 | -10.86092 | -47.61434 | 2025-10-30 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d5eae53b-17c0-30e3-95c0-4480aa251847 | -6.78035 | -42.48723 | 2025-10-30 04:25:00 | NOAA-20 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c31a1ed1-9726-3895-b1f1-246ea563a6af | -6.01806 | -41.977 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 44f3743d-7a5e-3c8d-9133-1f2a175b2afb | -4.231 | -55.66617 | 2025-10-30 04:25:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7b69ff4e-2f2b-3d64-bb5a-5825eca461cb | -7.30413 | -44.97247 | 2025-10-30 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a3bd7e2f-1f0d-3e43-b176-06f0de165f70 | -5.0333 | -43.61491 | 2025-10-30 04:25:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 81ed229a-5b60-3383-9680-c20b2c972148 | -5.43844 | -45.09395 | 2025-10-30 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README53.md)
