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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a7b87ca9-310c-3973-9be8-d2d6e939e5be | -12.2743 | -48.144699 | 2026-10-09 00:06:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cddb35b9-e700-303a-b7de-d3f0a50f30b9 | -1.7749 | -55.017601 | 2026-10-09 00:06:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca0d7f64-7741-3ab2-8b3c-c9f67289308f | -1.7364 | -52.233898 | 2026-10-09 00:06:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27ad4cc0-67a0-3b6b-8eb2-be7746bbc528 | -6.9309 | -46.584599 | 2026-10-09 00:06:00 | METOP-B | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 23042def-48f1-3c07-b42a-79763ed40756 | -14.9725 | -47.542801 | 2026-10-09 00:06:00 | METOP-B | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 302a447a-0323-3924-8dae-d45696f198d2 | -9.1226 | -45.842499 | 2026-10-09 00:06:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 36ad41dd-c622-3c91-9b6c-da98cd0c6874 | -9.2252 | -45.661598 | 2026-10-09 00:06:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a4d08445-0772-3356-8e38-f099297ac30e | -4.068 | -59.8214 | 2026-10-09 00:06:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9a38ff55-9c20-3217-bb78-03d0041893ec | -2.9696 | -54.113899 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23766fa7-0a16-3564-a760-e8ac2e314a2b | -12.031 | -43.453098 | 2026-10-09 00:06:00 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bc70e5fd-ef3b-3c52-8973-6d0cb7bd3c34 | -2.5078 | -56.143101 | 2026-10-09 00:06:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8ec9128-304d-37c3-9362-5935ebb8e8d6 | -11.1965 | -45.3036 | 2026-10-09 00:06:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e9ffa505-80a3-3a6f-a44f-48186635c397 | -2.2527 | -45.430099 | 2026-10-09 00:06:00 | METOP-B | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0971588b-5944-3d2d-830e-ff67a45ec9ce | -11.4115 | -46.686901 | 2026-10-09 00:06:00 | METOP-B | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 76db40f3-e6b6-3777-88db-9f1778243b29 | -2.9858 | -54.140701 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f9ee204-0b14-38ac-b033-fc4bd85e94c8 | -2.4714 | -56.071098 | 2026-10-09 00:06:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f265cda-c8ce-38d3-83a2-40265c71d66c | -13.4963 | -44.358101 | 2026-10-09 00:06:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 193056b1-dca3-3f82-91b5-39e1cf72534b | -2.2199 | -55.4478 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0e2ef82-2b5a-3615-8ac9-f1f24234f186 | -2.9806 | -54.071301 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6bb0042-38a7-3044-bc94-314d4aba6a6f | -5.9841 | -55.344799 | 2026-10-09 00:06:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 637a3966-27cf-3ee1-89bc-04bb37017f14 | -11.417 | -47.578999 | 2026-10-09 00:06:00 | METOP-B | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 40a84ba2-02cd-3436-8052-efa82cb100b8 | -10.7376 | -48.550999 | 2026-10-09 00:06:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6e2f2c08-c027-3b8c-9252-98219b924aa2 | -5.9493 | -55.3255 | 2026-10-09 00:06:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4a0db84-406c-38b3-b537-fb62cfff7a33 | -5.9255 | -51.825001 | 2026-10-09 00:06:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81f0ede4-4c10-3484-98dd-1759286671bf | -3.536 | -54.678299 | 2026-10-09 00:06:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8bf2b4b-641d-34d3-9089-8a6cae25ac74 | -2.8857 | -54.152302 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5502419-ad48-36fc-a803-7415f7d7800a | -11.8582 | -43.595299 | 2026-10-09 00:06:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 57f50260-c6b6-3463-8674-205f0e381e46 | -3.306 | -54.010399 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d6aa1e0-7d44-35d4-88b0-a3fe3c81fec2 | 2.4498 | -50.813202 | 2026-10-09 00:06:00 | METOP-B | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 007e611f-b08d-3282-983b-ba148958f0ea | -2.5721 | -56.155998 | 2026-10-09 00:06:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e109ca4-bb38-311d-9661-ad7b2ba27583 | -4.5418 | -47.050301 | 2026-10-09 00:06:00 | METOP-B | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 003dbe62-5874-32e3-bf6b-1efa3744ebda | -7.516 | -47.337002 | 2026-10-09 00:06:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8390cf16-f133-3ccb-b180-c118b9395ff0 | -2.9815 | -54.121399 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75a3c296-b391-38f7-b525-ae6d45009e51 | -6.9811 | -47.659901 | 2026-10-09 00:06:00 | METOP-B | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 335365ad-3dd0-3c5e-bdc9-ad085f81fe3a | -16.5912 | -46.756001 | 2026-10-09 00:06:00 | METOP-B | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1025f77a-1ea0-34a1-9cd0-faebded44f16 | -3.3947 | -50.217602 | 2026-10-09 00:06:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 541077f2-1b42-3670-a21c-8d9fd09970b3 | -6.9151 | -44.5653 | 2026-10-09 00:06:00 | METOP-B | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e9741a12-9343-38f0-88e8-6c0e0907eb51 | -15.3447 | -42.780201 | 2026-10-09 00:06:00 | METOP-B | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 536cb7d4-32d9-33e1-b2f9-cc2e9f248705 | -5.391 | -44.177601 | 2026-10-09 00:06:00 | METOP-B | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d896534e-90d5-3251-bc61-94f37424ee17 | -6.1286 | -55.6852 | 2026-10-09 00:06:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c19fe7f-3c51-309f-b156-fb216d618123 | -4.9825 | -44.986198 | 2026-10-09 00:06:00 | METOP-B | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2eeb7d36-9d10-3a0c-87f2-42a6984b9c93 | -3.4278 | -56.928398 | 2026-10-09 00:06:00 | METOP-B | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2dc4266b-cc3f-3bbe-a24e-406802edb632 | -9.0498 | -47.732899 | 2026-10-09 00:06:00 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d2896863-6ace-3d20-bc84-dbae4151c234 | -4.2644 | -46.291801 | 2026-10-09 00:06:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 587d26b7-70dd-3b3b-8fea-3fa0ff19ab07 | -3.2732 | -54.047798 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 406a0b41-9d8e-3965-b7b0-d31b7cf8895e | -12.3002 | -47.059898 | 2026-10-09 00:06:00 | METOP-B | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 997b0fc8-43de-3522-9f90-e7af93f5a3ee | -7.4513 | -42.827702 | 2026-10-09 00:06:00 | METOP-B | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 64a73826-7ce9-3e00-8780-83c9caeb9192 | -2.0811 | -46.567799 | 2026-10-09 00:06:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8d0211a-b6ff-38d3-8cf6-7e4d9d24722b | -4.6435 | -50.962399 | 2026-10-09 00:06:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ffea9ffe-090d-3e81-b431-a6b36589028d | -6.5086 | -55.314701 | 2026-10-09 00:06:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec063538-dff2-38a3-aab6-1b680ff698a7 | -14.1766 | -48.659698 | 2026-10-09 00:06:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8854c9fa-1aa4-3fa1-8bfd-53278def28e8 | -7.5144 | -47.329899 | 2026-10-09 00:06:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0461685e-5b22-3497-9d85-5156f06068dd | -13.7553 | -43.616901 | 2026-10-09 00:06:00 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7147f969-c99c-3ab6-93fd-2a4692cae8ef | -2.0633 | -56.858601 | 2026-10-09 00:06:00 | METOP-B | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a6f2502d-bf32-3b3d-bbe7-71b227a0e80b | -5.9423 | -55.340302 | 2026-10-09 00:06:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3acde095-3ec0-3b9a-8960-35cd2c218e72 | -15.103 | -43.631001 | 2026-10-09 00:06:00 | METOP-B | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 4a227517-a192-3bbb-b1d1-b8a0db597649 | -8.9811 | -45.900101 | 2026-10-09 00:06:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| daecfa65-438a-3ce1-9f83-7dac54976e57 | -3.0791 | -53.960098 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a217fa12-ff5c-35dc-ae32-23def03e54f7 | -3.3039 | -54.6954 | 2026-10-09 00:06:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8c11c9a1-45ab-3ae1-8727-249ad3981345 | -14.8814 | -50.295399 | 2026-10-09 00:06:00 | METOP-B | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 77e5040b-c860-3b24-a51e-6fa583a029c3 | -11.1886 | -45.313801 | 2026-10-09 00:06:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8e541ddc-cf92-3d63-9a11-68dd8a826da7 | -5.9673 | -55.361698 | 2026-10-09 00:06:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52d6bd00-3125-35fb-a8e5-32a0fee098c5 | -11.7887 | -45.5863 | 2026-10-09 00:06:00 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 83d23656-c229-399a-9842-f1f53b388b98 | -13.5021 | -44.382801 | 2026-10-09 00:06:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ec9f9152-ad90-34a9-9774-5aa78c778a69 | -2.7336 | -54.115101 | 2026-10-09 00:06:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db2d6b01-cedf-3a73-91cc-34f16d1e499f | -2.9351 | -54.051201 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| acff7809-0b87-31f7-a9ae-0358e8a12341 | -1.0528 | -53.587601 | 2026-10-09 00:06:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c125174a-6563-3e5b-ae4c-1baa3c4ae095 | -3.5313 | -54.6572 | 2026-10-09 00:06:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10cea5f2-cd6f-3e4d-b52e-8ccf62b924ad | -5.7045 | -49.079498 | 2026-10-09 00:06:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae5d8b09-f6f1-3968-8b16-e3dc0ccf13eb | -3.5353 | -49.4701 | 2026-10-09 00:06:00 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ecf4855-c360-3ad6-90f0-c40e556769a5 | -3.1103 | -53.777 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3f0884c-17dd-32b6-969a-1397a2d9714e | -2.9904 | -54.069099 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76195a6f-e6e1-3b16-b9c3-9dd657efc5a9 | -7.2093 | -55.153999 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75ad34b8-ba02-3fa5-aa4f-cb949750a7ab | -11.7947 | -46.784599 | 2026-10-09 00:06:00 | METOP-B | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 37131d96-81cc-3a6a-a0f3-6012cbc1f7e5 | -7.4737 | -42.834999 | 2026-10-09 00:06:00 | METOP-B | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2d324612-175b-3a04-836d-489942bd05e9 | -6.9179 | -46.483501 | 2026-10-09 00:06:00 | METOP-B | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b705605d-6045-38dc-9904-b2b113d6a7ff | -1.5921 | -47.3592 | 2026-10-09 00:06:00 | METOP-B | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0f06d11-3a6c-3510-b043-c4613f3e35c2 | -6.0318 | -53.481998 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e830c94-0481-3ce2-b0e1-90fd230a4df9 | -11.5827 | -43.653099 | 2026-10-09 00:06:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 58307726-2ca8-394f-95b9-605a6296acd0 | -12.0287 | -43.4436 | 2026-10-09 00:06:00 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0d09f4db-0f59-3dff-b66f-67255ceeb189 | -3.0135 | -54.0341 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82b9ecb0-ba37-3afd-baa3-a436024ffd53 | -6.7219 | -48.107601 | 2026-10-09 00:06:00 | METOP-B | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 0fafa742-c611-30b5-adbd-a1c079065f86 | -2.9981 | -54.0574 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f184dd7-23d8-38e1-a1f5-ab495b20bc8a | -3.2591 | -54.030701 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d663a53-e09e-3a1c-88cd-60453ede51b3 | -6.6808 | -44.314499 | 2026-10-09 00:06:00 | METOP-B | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e5b39664-9b41-3fc4-842c-656ef50f1065 | -3.1685 | -50.5858 | 2026-10-09 00:06:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c7c8961-364b-3d9a-b5a5-0922fbfa4863 | -13.4569 | -47.3004 | 2026-10-09 00:06:00 | METOP-B | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 381fe415-05ad-3fac-a3d2-89dc731712af | -6.9305 | -43.669201 | 2026-10-09 00:06:00 | METOP-B | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7774ed3a-5983-3a82-aea0-9f75164e5469 | -7.751 | -49.1987 | 2026-10-09 00:06:00 | METOP-B | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 45a4234d-a39b-346f-8dcb-8b994c7133b3 | -5.3794 | -45.940701 | 2026-10-09 00:06:00 | METOP-B | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e40f97a2-a141-32cf-8357-77e45015629c | -9.2871 | -47.4147 | 2026-10-09 00:06:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fc88ad69-48fb-357f-8e30-ca49926c78a9 | -4.1173 | -59.862301 | 2026-10-09 00:06:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c0376a83-2670-31fc-a580-cdc3548104a9 | -3.2017 | -58.8237 | 2026-10-09 00:06:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c7da85d2-ed6e-3dae-ae31-9040b070b5e8 | -8.2975 | -45.711498 | 2026-10-09 00:06:00 | METOP-B | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| abba9742-4443-3273-ad39-ba5b8b205362 | -2.4993 | -56.1049 | 2026-10-09 00:06:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5130bdcc-a0ed-343c-8293-966027978357 | -10.4605 | -47.863098 | 2026-10-09 00:06:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3fa51826-6ec3-3a80-932c-b1285bc45f78 | -6.4394 | -55.038399 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25e18a00-b341-3da6-a180-e48c068eef7a | -3.0275 | -54.050999 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9417d7e-bc7e-3774-8699-21d343ea9b3c | -18.0791 | -42.268501 | 2026-10-09 00:06:00 | METOP-B | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1a0d3f2b-40db-3ba9-8ca4-35ea2c767336 | -11.2278 | -45.304501 | 2026-10-09 00:06:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README7.md)
