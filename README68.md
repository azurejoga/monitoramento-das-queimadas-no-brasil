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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f52259d6-2a77-39b2-ab28-32ac736b93c9 | -10.26154 | -50.31746 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| b7297c33-3f2b-31a1-ac67-2bb05addbdf4 | -7.32331 | -45.24482 | 2025-10-02 04:29:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4edf86c5-a0a2-35aa-bc0e-c71f4ca0c4d2 | -6.77556 | -45.58623 | 2025-10-02 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1fccfa38-503d-39bc-b3ad-322f85fdf3b1 | -6.29863 | -43.80948 | 2025-10-02 04:29:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8a7faed0-7d9e-384f-b718-c3d2b6dc1b69 | -7.88159 | -47.30699 | 2025-10-02 04:29:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5a49c79c-5a89-3236-82ce-114dae908236 | -10.99541 | -46.60172 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ea56f3d9-8d12-32a3-ac12-0595f9b8a498 | -11.16851 | -47.28465 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dc8c68dc-095b-3419-a55a-5339b6cd06fc | -6.63406 | -43.68736 | 2025-10-02 04:29:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 51cf9708-5a81-3073-b121-07bcf51ac6f2 | -11.6211 | -45.05505 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7d05b5c8-8f9a-33e7-be29-0cc9fa41805e | -11.59616 | -47.2305 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3243a6da-5a67-322f-89d3-a76d3cac2216 | -10.86034 | -45.41701 | 2025-10-02 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 413436c6-1212-35da-ae59-e28559957855 | -11.67241 | -47.49955 | 2025-10-02 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| de7e5367-2bd8-3a08-888f-013c8de1c4bb | -9.4575 | -45.47474 | 2025-10-02 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7bcb4671-1def-391e-a025-7d8166121bb8 | -11.87462 | -45.01914 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1cda49c6-d48e-3d5c-b7a5-5e54188297e6 | -10.42868 | -47.47545 | 2025-10-02 04:29:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0b91680e-0747-3384-aba2-21329a620459 | -11.47298 | -44.98617 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7d355def-be76-3897-997d-d8b72ba136cc | -11.86991 | -45.02661 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| bb17c35b-2d79-3743-a1fa-afdfea385f10 | -6.96974 | -45.31921 | 2025-10-02 04:29:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2cccc852-3c04-3589-ab05-e2e55f61891a | -11.12868 | -43.38401 | 2025-10-02 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ddbf7e32-9f44-3e46-8330-9b3b3e7a1cc4 | -11.43183 | -43.49616 | 2025-10-02 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 55047b52-8760-3f83-a892-264abdbd3d76 | -9.41842 | -47.35923 | 2025-10-02 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 68b61b37-396e-3d53-bb2a-02edf84f21d4 | -8.58405 | -49.60147 | 2025-10-02 04:29:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 46dbb655-5987-39c7-aabd-d41832b78050 | -11.84643 | -44.96603 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea4cabaf-de61-32b8-8853-32c270db5775 | -11.76929 | -46.85882 | 2025-10-02 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3861084a-9695-3c50-9e8f-cb4a1441536f | -11.10539 | -49.80762 | 2025-10-02 04:29:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a051e224-e258-3427-b1c9-fb2519ac4156 | -9.77018 | -47.74845 | 2025-10-02 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7012473c-e212-3be1-af68-5fa45b079b5e | -11.60246 | -45.05973 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2074e34a-dd08-3448-91af-df78e75fa396 | -6.32601 | -43.03807 | 2025-10-02 04:29:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b9534e52-30d5-3d47-84b3-fd2de7868788 | -11.82295 | -45.02759 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 842bc844-a8e5-3a37-a03a-1cc280ff7288 | -7.13104 | -45.54016 | 2025-10-02 04:29:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9b67ca91-a2ea-39d6-a0a3-265a7771e414 | -11.59601 | -45.0548 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 059a7fb3-e327-3274-b9d9-d725bb1af3a6 | -7.30021 | -42.88605 | 2025-10-02 04:29:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b5735a2d-282a-3be5-80c1-0443494e03f5 | -11.41603 | -43.49853 | 2025-10-02 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c28cbddf-3628-3ecb-8ef3-38dabe23ad60 | -10.83975 | -45.3903 | 2025-10-02 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 919b414b-2018-3c1e-9f73-3798397908cc | -10.1066 | -45.67407 | 2025-10-02 04:29:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 006c06a3-940e-3588-8e9d-12022302060c | -11.03381 | -47.81921 | 2025-10-02 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e95fb18e-6f56-31b0-9189-63e58ec691eb | -10.10999 | -45.67463 | 2025-10-02 04:29:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d9a162f9-e3af-3bf5-9901-8b4cc500dd83 | -10.95983 | -46.65427 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 421d6e9a-2642-369d-a666-a405817ee506 | -11.26667 | -47.80244 | 2025-10-02 04:29:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8d7cf404-a565-34fc-bf4d-d766a039ac96 | -9.93121 | -43.73129 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 16.1 |
| c2c3d8bb-a5fd-3b82-9e61-41957eacedae | -10.86012 | -46.57676 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7db149be-89dd-3865-9103-dfe07da8e8f9 | -8.9066 | -46.66066 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 21d8830a-12ad-3e33-9171-551af998cb97 | -8.64103 | -43.97591 | 2025-10-02 04:29:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 51aad9f3-d233-34d6-ab9e-53c58284bf58 | -10.84182 | -46.62842 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 599f4cc2-a11a-3cf4-bc5d-2584b4187486 | -9.33754 | -45.9152 | 2025-10-02 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ee4d0235-847b-3dfd-9658-dd98db1f1238 | -10.24276 | -50.31855 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 24c4d875-7e54-30b7-b3ac-f8b01fe88582 | -11.20399 | -47.1893 | 2025-10-02 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| abba402d-4187-3757-bf6d-e6f60f158b23 | -9.94673 | -43.70279 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c6b338e5-2f57-3741-bc31-b4f467bdebcc | -9.93744 | -43.71466 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d734b086-55ae-384c-bbe7-d38fc6ae2e7f | -10.83844 | -46.60608 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fab8de4a-4526-32ff-bf2d-e800ccefd2b7 | -6.77721 | -45.57561 | 2025-10-02 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 694e31bf-b832-302b-aa26-d6720df4c517 | -11.61004 | -45.03269 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 81e509c8-f67e-3859-b05c-c7a1c0974823 | -10.82643 | -47.94513 | 2025-10-02 04:29:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6ecac81f-77f8-3421-9b96-ff3ff031b526 | -11.13631 | -43.38493 | 2025-10-02 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 165cb712-df06-35e3-ac55-b58a3454d62c | -11.83942 | -45.01356 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 538efda2-58eb-3a35-a8e5-97115cbe83ce | -11.43873 | -43.50197 | 2025-10-02 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c7d522db-ed68-3e4a-8ca6-b54b04e539bc | -7.72531 | -46.21924 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| efb9229a-b8b1-3f85-9a28-632c70bd3059 | -11.52437 | -43.54578 | 2025-10-02 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8419b5e0-3e75-3b55-b07d-d5db70f340b9 | -6.00045 | -44.57571 | 2025-10-02 04:29:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 00b6199d-2d5c-37ff-a6f6-9cb58aeb1bb1 | -10.81619 | -46.61705 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6233f83b-2c6a-3b11-8869-e31b49501fd8 | -6.71892 | -44.62015 | 2025-10-02 04:29:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb2a8f9b-daf9-310a-923e-a8188d72d766 | -6.36322 | -44.64183 | 2025-10-02 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b0d64c27-9654-3174-bc87-347d09637d54 | -10.1804 | -50.24496 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 316b1292-222a-36ea-8b1a-5d864b42b4ea | -10.83069 | -46.63392 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 64cce7cc-7c33-336d-904d-d032424f04b7 | -9.93835 | -43.75877 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| da70b15d-5b80-3802-9a75-946baf2278df | -8.89136 | -45.02977 | 2025-10-02 04:29:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ef590cea-b85d-3360-be97-681e78827098 | -11.81509 | -45.00718 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8f27262f-f042-3c73-8fa9-221663011e6d | -11.80865 | -45.00208 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 92c7a180-d897-315f-92fc-8bfedb919da3 | -12.22015 | -43.76235 | 2025-10-02 04:29:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4cb9bd16-f6e8-3aea-bc0d-8f3596be6265 | -11.61818 | -45.05057 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ba42bca2-72a8-34e9-a232-4c7b57ea3674 | -9.93341 | -43.76672 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0296be1b-c8e9-3098-acfc-e9735182120d | -11.45844 | -44.96329 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c791cdb2-098d-3526-9acf-0bdf5f02e72e | -11.74764 | -42.66932 | 2025-10-02 04:29:00 | NPP-375D | IPUPIARA | BAHIA | Brasil | 2914109 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 08393661-af3a-3b8c-b7e1-afb870e49bf3 | -11.8192 | -45.0038 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 04a8dcb2-07a7-3867-9740-62a3b368edd7 | -8.71502 | -47.14601 | 2025-10-02 04:29:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cec5b509-93ce-3c62-86be-2e53aa919636 | -8.52272 | -47.2513 | 2025-10-02 04:29:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0ad69de9-ccf0-356a-8f2c-bfaa542224f4 | -11.26522 | -47.66104 | 2025-10-02 04:29:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 09064999-af27-3f8e-bc68-757d32659937 | -10.33308 | -45.26469 | 2025-10-02 04:29:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f23e88e7-1ff7-3851-afac-b7a48abe4839 | -11.46705 | -45.02556 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| db149f64-ac6c-3afb-8e60-b3dea8b483bb | -9.92211 | -43.71681 | 2025-10-02 04:29:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d2ff7883-a133-3190-91c7-845d23cc0daf | -9.93064 | -50.48815 | 2025-10-02 04:29:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6377dce2-93f6-3690-a176-71babd0a8c74 | -7.76901 | -42.535 | 2025-10-02 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| dd0357cf-7e47-3fda-b6ca-46038fe0fcf5 | -10.22537 | -50.28709 | 2025-10-02 04:29:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 568abc1f-2eb8-3c58-8bd3-f1c7f4b4a4b2 | -7.78363 | -42.52946 | 2025-10-02 04:29:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 6306bf9c-7989-3c98-8892-61d190616bd3 | -11.43729 | -43.88871 | 2025-10-02 04:29:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 67906be4-eb47-371b-a307-c258eef9100d | -11.81655 | -47.595 | 2025-10-02 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ca9f6f90-c24b-3669-a373-85ae89d16786 | -11.81608 | -44.90476 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b28bf549-f725-3923-ae71-8fcd2be3aa53 | -10.83624 | -46.62027 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| eb4e09b1-79a9-3cd4-afb4-6dd12888e7b0 | -6.60013 | -50.0388 | 2025-10-02 04:29:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e2b3c79a-90cd-3468-a6ae-e7a2f8529209 | -11.80964 | -44.89946 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 838659a0-df51-3067-9907-df31fa4b6308 | -10.22764 | -48.22762 | 2025-10-02 04:29:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9ab2d9b7-7eb1-31be-8327-0f5e73dd35b1 | -5.81926 | -45.86593 | 2025-10-02 04:29:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a20105d3-d663-33aa-8a68-70178c4eb913 | -6.3533 | -43.30115 | 2025-10-02 04:29:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 754e47d7-c01b-318b-8d26-1abf53f7d6bb | -9.45219 | -50.89799 | 2025-10-02 04:29:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 37d6e0f0-5d71-3595-84f2-971c8048e613 | -7.41237 | -45.18818 | 2025-10-02 04:29:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 972b78c9-c483-39bd-abc0-c8642fb7695a | -9.33481 | -45.70867 | 2025-10-02 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e133fcc7-3312-3a21-bf18-d4af1e2d3271 | -8.87766 | -46.5844 | 2025-10-02 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1adc5379-e238-337c-b785-6df426f38779 | -11.82055 | -44.97023 | 2025-10-02 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0665c6b5-e600-3226-8f9c-91538104c22a | -10.81674 | -46.61351 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 315bec42-11c5-3ead-9359-3e4b9d7ab247 | -10.82955 | -46.6192 | 2025-10-02 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README69.md)
