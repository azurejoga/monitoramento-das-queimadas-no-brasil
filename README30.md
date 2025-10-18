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
| e5ca4fa8-2a0c-384d-90b0-60f41bf6f18f | -11.37964 | -44.24343 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9c79533e-f20c-3301-95fb-c0867c63baef | -12.22096 | -42.24452 | 2025-10-18 04:02:00 | NOAA-21 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| b36babc8-2f14-3d22-8776-5e0d02f55aca | -13.68335 | -43.85762 | 2025-10-18 04:02:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e55e3323-c0af-30d2-8a99-1e610774b869 | -13.76651 | -48.22821 | 2025-10-18 04:02:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6c461419-5604-3ece-b315-dac34ed49f20 | -9.88933 | -47.65181 | 2025-10-18 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a8e0192d-a360-3efa-b323-6f6e89c21e71 | -12.15408 | -45.0719 | 2025-10-18 04:02:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0207e223-425f-3c2e-9f16-21f76afbace1 | -8.39613 | -39.71209 | 2025-10-18 04:02:00 | NOAA-21 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7c0a4d89-36e2-393f-bd8e-eaeab2bd1882 | -13.0827 | -43.06448 | 2025-10-18 04:02:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 1e05ec38-44c7-3da2-beb1-56a127794cff | -10.96718 | -45.4661 | 2025-10-18 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 96aba2e6-730f-3ec6-87f5-f223c7262ddb | -8.38554 | -46.23776 | 2025-10-18 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 612efe81-4243-33df-bd1e-5597923a4af1 | -11.36717 | -45.26111 | 2025-10-18 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 79bf223b-3a94-3f6d-a0ed-ee963bd886a3 | -7.45679 | -42.16388 | 2025-10-18 04:02:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8b77b506-fdd6-3014-90a3-890224670843 | -10.59659 | -48.00388 | 2025-10-18 04:02:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f27fe3fc-8ca4-3486-ae6d-91af7f1f58a5 | -10.48565 | -43.41597 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 13b72ecf-7065-32d8-9bcb-cfc10dad0bd2 | -11.36968 | -44.28083 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0614129c-b463-3e04-8f10-8289adfd11e6 | -7.46586 | -42.173 | 2025-10-18 04:02:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c12fb57e-f5db-397d-8845-88e283e1be43 | -9.78355 | -42.02995 | 2025-10-18 04:02:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 43d44e4c-0b1f-30ff-aad8-a86d9c1a0993 | -6.58601 | -47.07535 | 2025-10-18 04:02:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4b864c34-6643-3397-b9f9-af0cc051479d | -11.63907 | -47.85593 | 2025-10-18 04:02:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4a75ed0f-63bc-3c21-9377-0a6e6aebeea5 | -9.7226 | -44.56376 | 2025-10-18 04:02:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e61cc381-a43f-3c26-81d1-e9da16cc3e5d | -10.24964 | -44.06187 | 2025-10-18 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 181a4bc2-a0d0-3a7b-a22d-e17181312a9e | -7.24631 | -49.517 | 2025-10-18 04:02:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 234732ef-0285-3c71-b9bc-bf8236070b43 | -10.64796 | -39.9293 | 2025-10-18 04:02:00 | NOAA-21 | ITIÚBA | BAHIA | Brasil | 2917003 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a415c1e9-2979-3ed1-b6b9-5b0de5f84958 | -10.14671 | -44.58654 | 2025-10-18 04:02:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a79a2331-cb36-3176-b077-3ff82019f98b | -10.43199 | -45.01829 | 2025-10-18 04:02:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9fa02148-e97e-38e3-9c59-4579c45f4f53 | -7.99428 | -44.15672 | 2025-10-18 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f2ed4605-518e-3f27-ab47-2b0a85718ac8 | -13.03405 | -46.95056 | 2025-10-18 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7b67b325-863f-360c-bd7d-7a5a47a1fa95 | -7.36762 | -44.2304 | 2025-10-18 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 825aa791-e6f5-35d3-b01b-3d07f36df5aa | -7.47109 | -42.7479 | 2025-10-18 04:02:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 28ba2192-c656-3202-b501-61c1c00bbbf0 | -11.36749 | -44.27176 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cbd87384-c952-34c1-8107-d16cb4324d8e | -10.49341 | -47.73946 | 2025-10-18 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 44d4f202-e7e7-30b4-b488-5a53a62f0074 | -6.79093 | -46.47269 | 2025-10-18 04:02:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9d1cc652-6bc4-30c5-ba50-ee17202cf6d4 | -10.4328 | -45.01359 | 2025-10-18 04:02:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3b12223e-6d06-3547-9dce-1ad0543f9a87 | -8.20272 | -43.96245 | 2025-10-18 04:02:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6c9de30c-9417-3b43-816e-41ae3584e634 | -12.79055 | -48.6268 | 2025-10-18 04:02:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 33da42dc-8ac4-30a4-a3a2-fc9b121a0499 | -8.19678 | -43.31039 | 2025-10-18 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 86c4bb83-f234-38cc-9909-7ebf3da3f416 | -11.40492 | -44.26949 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 87cebdca-78aa-3d6e-a3ca-da4e214891e5 | -10.99967 | -47.91476 | 2025-10-18 04:02:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 86de9666-4575-3536-ac7f-86a9356178cc | -6.93304 | -43.69138 | 2025-10-18 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9254c5a3-1448-328e-bb74-7468f66c8ad0 | -13.69941 | -47.65409 | 2025-10-18 04:02:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86d887d4-d1ed-3e4d-b9ec-5316c054bb5c | -8.61337 | -40.19847 | 2025-10-18 04:02:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 489e550d-b75c-372b-9231-a4c4a7a1d023 | -10.68296 | -44.56752 | 2025-10-18 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6ef7e00b-7187-3179-a050-0e249e584f0f | -10.58043 | -47.38651 | 2025-10-18 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1c819299-d46a-3d0b-b9c4-641fce1ae92b | -6.93673 | -43.69197 | 2025-10-18 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 47e78a4c-5a82-3586-8538-347298a851d2 | -11.46644 | -44.0258 | 2025-10-18 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b0f3a136-2dc0-3294-840b-cffe05c0db01 | -10.13948 | -44.53815 | 2025-10-18 04:02:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ec8d791f-7d4a-35fe-ac3e-e61ed7e21536 | -14.28258 | -44.65912 | 2025-10-18 04:02:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa5d4149-d623-3ad8-b5b7-b62eb2553eee | -13.62891 | -43.95669 | 2025-10-18 04:02:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 440b424c-ee94-39f3-ad07-1cb6fc470a31 | -12.7974 | -44.19583 | 2025-10-18 04:02:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d8fcfc32-bee1-3887-abbc-d259cc807d9f | -8.23095 | -43.31913 | 2025-10-18 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 5fb32934-625f-34d1-90f4-fbd0fc47dce1 | -12.73008 | -43.00901 | 2025-10-18 04:02:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 70d2b9b8-e03e-3116-9f81-63bcec218e14 | -12.42995 | -47.79324 | 2025-10-18 04:02:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 90486b26-f277-36be-937b-0f3c7f339424 | -10.29282 | -44.0259 | 2025-10-18 04:02:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6041aeec-eee7-3575-a0de-e266618a1419 | -10.16858 | -46.59492 | 2025-10-18 04:02:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 36d0c79a-a1b2-3fac-bdff-5aa4a002a742 | -8.94835 | -49.0216 | 2025-10-18 04:02:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35a641d5-164f-3de0-8e29-6ad544c06115 | -6.88883 | -45.45338 | 2025-10-18 04:02:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8ae196f7-83f5-37d2-9f10-cc01d9b5a691 | -13.04498 | -46.96057 | 2025-10-18 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8e8130c5-aeec-3b6b-8e9f-f4c69117b8ef | -11.36071 | -45.25742 | 2025-10-18 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a2795ee1-c940-3083-8691-af54a75e8f12 | -7.39744 | -46.97054 | 2025-10-18 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 33379304-3eca-3206-b673-62aaacdac477 | -10.69332 | -44.55094 | 2025-10-18 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 782abf65-e502-341d-9a0e-0eae7fc5066f | -8.26479 | -44.02273 | 2025-10-18 04:02:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1612bf96-a308-3711-b620-8ca02d7d64c1 | -8.16108 | -43.30465 | 2025-10-18 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b4dca1bc-abb9-32b4-a3d4-27441f96f90e | -12.99163 | -48.46102 | 2025-10-18 04:02:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7cd791e6-4736-32cd-b286-d6c4374326b7 | -10.80812 | -44.01439 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| af03a265-9433-3093-b329-1ddc056a4b8a | -11.49987 | -44.17632 | 2025-10-18 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d9e725a-5830-35b0-8f25-e8979e92473b | -13.77819 | -48.23933 | 2025-10-18 04:02:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9910b0fd-d1fe-3843-aacd-ba2b2a815003 | -13.76861 | -48.24181 | 2025-10-18 04:02:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| da9a3b25-24b0-3894-b57b-fa43fc62067a | -13.77099 | -48.22867 | 2025-10-18 04:02:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 87828cf6-5895-3cc0-b3f0-1f48747e9603 | -11.3465 | -44.22045 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d0ab8c87-a2f6-3edd-9892-857d56965999 | -8.56713 | -45.42565 | 2025-10-18 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 78a23a36-8414-3dbb-a616-35ae56bdf41e | -8.09515 | -45.44624 | 2025-10-18 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 43ab43dc-f5f9-3279-8a9a-3859fd125fe2 | -9.67098 | -44.55054 | 2025-10-18 04:02:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dd1d8067-3410-31ad-8faa-120911528d68 | -7.44453 | -44.7435 | 2025-10-18 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| deccbc8a-30f9-3e63-8001-e87ea7010142 | -8.85839 | -49.8911 | 2025-10-18 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 95a2b27c-2bea-38e4-9e49-76401675d4c9 | -9.68296 | -44.54789 | 2025-10-18 04:02:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cbf3adf7-a02c-36ad-8108-f50e80f9852a | -6.94487 | -43.68872 | 2025-10-18 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 74223a79-1f33-3497-a6b3-cc1687e0f787 | -10.92782 | -47.97507 | 2025-10-18 04:02:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4863d04a-574a-3ecb-bc11-fda8220fdea6 | -10.52459 | -43.39769 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 34207e10-8ba9-3471-b1d9-2bf6b56369bb | -10.47945 | -43.43155 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 44c48ae1-5e50-3b00-8ee5-6b9238c18f80 | -10.11863 | -44.54865 | 2025-10-18 04:02:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c9153607-7244-3be6-9d1b-af27c0d32c03 | -10.97906 | -47.92528 | 2025-10-18 04:02:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3b1fa0dd-88b7-356f-88a6-abf3ef877b6d | -14.13201 | -44.70997 | 2025-10-18 04:02:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a1bafb20-f6dc-3fbe-8d66-3443726bf735 | -10.82108 | -43.9295 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6e31afd9-a343-3cb2-884f-f800c8206b51 | -13.43471 | -47.98225 | 2025-10-18 04:02:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f816200f-4941-3238-a5c9-26a463324203 | -7.14567 | -46.41282 | 2025-10-18 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| dcbc0bee-60bc-3487-bfde-ea00645a811b | -11.20707 | -43.99303 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6574520c-7827-3d66-a0e8-5e4cb1ab7b63 | -11.37694 | -45.27251 | 2025-10-18 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7d0fe0cc-eb45-3c72-8ffe-4a3eccb7f0a3 | -10.24168 | -44.03538 | 2025-10-18 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 22752b21-f637-34f1-ad1c-488b01341892 | -8.25102 | -43.33081 | 2025-10-18 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| bc491ba9-df2a-3183-a3b0-94728431aad0 | -9.71388 | -43.59859 | 2025-10-18 04:02:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7f538126-7fc1-31c9-8e57-01c9d8dfcbbe | -10.2389 | -44.05225 | 2025-10-18 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fb8eca86-0df4-3cd3-be41-2de551ba15df | -11.48992 | -44.19181 | 2025-10-18 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b18488cd-3aa4-3752-abc4-722a9342ad4c | -12.98181 | -47.11092 | 2025-10-18 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1bdc2ed1-3168-3b5a-8ca6-97be0d92c42d | -13.20179 | -48.31717 | 2025-10-18 04:02:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0067e2a4-f3e9-38d5-9c06-7757bf554abf | -10.22797 | -49.68514 | 2025-10-18 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2d05d30c-684a-390b-a57e-80056a150b64 | -9.25699 | -43.74697 | 2025-10-18 04:02:00 | NOAA-21 | GUARIBAS | PIAUÍ | Brasil | 2204550 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a156a483-453c-3c47-b52e-0d9f36a6b2da | -11.60748 | -44.07424 | 2025-10-18 04:02:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 8e36c758-12fe-36ea-b88d-39e0024c34dc | -10.98414 | -44.31918 | 2025-10-18 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 40d793c0-806d-3f61-a643-b498676b732c | -11.47987 | -44.01121 | 2025-10-18 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bd8f6dc5-6142-3139-b5a3-b2c9c9e23e3e | -11.34721 | -44.21624 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README31.md)
