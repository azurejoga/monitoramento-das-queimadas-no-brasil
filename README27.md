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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8176e57a-ca85-3ba8-9828-b012d23ac71d | -18.05769 | -52.98412 | 2024-12-12 04:42:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 89390e6a-4007-32f1-b3b2-1592355a9de5 | -15.07835 | -59.63609 | 2024-12-12 04:42:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 78a0b261-148d-335d-9c42-be3879825859 | -18.05494 | -52.97985 | 2024-12-12 04:42:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ad4ab96e-7949-3eb7-8077-0f51a3a63b09 | -15.02518 | -57.61342 | 2024-12-12 04:42:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 605eabac-e1eb-3fda-b27a-610ec4534913 | -14.75016 | -52.65345 | 2024-12-12 04:42:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 04963770-1b8a-3054-874c-a47babef2844 | -15.07949 | -59.62392 | 2024-12-12 04:42:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c62612c7-ad38-3389-88d6-b2c1ce4224e1 | -18.0516 | -52.97926 | 2024-12-12 04:42:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0abcc4d7-eeae-3faa-b7ae-b3301b7716f4 | -18.49493 | -55.13334 | 2024-12-12 04:42:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 55deda0d-b02d-3727-a724-8b7574d67702 | -15.96332 | -57.16047 | 2024-12-12 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e37e11dd-8caa-3fc6-882d-e3104c965a47 | -19.35917 | -49.19448 | 2024-12-12 04:42:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e1d3e3c9-6298-3bfb-b10b-4e1d0b4513a7 | -19.01991 | -57.62251 | 2024-12-12 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 35ea2f4a-e323-3695-8db9-6117fad9467d | -14.75968 | -52.65887 | 2024-12-12 04:42:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2ef13e7a-97d9-320f-af8e-046c1619f788 | -14.7581 | -52.64725 | 2024-12-12 04:42:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ef3007d-337f-315b-a569-ec8c54724717 | -15.96544 | -57.15993 | 2024-12-12 04:42:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dd8c102e-02f0-3020-9bf0-a3c52d6c3fec | -17.29977 | -53.77118 | 2024-12-12 04:42:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 01dd5168-1fca-3f3b-922b-276fbf40d8f9 | -14.75076 | -52.64977 | 2024-12-12 04:42:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 95306d2a-6670-378d-bbfc-0428b63b3ae9 | -15.08166 | -59.61932 | 2024-12-12 04:42:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9af60e5a-0035-33e5-baa4-f3dc10757858 | -14.75473 | -52.64668 | 2024-12-12 04:42:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e6d1895a-80c5-391e-aa53-2ca0ee6b66e9 | -15.07904 | -59.6531 | 2024-12-12 04:42:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0861df61-c75f-3dd8-99ed-c698ac59aabf | -15.09077 | -59.65049 | 2024-12-12 04:42:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1b4b708d-d781-3f58-9308-d7a5056b8112 | -14.91399 | -52.87058 | 2024-12-12 04:42:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bada0dd7-76b8-3df7-bed7-62d3ee61d33d | -14.74837 | -52.66448 | 2024-12-12 04:42:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e6712821-08ba-330b-8c9c-84ed4eddf08f | -20.73063 | -54.42076 | 2024-12-12 04:42:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8e7550f3-9b41-39ca-9463-dcb00e574ab0 | -18.05434 | -52.98353 | 2024-12-12 04:42:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef4ea06e-6fb6-3e87-9c6f-10a53ca5e1d0 | -15.08118 | -59.64181 | 2024-12-12 04:42:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5cfdabc5-ac31-30f0-9c38-dcf38b52524a | -17.30041 | -53.76733 | 2024-12-12 04:42:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0c59f656-f95e-3ae8-aaf7-978fa5156b9d | -18.051 | -52.98294 | 2024-12-12 04:42:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bed05d5e-8ea4-356d-8552-0328f0ee1910 | -15.08655 | -59.62029 | 2024-12-12 04:42:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7abf0d08-b70e-3a2d-82ce-de2a3a808e9e | -15.07012 | -59.65196 | 2024-12-12 04:42:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7ff5b2f1-50cc-34c7-a7b6-dc7e94e85edf | -15.08589 | -59.64944 | 2024-12-12 04:42:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dbedf5f6-8a03-300b-9088-0c6f896775d5 | -15.08212 | -59.64273 | 2024-12-12 04:42:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 686dc87b-09b4-3e8d-bb58-a8f607f6936e | -17.29636 | -53.7706 | 2024-12-12 04:42:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| db165231-a2d1-37bc-afd7-35c978680be5 | -20.17563 | -54.98986 | 2024-12-12 04:42:00 | NPP-375D | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dd39a384-5ca8-3a4d-8f02-efb8985718a7 | -14.91338 | -52.87431 | 2024-12-12 04:42:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bdc71555-6bd0-3c63-b0c0-880db9a18614 | -15.07415 | -59.65206 | 2024-12-12 04:42:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 78ee2942-e474-3814-85dc-73c66743c5d5 | -15.06817 | -59.65672 | 2024-12-12 04:42:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cfe64a18-44f4-3b3f-99d0-d30aaa96b966 | -17.74659 | -56.323 | 2024-12-12 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 21cdc632-bd3c-3290-83dd-520d68246879 | -18.04922 | -52.99395 | 2024-12-12 04:42:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d04897bd-7afb-3445-881f-41d06e8df1e7 | -14.76028 | -52.65514 | 2024-12-12 04:42:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e9bdab34-63b3-3d20-946d-a55e9024dfd1 | -15.07629 | -59.6408 | 2024-12-12 04:42:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2c96b231-ddc6-393b-9e6b-c861e00cffdb | -15.09299 | -59.63919 | 2024-12-12 04:42:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 77a2f03a-e078-33b8-882c-da748eec72e7 | -15.02492 | -57.60656 | 2024-12-12 04:42:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a554d185-1b04-34ea-aaa2-5c622b893838 | -18.04529 | -52.99703 | 2024-12-12 04:42:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| faaae814-639b-3df9-aae4-4592ba5390a5 | -14.75255 | -52.63876 | 2024-12-12 04:42:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 00dae702-5359-3bef-9d6a-27ca2524bc5d | -17.30319 | -53.77177 | 2024-12-12 04:42:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ed24a526-d520-30ad-b8da-977e4a72af04 | -14.7563 | -52.65829 | 2024-12-12 04:42:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bc67d716-59f8-36c3-a139-3c842feb1a57 | -15.92218 | -59.80304 | 2024-12-12 04:42:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b39e16d-3552-331c-8d36-23bc0e22cbd9 | -22.54097 | -48.81123 | 2024-12-12 04:44:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1bb43e02-0209-3c71-828d-48d1edf6884e | -22.31206 | -49.7591 | 2024-12-12 04:44:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 534062d4-3f3c-3a2e-8fde-21f8d53f5735 | -26.73486 | -52.71839 | 2024-12-12 04:44:00 | NPP-375D | QUILOMBO | SANTA CATARINA | Brasil | 4214201 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ec7a45fe-9a57-3133-b664-6416572c97fa | -23.02512 | -50.39315 | 2024-12-12 04:44:00 | NPP-375D | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6154f23b-695f-3e29-a2ee-b752dc65fbf0 | -21.79376 | -55.9879 | 2024-12-12 04:44:00 | NPP-375D | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6122e64f-81e1-36a0-911f-a0f677a46d8b | -22.31571 | -49.75965 | 2024-12-12 04:44:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6d50dd75-411c-38bb-9882-a58ea23f3531 | -21.78593 | -55.99077 | 2024-12-12 04:44:00 | NPP-375D | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 069d6ad0-3257-3958-9468-f45503a9a343 | -23.70376 | -46.47697 | 2024-12-12 04:44:00 | NPP-375D | MAUÁ | SÃO PAULO | Brasil | 3529401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2fbb9ffa-ad9d-3f61-86e5-02904542d159 | -21.79021 | -55.98721 | 2024-12-12 04:44:00 | NPP-375D | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3a3e83c9-e50c-3dfc-afe5-863921882faa | -23.02303 | -50.39528 | 2024-12-12 04:44:00 | NPP-375D | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d270e859-a997-3016-a3f4-69f957b300fa | -29.6373 | -54.17076 | 2024-12-12 04:46:00 | NPP-375D | SÃO PEDRO DO SUL | RIO GRANDE DO SUL | Brasil | 4319406 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 054735fd-4b26-3466-8a3b-f6c665a175d9 | -31.03098 | -50.78727 | 2024-12-12 04:46:00 | NPP-375D | MOSTARDAS | RIO GRANDE DO SUL | Brasil | 4312500 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| a54bb6ef-0179-35de-b17e-71e80769cbd3 | -29.6314 | -51.97097 | 2024-12-12 04:46:00 | NPP-375D | CRUZEIRO DO SUL | RIO GRANDE DO SUL | Brasil | 4306205 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4a31ba76-8aa3-344d-862b-2e61c3fe13af | -31.02784 | -50.7878 | 2024-12-12 04:46:00 | NPP-375D | MOSTARDAS | RIO GRANDE DO SUL | Brasil | 4312500 | 43 | 33 | nan | nan | nan | Pampa | 2.2 |
| 9096b887-9fa5-324b-82b8-b763c311d16e | -31.02714 | -50.78667 | 2024-12-12 04:46:00 | NPP-375D | MOSTARDAS | RIO GRANDE DO SUL | Brasil | 4312500 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| 9c72553e-0c63-3b79-beec-ec5cfbf80157 | -3.2503 | -46.8709 | 2024-12-12 04:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| b91491f9-ae27-3524-9872-810bbcf2ff18 | 2.47715 | -60.69471 | 2024-12-12 04:59:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 09bd6ddb-532f-37c8-bd23-3665dde5956f | 3.29288 | -60.06818 | 2024-12-12 04:59:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 57e02604-ad64-3ee2-8e5b-f144041383c7 | 3.30252 | -60.07112 | 2024-12-12 04:59:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a0236ec9-3527-3ae9-802f-074bdba4051e | 3.29737 | -60.06744 | 2024-12-12 04:59:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 60b004a1-e256-3a0d-b2df-af466188dbde | 3.29354 | -60.07264 | 2024-12-12 04:59:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 39d16dcd-2c63-3a52-853e-ac913544461a | 3.29129 | -60.07071 | 2024-12-12 04:59:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 08c878fe-a5eb-378b-bcb1-21635298b43c | 3.82891 | -60.52742 | 2024-12-12 04:59:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee1fb215-5de1-3b48-adbf-78e561d46e68 | 3.29578 | -60.06996 | 2024-12-12 04:59:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 50198404-bed0-3b13-ab88-cb4d9bc36e91 | -3.9936 | -46.95683 | 2024-12-12 04:59:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e428625-9ed8-3430-93ba-bc80c378adbc | -3.04002 | -53.25514 | 2024-12-12 04:59:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f6946231-a97b-3bea-94bd-b9012a83d5ce | -2.56282 | -53.39574 | 2024-12-12 04:59:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6606ded8-e960-3c9a-8ee8-685844ee6bb2 | -2.08127 | -52.27826 | 2024-12-12 04:59:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f46868d0-6cad-39fd-97b0-45fc455f96b7 | -4.13271 | -46.70752 | 2024-12-12 04:59:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 673e89aa-6777-3d33-8ad3-5c39d1ea37ce | -2.27106 | -53.48516 | 2024-12-12 04:59:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 90fb8355-9212-3dac-80ac-f594285aeda6 | -1.90742 | -52.83394 | 2024-12-12 04:59:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 560fce09-58dc-36da-9391-f3b303470dcf | -1.90799 | -52.83029 | 2024-12-12 04:59:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 506f48fb-fac9-326b-9f86-314f9f0d8068 | -3.81853 | -44.12587 | 2024-12-12 04:59:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ecc5e5f6-e655-3ed3-b065-cb5a196fb16b | -2.55838 | -53.42422 | 2024-12-12 04:59:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 14efd247-a835-3bd9-ac8e-679ebcf3ee7c | -3.24271 | -46.87944 | 2024-12-12 04:59:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| e4214161-b66b-36cd-b817-4362389439a5 | -3.19416 | -54.3329 | 2024-12-12 04:59:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f2508ae-ad7d-3260-a068-a225d02d826b | -2.95381 | -53.11197 | 2024-12-12 04:59:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a81d7e2b-2503-3f80-b5e9-04297cb25695 | -3.26931 | -49.76752 | 2024-12-12 04:59:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a004eef4-afe0-345d-a1f0-1538970c3468 | -2.56549 | -51.88292 | 2024-12-12 04:59:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cbb7ce80-bff5-3a2f-b3d7-6fa336d08d26 | -2.31166 | -46.99425 | 2024-12-12 04:59:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bdf0678d-e5a6-3f3d-a847-d693b27eb90e | -2.81476 | -53.03825 | 2024-12-12 04:59:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e492809-5c75-3c8c-a6c9-ad85d498b29e | -3.21167 | -53.00833 | 2024-12-12 04:59:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 715a440e-9ab7-30c6-a61b-4a4bc6c0de15 | -2.58127 | -51.92229 | 2024-12-12 04:59:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec77dccc-c660-36b4-a896-30d02831999d | -2.78386 | -53.238 | 2024-12-12 04:59:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2c7c51c9-52af-3fe8-83fb-52e20587878b | -3.06653 | -53.75981 | 2024-12-12 04:59:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b650ba67-ead2-319c-ba3c-70d5346ad18c | -1.87142 | -54.68684 | 2024-12-12 04:59:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7a3d67c9-edb4-3cdd-8453-18d178c5c5b3 | -3.24852 | -46.87442 | 2024-12-12 04:59:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| ca19cb79-c2b2-38af-b938-7312fc720323 | -3.0372 | -53.25098 | 2024-12-12 04:59:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86ba7be9-0fad-3334-b6fe-899776296804 | -2.95721 | -53.11251 | 2024-12-12 04:59:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9190e142-e91f-3d9b-9983-ba77d9e2a1b1 | -1.91082 | -52.83447 | 2024-12-12 04:59:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 455c88fd-7120-3b17-9b5f-edc8b8add024 | -2.78048 | -53.23746 | 2024-12-12 04:59:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a202c9b-f85e-38cf-866c-621022b0f10c | -3.30393 | -52.7734 | 2024-12-12 04:59:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1add6b0a-2583-3098-a7b8-3be2d98cefa2 | -4.07759 | -46.12948 | 2024-12-12 04:59:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README28.md)
