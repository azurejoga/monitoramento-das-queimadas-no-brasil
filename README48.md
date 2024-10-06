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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 03f32c51-1f1c-3d3d-8832-0e4abda0eb1d | -8.2035 | -40.72336 | 2024-10-06 03:53:00 | NPP-375D | BETÂNIA DO PIAUÍ | PIAUÍ | Brasil | 2201739 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c1ad5ba9-9bbd-324a-8df2-ee679804a49b | -8.20288 | -40.72715 | 2024-10-06 03:53:00 | NPP-375D | BETÂNIA DO PIAUÍ | PIAUÍ | Brasil | 2201739 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d8dddff2-6f4b-3b9a-99c1-e6ea6138bf30 | -4.7522 | -40.221 | 2024-10-06 03:53:00 | NPP-375D | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b3f940b3-a38b-3c3a-82c0-89e247fd21a2 | -4.75157 | -40.22486 | 2024-10-06 03:53:00 | NPP-375D | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a96e9a1e-98fa-3bab-bb83-874b48dd449a | -6.32491 | -40.4706 | 2024-10-06 03:53:00 | NPP-375D | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 00d3d80c-9c71-3cc0-b498-8060d64b0262 | -6.27624 | -41.85961 | 2024-10-06 03:53:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 47959550-f377-36cb-850f-6287d8b358ae | -6.27179 | -41.86347 | 2024-10-06 03:53:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1fb81197-3fcc-3f05-971a-e227f9ec3ba1 | -5.17753 | -41.29653 | 2024-10-06 03:53:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 77e7d5b3-45ff-31e7-b5ef-6468ac5113ba | -7.35151 | -41.94712 | 2024-10-06 03:53:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| f3ab7ca0-ecd9-37f2-a8a7-145a98d742b7 | -7.34854 | -41.94216 | 2024-10-06 03:53:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b153c99d-58d9-3855-8bc3-b13f873ba35b | -7.02639 | -42.11919 | 2024-10-06 03:53:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e9ff17c1-20c3-3a22-af61-65fd1ec1a48c | -7.02527 | -42.12103 | 2024-10-06 03:53:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 535db042-1ea4-3f6e-8a11-c8b543ed13fa | -6.97244 | -41.68654 | 2024-10-06 03:53:00 | NPP-375D | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3cc1feb3-acf2-3a56-ac75-e5b0695479de | -6.96878 | -41.68595 | 2024-10-06 03:53:00 | NPP-375D | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 51bd3104-6a48-305a-a25f-6499a474b1ad | -6.93492 | -41.97286 | 2024-10-06 03:53:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 05312905-94d8-3081-a788-3b1763240f5b | -6.93328 | -41.97479 | 2024-10-06 03:53:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 66660813-26ff-3cab-8568-864ef20d4d41 | -6.84846 | -41.68936 | 2024-10-06 03:53:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fa58891b-4d38-3714-8eae-17b4af856aff | -6.84776 | -41.69366 | 2024-10-06 03:53:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5f180170-0bbb-3a41-8519-3c808781be8a | -6.84706 | -41.69797 | 2024-10-06 03:53:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a93990d0-bc04-3c3a-aefa-b582771ce462 | -6.8251 | -41.80951 | 2024-10-06 03:53:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4c937677-c180-3d72-bcf6-ac1aade2afa7 | -6.49641 | -41.38008 | 2024-10-06 03:53:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7e63de19-693e-366a-ad93-02278e0bf166 | -6.49542 | -41.3814 | 2024-10-06 03:53:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6c7911e4-c0c1-3126-a6b7-de8f2d5b9c20 | -6.49279 | -41.37956 | 2024-10-06 03:53:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 89dce1d2-0235-3ee3-b9c7-282082644a4b | -6.49246 | -41.37673 | 2024-10-06 03:53:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f4f7358a-f167-3ed0-b0b1-4bd1a3edddf2 | -6.49179 | -41.38087 | 2024-10-06 03:53:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c4a33149-0847-32ec-86be-39104dd3cace | -6.47829 | -41.94743 | 2024-10-06 03:53:00 | NPP-375D | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| c8de0b29-763b-3e16-9a4e-e72e4d93d24f | -8.42276 | -41.9458 | 2024-10-06 03:53:00 | NPP-375D | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0f30ab55-def4-3656-8c7a-871475b2e282 | -10.23037 | -42.39091 | 2024-10-06 03:53:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| a09a7096-e0fc-3888-882a-56e786ee2d2c | -10.23018 | -42.39245 | 2024-10-06 03:53:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 884152ae-e806-3716-8e05-6c3898bd6d2f | -10.13119 | -42.42388 | 2024-10-06 03:53:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 84601524-651b-3f95-aa9e-76de4080e689 | -10.13046 | -42.42818 | 2024-10-06 03:53:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c5bd46bd-53ec-3040-ab16-243d5b8e7a15 | -4.80552 | -42.77378 | 2024-10-06 03:53:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| bb052f26-d3e4-39e0-bfa1-57cabae71770 | -6.23714 | -43.38898 | 2024-10-06 03:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ae93a5e4-f7c9-3720-9ffe-9fa430cbba44 | -6.23306 | -43.38826 | 2024-10-06 03:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 91aa3e62-9545-3472-b778-48816dbe1025 | -6.07371 | -42.33983 | 2024-10-06 03:53:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| f72e12f7-de50-328e-8b07-1a0475fe0556 | -5.94978 | -43.38652 | 2024-10-06 03:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 4.7 |
| f279e6f1-68f2-3e2a-afb0-bdad0cbb8dbb | -5.94711 | -43.38562 | 2024-10-06 03:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 5.0 |
| ca5472e0-1570-3f1b-9b4c-b12dc195811e | -5.88169 | -41.98025 | 2024-10-06 03:53:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 678fc682-2b40-3b39-846e-c7755d5c344c | -5.74028 | -43.05051 | 2024-10-06 03:53:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 41e26cc8-7edb-3cc7-a9cb-8cd142f601af | -5.68502 | -43.1575 | 2024-10-06 03:53:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0f7947d0-61b3-307e-9f43-d54f1145eaea | -5.55165 | -42.78532 | 2024-10-06 03:53:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 0b590aa9-ce9d-3072-8ed7-c7fe2906ffed | -5.5508 | -42.79047 | 2024-10-06 03:53:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 5bcdde73-0136-3213-96c5-6211945edffd | -5.50895 | -42.78638 | 2024-10-06 03:53:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 3fac40ff-121e-3485-ad4d-04df08dfe216 | -5.18139 | -42.80713 | 2024-10-06 03:53:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5ce425f4-1a1f-3ff5-8b44-7b1654f5c7b1 | -7.75529 | -43.04721 | 2024-10-06 03:53:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 812c208d-fc62-3320-a65f-2a6b859da78f | -7.77059 | -43.07557 | 2024-10-06 03:53:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| d14e2dc7-89e1-32c6-bb94-719e35bedbea | -7.7658 | -43.08008 | 2024-10-06 03:53:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 01db4991-29b1-3b65-9931-f6f173b7ec6c | -7.65924 | -42.45 | 2024-10-06 03:53:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| aa73b661-8dbb-3a06-8b6c-23a59198e331 | -7.65626 | -42.42145 | 2024-10-06 03:53:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 584ca79d-cf70-3d3d-87a5-0376af633928 | -7.65249 | -42.42081 | 2024-10-06 03:53:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| d21adc73-6e48-3257-a545-2b0cd7119fbd | -7.64571 | -42.41502 | 2024-10-06 03:53:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5dab46ef-ad15-3198-a58f-49289c7d0d10 | -7.6425 | -42.48032 | 2024-10-06 03:53:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 46aba316-efad-362e-aed3-1359993566e5 | -7.64195 | -42.41436 | 2024-10-06 03:53:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b50062b8-928d-349f-9365-36a9b26479c2 | -7.64173 | -42.4849 | 2024-10-06 03:53:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 4fa7ee49-584b-3c93-a345-4305a1d9f001 | -7.64096 | -42.48949 | 2024-10-06 03:53:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 29314f6e-6cf4-321a-9f04-08d37a2bf6c4 | -7.64019 | -42.49409 | 2024-10-06 03:53:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 335d8957-253a-3c30-9441-ff42e28d8dec | -7.63562 | -42.49808 | 2024-10-06 03:53:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 1816b0f6-199a-35d0-a7ea-79a8827b7d8f | -7.63183 | -42.49745 | 2024-10-06 03:53:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 528a9d67-535c-325a-bc42-01ee3b3b9ba5 | -7.62804 | -42.49684 | 2024-10-06 03:53:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 2a35a761-445d-32db-9b16-eacc7f9b2970 | -7.62503 | -42.49162 | 2024-10-06 03:53:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 0ba27325-e97e-395b-af64-b2dbf8581992 | -7.61611 | -42.45237 | 2024-10-06 03:53:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 5bd6071f-df19-30b0-9428-45ab68a4f507 | -7.61606 | -42.45461 | 2024-10-06 03:53:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 9d67e003-4822-3994-9209-6978ee3e4af1 | -7.61534 | -42.45692 | 2024-10-06 03:53:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b04c46c2-2363-3306-b388-f0fb70086a67 | -7.29837 | -42.24825 | 2024-10-06 03:53:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c9ec80d8-6c38-35ad-81c4-bffd96cf76c2 | -7.29462 | -42.2476 | 2024-10-06 03:53:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e709e17e-9c2b-3d51-a641-7086f8ed5804 | -7.13994 | -42.6247 | 2024-10-06 03:53:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ac4b9c3c-03ad-36e9-92a1-7dbaade673a1 | -7.13688 | -42.61926 | 2024-10-06 03:53:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| aad86478-aa6e-3a68-a1fa-29224f4c34a4 | -7.1361 | -42.62405 | 2024-10-06 03:53:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0c35cd87-6d27-396e-948f-82ff9aa6d581 | -7.1346 | -42.60913 | 2024-10-06 03:53:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ce31e832-1161-3c8a-9fa5-190acf56b782 | -7.13076 | -42.6085 | 2024-10-06 03:53:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1d5c2965-7737-32e9-83d9-e71124fe5931 | -7.1277 | -42.60314 | 2024-10-06 03:53:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d9394790-595d-3142-b69d-f84523c7f4d1 | -7.12457 | -42.6221 | 2024-10-06 03:53:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0b3ff87e-e070-3532-b6de-75d46a7daa6f | -7.12379 | -42.62685 | 2024-10-06 03:53:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 93e2a300-8d97-37ed-9088-da9e6d24f21d | -7.12307 | -42.60727 | 2024-10-06 03:53:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 4baa958e-3e2c-329d-90f1-54a728684901 | -7.1215 | -42.61675 | 2024-10-06 03:53:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 7a1f7987-d8cb-37e5-9bae-8268e32eecce | -7.11994 | -42.6262 | 2024-10-06 03:53:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1448a62f-7367-3075-880e-c2453dd819ed | -7.11922 | -42.60667 | 2024-10-06 03:53:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 3b56b507-d8aa-3932-b1da-b8c0918bdaeb | -7.11766 | -42.61613 | 2024-10-06 03:53:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ef7fd619-a910-3425-bb52-33f7487f9386 | -7.11688 | -42.62082 | 2024-10-06 03:53:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| def65b5f-e518-3b9e-a5d6-3ddc8dabbd4a | -7.11381 | -42.61551 | 2024-10-06 03:53:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| d3f5c4f8-863a-3cd1-8e45-b0c4e92d1918 | -6.65165 | -42.11548 | 2024-10-06 03:53:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0256f8e1-0542-34b4-b95b-6d4fb23b00b8 | -6.64718 | -42.1192 | 2024-10-06 03:53:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 96a53dce-f1f7-3ea9-9f1b-2e2072eba573 | -6.64269 | -42.12297 | 2024-10-06 03:53:00 | NPP-375D | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 85a00d1a-1a9a-34dc-8af6-22403e6c6b4f | -6.63819 | -42.12685 | 2024-10-06 03:53:00 | NPP-375D | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| e69b5ed4-724f-3454-ae6c-b1061ade3c83 | -6.63444 | -42.12622 | 2024-10-06 03:53:00 | NPP-375D | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| de0074fa-b61e-3dae-9a6c-2da98e13fc15 | -6.63368 | -42.13079 | 2024-10-06 03:53:00 | NPP-375D | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| f2d3ca7f-453d-3d65-84e1-8a673c592912 | -6.63292 | -42.1121 | 2024-10-06 03:53:00 | NPP-375D | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| e3c584a6-816b-33c6-9c66-ffc4ccb22ddf | -6.63068 | -42.1256 | 2024-10-06 03:53:00 | NPP-375D | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a38acc18-5443-3a3c-8bc9-c76759df3011 | -6.62992 | -42.13015 | 2024-10-06 03:53:00 | NPP-375D | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 3ef374ea-afae-3c87-b1e5-5db163b5a83d | -6.62617 | -42.12952 | 2024-10-06 03:53:00 | NPP-375D | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 36bb2ea0-5869-3cab-806e-701cc18cc2bf | -6.62389 | -42.12001 | 2024-10-06 03:53:00 | NPP-375D | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| eb48506e-edda-36e6-bb8a-54f711010410 | -6.62314 | -42.12447 | 2024-10-06 03:53:00 | NPP-375D | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 3a16c227-55e8-377f-b112-92220d0d4992 | -6.62241 | -42.1289 | 2024-10-06 03:53:00 | NPP-375D | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| ced472b4-cdf6-3d14-a4b0-9639a97f0ea8 | -6.61937 | -42.12394 | 2024-10-06 03:53:00 | NPP-375D | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 5106033f-8ed1-3d59-a750-4700cceaa308 | -6.61863 | -42.12837 | 2024-10-06 03:53:00 | NPP-375D | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| a3ac73e3-961e-353d-8029-e016e032e116 | -7.74747 | -43.0459 | 2024-10-06 03:53:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| c2c1c047-3a6c-3247-bf79-52d92b8feadd | -7.7921 | -43.11541 | 2024-10-06 03:53:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 51cc14d4-c585-3925-b409-2fd9ce08f946 | -7.76973 | -43.08066 | 2024-10-06 03:53:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| bcab21c2-382c-3055-93bb-33461f59259e | -7.76274 | -43.07434 | 2024-10-06 03:53:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 72c9f590-f109-3188-b998-5266b6494cb5 | -7.74356 | -43.04524 | 2024-10-06 03:53:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |


[Clique aqui para ver as próximas entradas](README49.md)
