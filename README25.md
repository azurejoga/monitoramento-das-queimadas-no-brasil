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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b7ffc428-4cb9-39f6-b7cf-608152f4cc39 | -6.96114 | -42.83607 | 2024-12-17 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e732d258-ecbb-3aae-bd44-d0017ee92f05 | -7.86338 | -43.08698 | 2024-12-17 04:46:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 78cff233-1a5d-395a-af3d-e833a160f971 | -6.93347 | -43.51009 | 2024-12-17 04:46:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0e426fb5-75ff-3971-9b98-416bf8078ab3 | -13.61877 | -45.58861 | 2024-12-17 04:46:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dbeb39c5-b9bd-3566-abcc-4925a837885e | -7.86298 | -43.08985 | 2024-12-17 04:46:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 24d73204-e3b9-315f-840b-3c5c6ae7ff9b | -6.95644 | -42.8324 | 2024-12-17 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5d064469-0177-3e9e-836d-205a9e90f4cb | -6.96872 | -42.83375 | 2024-12-17 04:46:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| aecba563-1309-3a3a-933b-799b3c2c7e39 | -6.97723 | -42.83242 | 2024-12-17 04:46:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0cb225f1-c6db-3a19-859f-6546e3342a40 | -6.95428 | -42.82562 | 2024-12-17 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 562b62b3-fd33-3b17-85ac-1b1eea2cdf23 | -6.95811 | -42.83521 | 2024-12-17 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 58d4a34d-3a20-3fa1-9a8f-f170f24b9df9 | -6.96914 | -42.83081 | 2024-12-17 04:46:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8c454dbe-908e-3138-8d23-003f2946fc5c | -9.22566 | -47.56666 | 2024-12-17 04:46:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b09da61-8cd1-3e9e-844e-74d7f9e359cc | -6.95853 | -42.83226 | 2024-12-17 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8df59402-e7c4-3933-a863-5fec220942be | -6.95684 | -42.82944 | 2024-12-17 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fc45adff-30c8-32c8-84b6-4351d698189a | -6.99354 | -43.55923 | 2024-12-17 04:46:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 49576a2d-cb97-309e-940f-4f66a2f3d872 | -6.98869 | -43.55851 | 2024-12-17 04:46:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 48d168e8-e551-3445-84db-97b8ac5c23f3 | -6.96411 | -43.00305 | 2024-12-17 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b896c346-32d0-38c1-b5fe-4aa836c98b13 | -6.95386 | -42.82858 | 2024-12-17 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c63b0d9c-1554-3f35-8d70-9505f1397faf | -6.97173 | -42.83466 | 2024-12-17 04:46:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e3ef07e1-6019-3a80-9463-0e1b2f5800c3 | -6.96703 | -42.83096 | 2024-12-17 04:46:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3a3eaa91-6d4d-32d1-a39b-914311348def | -12.41098 | -43.79934 | 2024-12-17 04:46:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b5f78baf-e5d4-3a5f-b43f-636eb370e6d3 | -6.92373 | -43.50878 | 2024-12-17 04:46:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 2063b3a1-f341-3b25-8212-293b44758303 | -6.95937 | -42.82639 | 2024-12-17 04:46:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e50a98c9-0872-3ee8-a428-feb1e42aa1c8 | -6.9809 | -42.80564 | 2024-12-17 04:46:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| e3046b01-d21b-3321-8313-e10c395d1307 | -6.944 | -47.79542 | 2024-12-17 04:46:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eeac1e42-b89e-3cb8-8bdb-118b463864e9 | -6.96234 | -42.82726 | 2024-12-17 04:46:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ff5d42c7-2dac-3d92-a5a3-4a8583abdc61 | -6.92935 | -43.50413 | 2024-12-17 04:46:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 0596dd7b-67e6-3db7-a48e-2c9fdefe6fb6 | -6.86399 | -44.77116 | 2024-12-17 04:46:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 05170b3e-75f2-3e23-86ab-3a8b166bd687 | -6.96405 | -42.83007 | 2024-12-17 04:46:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2da70344-d2a5-3da2-9b2a-52e533f0ea9e | -6.9166 | -43.52409 | 2024-12-17 04:46:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d5378db0-6094-399b-952c-c7bc3f677876 | -7.41267 | -44.72111 | 2024-12-17 04:46:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e5927a08-1203-3963-b8e9-a01eca483058 | -6.96154 | -42.83313 | 2024-12-17 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4e3aae49-a3ee-3e16-bf20-0b44e84dee36 | -6.64032 | -47.35308 | 2024-12-17 04:46:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5734440a-0fc3-3c6b-8731-67a78f1f6825 | -6.97213 | -42.83171 | 2024-12-17 04:46:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cd7c9b97-ccd8-30b0-8950-6a7f49c0da51 | -6.95724 | -42.82648 | 2024-12-17 04:46:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c1ca75b6-a94f-3bb0-973e-3f8334b483ef | -7.41203 | -44.72559 | 2024-12-17 04:46:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 14766c5f-3505-37e1-b8b9-13b06b65db0c | -6.92859 | -43.50948 | 2024-12-17 04:46:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 46.3 |
| ad0cd352-fa66-31d0-afe4-cf50833305a4 | -15.10584 | -59.64481 | 2024-12-17 04:48:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7cce17e-6115-389c-b6e0-b386755e1f98 | -19.09555 | -52.86312 | 2024-12-17 04:48:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 16eeda49-4999-3103-84cc-97b77788ce34 | -19.08482 | -52.85816 | 2024-12-17 04:48:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e54b57c7-9766-3878-b6c5-5c01150aca22 | -19.06459 | -52.85479 | 2024-12-17 04:48:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 245c3a21-66f8-374e-9130-17786eb3bbb7 | -19.08937 | -52.85823 | 2024-12-17 04:48:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2ac27376-156b-3dc2-9042-bf4b812d38c2 | -19.09218 | -52.86256 | 2024-12-17 04:48:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 18.8 |
| e14f7897-303d-3344-af1c-fc5e2cc9dc01 | -18.89922 | -56.05053 | 2024-12-17 04:48:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.1 |
| d373663d-ef1c-32ff-9934-363570d70f68 | -19.06402 | -52.85855 | 2024-12-17 04:48:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| efd91293-333b-34ab-969f-cef28d941af2 | -15.87751 | -53.27575 | 2024-12-17 04:48:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 086133a7-e7d5-35f7-a859-76fcf066dfed | -17.26333 | -51.05695 | 2024-12-17 04:48:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1f253513-6f4b-370f-80ef-9b96fc303374 | -19.09162 | -52.86631 | 2024-12-17 04:48:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 92391e88-b37a-31ed-a773-8fcc2000aace | -18.89809 | -56.04678 | 2024-12-17 04:48:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 5c4885d4-36f2-344c-a9aa-227b06fcd3d6 | -15.09238 | -59.64843 | 2024-12-17 04:48:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d80a7d19-d9b3-3d34-88cb-442dfb985aac | -15.24172 | -59.91186 | 2024-12-17 04:48:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 643a58fe-2b17-32c8-b79c-5208255155d9 | -19.09274 | -52.85879 | 2024-12-17 04:48:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 18.8 |
| aa978732-7724-339e-8b31-e766a090a8cf | -18.01726 | -54.42912 | 2024-12-17 04:48:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 611d4230-37fd-3eef-8546-90049dc9406f | -15.07837 | -59.65013 | 2024-12-17 04:48:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4ff353d-6958-336c-8c91-4a507328cdd3 | -15.0792 | -59.6457 | 2024-12-17 04:48:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a5597b0-c42b-3787-976e-092e4a3b786e | -15.2364 | -59.91552 | 2024-12-17 04:48:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 640a6adc-ec03-3ad3-bd11-2b14e859cd2f | -18.89743 | -56.05071 | 2024-12-17 04:48:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 6b484e0c-4bb9-3593-9cf4-751b268a5a15 | -19.05728 | -52.85745 | 2024-12-17 04:48:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9ffefc1f-6991-3387-8d92-f966c0051eae | -19.05671 | -52.86121 | 2024-12-17 04:48:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5a486d36-feda-3c52-ac7e-5d9e960727fd | -19.08881 | -52.86199 | 2024-12-17 04:48:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7519e048-6bd6-325c-911f-850cb5df6579 | -19.06796 | -52.85535 | 2024-12-17 04:48:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 241dce96-658f-34a2-9f76-96cf834cec22 | -15.09759 | -59.64488 | 2024-12-17 04:48:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7227397c-b993-3937-ba81-8796dcb701a5 | -19.06122 | -52.85424 | 2024-12-17 04:48:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 567bc740-cd44-3858-9e5a-c0340ed873c0 | -15.07315 | -59.65366 | 2024-12-17 04:48:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fbb3ed69-b902-3b13-8f2a-aeb014108c85 | -15.08716 | -59.65196 | 2024-12-17 04:48:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8fc6d0f9-3ec0-3137-a231-8263084272a2 | -19.09499 | -52.86687 | 2024-12-17 04:48:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 09ecc5fa-e709-324e-8bd8-6bc4ab1c5b21 | -15.52991 | -59.08411 | 2024-12-17 04:48:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a84a2310-65c6-3746-bada-f6e07aeabecb | -15.10199 | -59.64576 | 2024-12-17 04:48:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb5dccc9-6f9b-3abf-bbfa-69c4a244ee51 | -19.08544 | -52.86143 | 2024-12-17 04:48:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c941e48b-a6ac-3e0d-afe3-cb311ee2c797 | -15.24087 | -59.91642 | 2024-12-17 04:48:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69433620-2838-3d1c-8922-c663a97044ac | -19.06008 | -52.86176 | 2024-12-17 04:48:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9cb80116-e8bf-3980-84b3-330d5b28eac7 | -18.90153 | -56.04742 | 2024-12-17 04:48:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.6 |
| d28b25d9-289c-3266-b60a-5e3cb051a333 | -18.90087 | -56.05135 | 2024-12-17 04:48:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 6c9f774e-a2c4-3b50-ab48-75620080c8cb | -18.89989 | -56.0466 | 2024-12-17 04:48:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.1 |
| 111c96d7-cf7b-3b55-ad33-dfdfaf90ebe8 | -15.08277 | -59.65104 | 2024-12-17 04:48:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 917bec83-aa9d-3fbd-ad3c-7be36c9b768d | -19.23842 | -52.34803 | 2024-12-17 04:48:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| acd56d0c-c620-3638-9e95-44c037a64377 | -19.086 | -52.85766 | 2024-12-17 04:48:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7e89b325-7fa3-349f-aa15-de434e76ba0c | -19.08425 | -52.86192 | 2024-12-17 04:48:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c8213a5a-29da-3aae-930a-a8f92a4137f7 | -17.70099 | -54.0862 | 2024-12-17 04:48:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 52160bbc-ea77-3561-b624-5c38bba84520 | -19.08994 | -52.85446 | 2024-12-17 04:48:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7f2bbb20-48ed-3185-916f-88f52c3396cd | -17.72288 | -54.0895 | 2024-12-17 04:48:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.3 |
| acb7f029-f796-359c-99ff-5a7a11ef9dc3 | -16.47083 | -52.33585 | 2024-12-17 04:48:00 | NPP-375D | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| effcdd51-97ec-3722-9972-8004daf679b5 | -19.16337 | -54.83598 | 2024-12-17 04:48:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 865c8e26-0e90-3ec5-9bfe-14e82dc5abd4 | -15.0748 | -59.64482 | 2024-12-17 04:48:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0e01574e-5d87-3bd5-adba-01c3b8a6d530 | -19.06065 | -52.858 | 2024-12-17 04:48:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 40d4d169-a66b-39ab-a3e3-ec69004b32e8 | -15.87808 | -53.27216 | 2024-12-17 04:48:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 589bba9f-da5a-3b74-8c02-1af8732ff756 | -17.26685 | -51.0575 | 2024-12-17 04:48:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fcbb605e-9ea1-3ab7-ac1e-9a398771d5e8 | -19.07134 | -52.85591 | 2024-12-17 04:48:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2c4fe255-a97f-361b-b73e-379ae065e412 | -15.09156 | -59.65286 | 2024-12-17 04:48:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cc124e20-b0ba-32f1-812b-3e3c0e045200 | -15.07397 | -59.64924 | 2024-12-17 04:48:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1a2c2b28-98c0-390d-819b-98d808e4ca90 | -5.0936 | -43.9176 | 2024-12-17 04:50:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 96.4 |
| b3f5f31e-2cde-3aee-8618-74bb48984a44 | -6.9349 | -43.4934 | 2024-12-17 04:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 750dc961-205c-3b61-b1b7-2b6142380fb2 | -3.2968 | -53.3749 | 2024-12-17 04:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| d1904652-ec85-3e44-a4a6-b2f99275473f | 4.4435 | -60.9846 | 2024-12-17 04:50:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 611599a3-2d9a-34c9-aab3-97950dce124d | -6.9346 | -43.5168 | 2024-12-17 04:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 5f69992e-4a09-3a28-b726-7cabfeac4ad4 | -5.0938 | -43.8945 | 2024-12-17 04:50:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| ef04ff61-a1bf-3f8c-b8da-40d3dc8c1636 | -22.67263 | -42.85222 | 2024-12-17 04:50:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 97ff5d98-6188-371b-953d-1e426dec9172 | -20.18323 | -54.99233 | 2024-12-17 04:50:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b8fa49be-9246-320c-b751-4af53b1edcf3 | -23.44765 | -46.06514 | 2024-12-17 04:50:00 | NPP-375D | GUARAREMA | SÃO PAULO | Brasil | 3518305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 69128433-97cb-3d4a-ae28-1fa5647b2706 | -20.4781 | -53.67598 | 2024-12-17 04:50:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README26.md)
