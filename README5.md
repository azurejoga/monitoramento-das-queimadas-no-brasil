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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 64db69f2-f330-37ee-b4f2-45e5f6a3b1ac | -23.3169 | -47.248901 | 2024-10-02 00:27:54 | METOP-B | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d208fdbd-3504-36ef-a7a7-ac571cd6d6d0 | -23.318701 | -47.258099 | 2024-10-02 00:27:54 | METOP-B | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d296c03b-afbf-3943-899d-37faf0e77362 | -23.320499 | -47.2673 | 2024-10-02 00:27:54 | METOP-B | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7fe5d0f6-17bc-31e3-adf3-9b2200187cc9 | -22.8965 | -45.085899 | 2024-10-02 00:27:54 | METOP-B | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| abdca2f3-c339-3b63-864c-f0a02f51431c | -22.8981 | -45.093601 | 2024-10-02 00:27:54 | METOP-B | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ca6945ca-b4d2-3309-8702-35813a3954bb | -22.8997 | -45.1012 | 2024-10-02 00:27:54 | METOP-B | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5724c0a5-4cc6-3c36-9767-7828986a416b | -22.901199 | -45.108898 | 2024-10-02 00:27:54 | METOP-B | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c98174a4-a6ed-3f11-a501-a1705080742e | -22.9028 | -45.1166 | 2024-10-02 00:27:54 | METOP-B | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 630371d7-6525-3c1e-af6d-218f02fd1c01 | -22.885099 | -45.080601 | 2024-10-02 00:27:54 | METOP-B | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a3f0b27d-81ee-3ab2-83ed-f282ccfd4a47 | -22.8867 | -45.0882 | 2024-10-02 00:27:54 | METOP-B | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3c866326-476d-3e49-8c6d-7fade385aca9 | -22.8883 | -45.095901 | 2024-10-02 00:27:54 | METOP-B | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 33a2d55f-a658-341a-8c16-983365075cd6 | -22.8899 | -45.1036 | 2024-10-02 00:27:54 | METOP-B | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5c91ef91-2451-3057-b5ed-a34228dfdab3 | -22.875299 | -45.082901 | 2024-10-02 00:27:54 | METOP-B | LORENA | SÃO PAULO | Brasil | 3527207 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 36054404-09ca-36cc-b97d-4bb49fb16891 | -22.8769 | -45.0905 | 2024-10-02 00:27:54 | METOP-B | LORENA | SÃO PAULO | Brasil | 3527207 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6c25e6ed-6113-329d-a710-1a76a67539c0 | -22.8785 | -45.098202 | 2024-10-02 00:27:54 | METOP-B | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 059fd524-cd5a-3112-9ee9-94aea12b08d7 | -22.8801 | -45.1059 | 2024-10-02 00:27:54 | METOP-B | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 82e2c277-8128-34bd-a62b-e321fff70c52 | -22.762699 | -44.6404 | 2024-10-02 00:27:55 | METOP-B | SÃO JOSÉ DO BARREIRO | SÃO PAULO | Brasil | 3549607 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 56828575-bc38-3242-a100-61948b23be6b | -22.7642 | -44.647999 | 2024-10-02 00:27:55 | METOP-B | SÃO JOSÉ DO BARREIRO | SÃO PAULO | Brasil | 3549607 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 36c7d6a9-579c-3d7c-bc58-c5e0f87fed64 | -22.6059 | -43.950001 | 2024-10-02 00:27:55 | METOP-B | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ff5b8e97-8fae-3f63-84bd-8466008dfa00 | -22.607401 | -43.957401 | 2024-10-02 00:27:55 | METOP-B | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 80389f23-d7d3-3143-9200-7a2e402fbb83 | -22.5089 | -43.833599 | 2024-10-02 00:27:56 | METOP-B | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 846634ca-8b9d-38ac-9fd3-0ee07887f96c | -22.3424 | -43.352001 | 2024-10-02 00:27:57 | METOP-B | PATY DO ALFERES | RIO DE JANEIRO | Brasil | 3303856 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8329b1c0-7b4a-3615-af46-4ae0baa98465 | -22.378 | -43.515202 | 2024-10-02 00:27:57 | METOP-B | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 99399da4-ee3e-3b56-94ca-7c32d2304ce4 | -22.216801 | -43.155899 | 2024-10-02 00:27:58 | METOP-B | AREAL | RIO DE JANEIRO | Brasil | 3300225 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5399bda6-38ec-3df2-ac09-6bc5c58e4cfb | -22.482901 | -44.144199 | 2024-10-02 00:27:58 | METOP-B | VOLTA REDONDA | RIO DE JANEIRO | Brasil | 3306305 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 255b6f42-7ec8-3b74-a82c-71b6628f8e25 | -22.457001 | -44.1194 | 2024-10-02 00:27:58 | METOP-B | VOLTA REDONDA | RIO DE JANEIRO | Brasil | 3306305 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7acdcc6c-120a-3d87-8575-8f81cd64c1dc | -22.4473 | -44.121799 | 2024-10-02 00:27:58 | METOP-B | VOLTA REDONDA | RIO DE JANEIRO | Brasil | 3306305 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f6c82f6d-2133-3197-9743-b6f66598ea68 | -22.3519 | -44.012699 | 2024-10-02 00:27:59 | METOP-B | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7f299508-7a5e-35eb-b395-07bb14572a6b | -22.347401 | -44.231998 | 2024-10-02 00:28:00 | METOP-B | QUATIS | RIO DE JANEIRO | Brasil | 3304128 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1ccfc530-5576-3610-94f2-e53175df2950 | -21.6294 | -41.519501 | 2024-10-02 00:28:02 | METOP-B | CARDOSO MOREIRA | RIO DE JANEIRO | Brasil | 3301157 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a952d30d-0c5a-3796-8479-36e8454f97a6 | -21.6313 | -41.527599 | 2024-10-02 00:28:02 | METOP-B | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f30c8601-4570-3fb7-bcfc-cbf5d618ad17 | -21.372101 | -51.020699 | 2024-10-02 00:28:02 | METOP-B | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 855bf8d4-896c-3797-9f38-edf186a4996e | -19.774401 | -43.164101 | 2024-10-02 00:28:02 | METOP-B | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 702df8dc-be57-3567-9c19-761eb77a97bb | -21.340401 | -51.012299 | 2024-10-02 00:28:02 | METOP-B | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f258e44e-d77d-34b8-80c6-83988014607b | -21.3281 | -51.000198 | 2024-10-02 00:28:02 | METOP-B | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 856125c8-ad9f-3adf-a72e-cd743b036b94 | -21.330601 | -51.014198 | 2024-10-02 00:28:02 | METOP-B | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 16fcbed4-e46d-3c25-bc5a-e89fe6d5c19d | -21.3794 | -51.0047 | 2024-10-02 00:28:02 | METOP-B | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 428f1f23-e118-3bdf-b9aa-57894a1510a5 | -21.381901 | -51.018799 | 2024-10-02 00:28:02 | METOP-B | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b2ada87d-9e5a-3d74-88e3-916867fb01d1 | -21.3696 | -51.006599 | 2024-10-02 00:28:02 | METOP-B | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f6f30c91-84a3-3086-b951-90baeb153d1a | -21.514601 | -42.052502 | 2024-10-02 00:28:06 | METOP-B | SANTO ANTÔNIO DE PÁDUA | RIO DE JANEIRO | Brasil | 3304706 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3b8bd2aa-a7b8-39d2-af1f-b22dedb58987 | -21.516399 | -42.060299 | 2024-10-02 00:28:06 | METOP-B | SANTO ANTÔNIO DE PÁDUA | RIO DE JANEIRO | Brasil | 3304706 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 41cb89cf-0564-3ffd-baae-517d79dc6d37 | -21.314301 | -41.4104 | 2024-10-02 00:28:07 | METOP-B | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4afba002-8016-3b75-870d-e40642320898 | -21.316299 | -41.418701 | 2024-10-02 00:28:07 | METOP-B | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ab1a50b8-5924-39f2-a0cf-f8614ca065f4 | -21.6122 | -42.802399 | 2024-10-02 00:28:07 | METOP-B | ARGIRITA | MINAS GERAIS | Brasil | 3104403 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4d4e180d-7763-341a-9f63-2abb2a262db7 | -21.6789 | -43.9459 | 2024-10-02 00:28:10 | METOP-B | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bda8134b-f652-30c2-921a-f1f6670e41ab | -21.6805 | -43.953201 | 2024-10-02 00:28:10 | METOP-B | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8ce5f0cf-0732-3483-af1d-cb99d346b637 | -21.6675 | -43.941002 | 2024-10-02 00:28:10 | METOP-B | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0b0b2f38-1696-35ca-b149-82ad6d5f605c | -21.6691 | -43.948299 | 2024-10-02 00:28:10 | METOP-B | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f2f2389c-4801-308b-b3d0-f9df6acc77f0 | -21.6707 | -43.9557 | 2024-10-02 00:28:10 | METOP-B | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d1fc3982-227e-34b2-b9ee-3d28efbd768f | -21.6593 | -43.950699 | 2024-10-02 00:28:10 | METOP-B | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8a335124-6b1d-358f-b760-711e54f9be34 | -21.6625 | -43.965401 | 2024-10-02 00:28:10 | METOP-B | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ce54858e-a455-316a-b467-4b3a4c11244d | -22.604401 | -48.760399 | 2024-10-02 00:28:11 | METOP-B | LENÇÓIS PAULISTA | SÃO PAULO | Brasil | 3526803 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| dd47c3ea-865c-397d-98ea-c30d5f7b2ff6 | -22.6064 | -48.771099 | 2024-10-02 00:28:11 | METOP-B | LENÇÓIS PAULISTA | SÃO PAULO | Brasil | 3526803 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| aca19234-9d24-3633-9bf3-22324db828e2 | -21.881399 | -45.335201 | 2024-10-02 00:28:11 | METOP-B | CAMBUQUIRA | MINAS GERAIS | Brasil | 3110707 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cee6e023-e5e8-36db-8894-7235c34c660f | -21.8829 | -45.3428 | 2024-10-02 00:28:11 | METOP-B | CAMBUQUIRA | MINAS GERAIS | Brasil | 3110707 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8a49834e-8a8a-3067-80db-e892597d0221 | -22.114799 | -46.582001 | 2024-10-02 00:28:12 | METOP-B | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1f2c3f61-d79f-3a77-a944-8454522cfff9 | -22.1164 | -46.590302 | 2024-10-02 00:28:12 | METOP-B | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f8e21d35-6ef7-3603-9948-0209723c6064 | -22.118099 | -46.598598 | 2024-10-02 00:28:12 | METOP-B | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3e13df91-102c-3929-96a0-636bff09a4a9 | -21.556801 | -43.952702 | 2024-10-02 00:28:12 | METOP-B | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7fe0094f-151a-390e-9e31-e645d4d63a80 | -21.558399 | -43.960098 | 2024-10-02 00:28:12 | METOP-B | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0d02286a-a822-347d-a43a-9bc7a3f045ce | -22.3944 | -49.2743 | 2024-10-02 00:28:16 | METOP-B | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e526b6bb-dd3d-3b0f-99c9-4c18a584a42a | -22.3965 | -49.285702 | 2024-10-02 00:28:16 | METOP-B | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c3431275-bbbd-3866-969e-6fcd5fd79781 | -22.3985 | -49.2971 | 2024-10-02 00:28:16 | METOP-B | CABRÁLIA PAULISTA | SÃO PAULO | Brasil | 3508306 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f063f351-989b-3d9c-808f-d77ccc03092a | -22.3825 | -49.2649 | 2024-10-02 00:28:16 | METOP-B | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5abb1061-f49b-37c8-a12c-1708b0840261 | -22.3846 | -49.276299 | 2024-10-02 00:28:16 | METOP-B | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b522b22b-2265-3d72-a0d0-dfe23e2e3d2a | -22.3867 | -49.287701 | 2024-10-02 00:28:16 | METOP-B | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8f86da5d-6413-3962-bf56-641edbad18da | -22.3708 | -49.2556 | 2024-10-02 00:28:16 | METOP-B | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 28f08ce8-18c3-3464-88f9-16b6f5340847 | -22.372801 | -49.266899 | 2024-10-02 00:28:16 | METOP-B | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7d9559b1-f4ae-336c-bd9e-78a9dc632c68 | -22.374901 | -49.278301 | 2024-10-02 00:28:16 | METOP-B | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8ace1a2c-0197-3af3-9ec0-7e905b0ff328 | -22.377001 | -49.2897 | 2024-10-02 00:28:16 | METOP-B | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7a2eb32b-2a66-3fc3-a07e-de8db9960088 | -22.379 | -49.301102 | 2024-10-02 00:28:16 | METOP-B | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 66f3a8aa-4dce-3868-9d6e-1a02a544b4df | -22.361 | -49.257599 | 2024-10-02 00:28:16 | METOP-B | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8f6043b6-cc09-3532-8b38-b05530f2a4e1 | -22.363001 | -49.268902 | 2024-10-02 00:28:16 | METOP-B | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| dcfb4273-f5cd-347e-9874-ae295aaea487 | -22.365101 | -49.2803 | 2024-10-02 00:28:16 | METOP-B | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| af50fb77-f075-3c59-920d-8a4bbcfcfc93 | -22.367201 | -49.291698 | 2024-10-02 00:28:16 | METOP-B | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3da66413-b196-3314-8265-a3817f2bf336 | -22.3692 | -49.303101 | 2024-10-02 00:28:16 | METOP-B | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8754118a-907c-31ab-abf3-cf21fb0accda | -22.355301 | -49.282398 | 2024-10-02 00:28:16 | METOP-B | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9af72661-9331-3d4b-b61c-e0d08bd8b031 | -22.357401 | -49.2938 | 2024-10-02 00:28:16 | METOP-B | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3dcc09c6-8749-3b76-ab4d-fa7495bffb55 | -22.359501 | -49.305199 | 2024-10-02 00:28:16 | METOP-B | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 418f7a8c-b16d-312c-9bdd-014592ad85e6 | -22.3615 | -49.316601 | 2024-10-02 00:28:16 | METOP-B | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 31b808af-83b7-3fa1-a438-a523115e1595 | -22.3636 | -49.327999 | 2024-10-02 00:28:16 | METOP-B | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| edbf386f-eb63-33e0-b57e-c6615c377e76 | -22.351801 | -49.3186 | 2024-10-02 00:28:16 | METOP-B | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b106b489-1f5a-3a3a-a0e4-21ca091a31fc | -20.928499 | -42.928501 | 2024-10-02 00:28:18 | METOP-B | SÃO GERALDO | MINAS GERAIS | Brasil | 3161502 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c7aa7f50-2890-359f-a431-ac8082b33146 | -20.930201 | -42.936001 | 2024-10-02 00:28:18 | METOP-B | SÃO GERALDO | MINAS GERAIS | Brasil | 3161502 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2d769fb3-9920-390d-b25a-3cb392457499 | -20.690001 | -41.972599 | 2024-10-02 00:28:19 | METOP-B | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f93c8fb4-9696-3e30-bcdd-e5feb188c450 | -20.9681 | -43.2901 | 2024-10-02 00:28:19 | METOP-B | ALTO RIO DOCE | MINAS GERAIS | Brasil | 3102100 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c3e779d9-4b96-33b8-a987-c3a188960bdd | -20.969801 | -43.297501 | 2024-10-02 00:28:19 | METOP-B | ALTO RIO DOCE | MINAS GERAIS | Brasil | 3102100 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 11880111-df2c-3459-aafa-9294cb08ee07 | -21.8976 | -48.4571 | 2024-10-02 00:28:21 | METOP-B | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a8c8363c-56c3-3648-8aad-62c56bdcf5e8 | -21.899599 | -48.467201 | 2024-10-02 00:28:21 | METOP-B | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 14832d93-4d76-302c-a96c-8e66d4889821 | -21.901501 | -48.4772 | 2024-10-02 00:28:21 | METOP-B | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c487412f-f1c3-3b24-a533-776830a16555 | -21.8878 | -48.459202 | 2024-10-02 00:28:21 | METOP-B | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 333d9f26-e589-3d85-9f93-71121ea90e13 | -21.889799 | -48.469299 | 2024-10-02 00:28:21 | METOP-B | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 570dcc37-9f0d-360d-a458-a538d668d8a7 | -21.891701 | -48.479301 | 2024-10-02 00:28:21 | METOP-B | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 77c4b613-ee17-3898-8a50-c92ff490cf67 | -21.8011 | -48.754398 | 2024-10-02 00:28:24 | METOP-B | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d41036b1-627f-3064-b735-43a1c6d60230 | -21.802999 | -48.764801 | 2024-10-02 00:28:24 | METOP-B | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 1681055d-d7b5-3fbd-80ea-cad56518a5c9 | -21.586399 | -47.7355 | 2024-10-02 00:28:24 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 84494766-d245-32a2-874c-ef4602b92298 | -20.3524 | -42.7542 | 2024-10-02 00:28:27 | METOP-B | URUCÂNIA | MINAS GERAIS | Brasil | 3170503 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fcb91ded-aba5-3fae-81b2-5f6ff20cd45e | -20.9849 | -45.562401 | 2024-10-02 00:28:27 | METOP-B | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3a1b5cfa-fbf0-3e0c-bcdf-d57e86686682 | -20.9865 | -45.569901 | 2024-10-02 00:28:27 | METOP-B | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c18d1670-368d-3fd7-9479-d94037fee878 | -20.5103 | -44.0173 | 2024-10-02 00:28:29 | METOP-B | JECEABA | MINAS GERAIS | Brasil | 3135407 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |


[Clique aqui para ver as próximas entradas](README6.md)
