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

## Dados Diários - Página 217

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 11aa349e-4070-34f2-9bc7-8b9f2df758de | -8.8497 | -67.3946 | 2024-10-03 14:15:57 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 00bd557a-5109-3858-9e0e-3753e7e46873 | -9.0516 | -67.8525 | 2024-10-03 14:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 63608506-b87f-3025-b21e-336ec417a4a6 | -8.9791 | -67.4099 | 2024-10-03 14:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 8aa2fa57-ba47-3b41-9451-c10451e5ce86 | -9.0515 | -67.871 | 2024-10-03 14:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 69.9 |
| ed1012ab-1120-35b2-82a1-513670308034 | -9.0149 | -67.7423 | 2024-10-03 14:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 95.2 |
| c903632a-bc00-30de-9f85-af5216878a94 | -9.3832 | -68.3441 | 2024-10-03 14:16:00 | GOES-16 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 67.3 |
| f8228821-c552-3e1b-8e5e-f0d95ddbc5cb | -9.4368 | -64.5419 | 2024-10-03 14:16:00 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 64.9 |
| fe5b45aa-c204-366d-8087-a7d3fcb30a5d | -9.5824 | -50.1797 | 2024-10-03 14:16:00 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 6654f8dd-ee0d-32fe-8016-8a34ddacd9cd | -9.3648 | -68.326 | 2024-10-03 14:16:00 | GOES-16 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 839ff879-ff51-3e53-94b9-62afc96c2beb | -9.3833 | -68.3256 | 2024-10-03 14:16:00 | GOES-16 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 203.7 |
| 4a2243bc-b69a-31d0-97ee-ce4f3c3ba997 | -9.4752 | -68.5639 | 2024-10-03 14:16:01 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 48.7 |
| c23aacd6-559d-37ee-a838-19c4a429696d | -9.754 | -64.3041 | 2024-10-03 14:16:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 0d7aa0a4-9550-3095-99d4-ee0eddc8d7c4 | -9.7541 | -64.2853 | 2024-10-03 14:16:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.0 |
| e9258d6f-025c-3f97-b1ff-2942aad2d7a9 | -9.7173 | -64.2302 | 2024-10-03 14:16:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.7 |
| d61e6ea1-171f-368f-aeec-94d335105871 | -10.0418 | -48.2097 | 2024-10-03 14:16:03 | GOES-16 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 48.8 |
| b83d40b1-f633-3652-a74e-6e1ac358fa81 | -10.0229 | -48.2117 | 2024-10-03 14:16:03 | GOES-16 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 52.4 |
| e6547bf0-988f-396e-913c-cc2bbca8fe2b | -10.7168 | -46.1489 | 2024-10-03 14:16:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 5cd564c7-5286-30c8-aa4a-3641117d6dac | -10.5929 | -48.0597 | 2024-10-03 14:16:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 7ac48a89-b9eb-3927-8070-71df8bc8c822 | -10.6978 | -46.1514 | 2024-10-03 14:16:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 353c4682-04d9-3783-bbac-f551d45427ba | -10.6116 | -48.0795 | 2024-10-03 14:16:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 3121f426-a144-3b3c-ac10-89eb4f8a9140 | -10.5926 | -48.0817 | 2024-10-03 14:16:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 5b3b1c94-cb41-38ab-a8d3-67ea06230bf2 | -10.6319 | -53.6805 | 2024-10-03 14:16:07 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| c125f9d6-cf3d-3fa3-bedb-e29806ab1039 | -10.8906 | -45.9905 | 2024-10-03 14:16:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 210.5 |
| 9248b1b2-4a80-3987-9c7a-b78fb9914633 | -10.6505 | -53.6994 | 2024-10-03 14:16:07 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 8db48fa0-33cb-31b6-890f-c81313e400db | -10.7312 | -47.6904 | 2024-10-03 14:16:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 233.3 |
| 45e91cf4-6113-313f-92b1-23dcce14fd54 | -10.6317 | -53.7011 | 2024-10-03 14:16:07 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 1b689f13-11ce-328c-8b59-4ea037518e3a | -10.7319 | -47.6461 | 2024-10-03 14:16:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 262.8 |
| 569454d2-c53f-34af-a528-a700ce95ad3b | -10.7122 | -47.6927 | 2024-10-03 14:16:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 0575ad02-56f9-3371-9e92-53de1d7e2779 | -10.7315 | -47.6683 | 2024-10-03 14:16:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 150.8 |
| 6491e9e6-1eaa-3b81-a813-687378bf417a | -11.1575 | -45.9779 | 2024-10-03 14:16:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 216.0 |
| b81581c8-7a39-3e5f-80d9-e0658634df63 | -11.2779 | -43.4118 | 2024-10-03 14:16:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 104.3 |
| c254ef59-4497-30e8-ac14-ce3857e43a4b | -11.2567 | -46.9123 | 2024-10-03 14:16:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 162.4 |
| 7f254c33-47c4-36a2-af94-1a367525a665 | -11.7967 | -57.3627 | 2024-10-03 14:16:13 | GOES-16 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 52a98607-ccfa-3b69-94f4-841d2111ee0e | -11.9737 | -47.3986 | 2024-10-03 14:16:14 | GOES-16 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 4725a9e1-26f0-3b2f-8567-804c533e0ebf | -12.0128 | -47.3486 | 2024-10-03 14:16:14 | GOES-16 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 199.4 |
| aa08c8fa-68f8-3f4a-8818-43cee51520bc | -12.3292 | -54.0954 | 2024-10-03 14:16:16 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 70.1 |
| e4fa9eaa-a3d0-3a2f-a279-b83901b7af04 | -12.7812 | -50.5973 | 2024-10-03 14:16:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 44bf275e-738b-37cb-af67-7b6c1e4d615b | -12.762 | -50.5997 | 2024-10-03 14:16:18 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| bd247370-70e6-3037-a04c-9aec50a0b095 | -12.9831 | -51.129 | 2024-10-03 14:16:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 101.0 |
| f5172eba-7835-3a88-af1a-d8be1ea8e42c | -13.198 | -48.6267 | 2024-10-03 14:16:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 104.5 |
| c91b07c9-778c-334a-960d-93a35183dd41 | -13.0402 | -51.1432 | 2024-10-03 14:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 180.8 |
| f56d2c2b-349a-32fa-a3f3-5864d0af30c6 | -13.1783 | -48.6516 | 2024-10-03 14:16:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 295.4 |
| b99eba22-83f7-3fd0-ae1a-9e069a12263b | -13.1787 | -48.6295 | 2024-10-03 14:16:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 4228eac1-2b26-3c9b-9dd7-8ef7877eef06 | -13.0406 | -51.1218 | 2024-10-03 14:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 149.3 |
| b3997ba1-de06-34e4-9eb3-6dd1f1cd9961 | -13.0022 | -51.1266 | 2024-10-03 14:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 81.2 |
| ef33e1b1-20ff-3d69-92a7-42e0aad05923 | -13.1924 | -51.2097 | 2024-10-03 14:16:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 7f2dcfa1-033f-331a-bf87-0f8bdf1aac5a | -13.615 | -51.1771 | 2024-10-03 14:16:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 125.8 |
| cda42047-ea4e-330d-912e-fbacfc4bfced | -13.6146 | -51.1986 | 2024-10-03 14:16:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 514d93d6-6b17-32c5-95f2-b7589ef82fcb | -13.5565 | -51.2275 | 2024-10-03 14:16:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 6fa3da5f-7b55-3d1a-b912-f5737a60bb45 | -13.6342 | -51.1746 | 2024-10-03 14:16:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 207.1 |
| 6ece92f8-68c1-3885-9430-c5e58dae5b34 | -14.0202 | -45.0747 | 2024-10-03 14:16:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 135.6 |
| f546b15c-2982-3f09-815e-824f1d212571 | -14.0392 | -45.0947 | 2024-10-03 14:16:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 808.7 |
| a3c1dc67-a980-3b80-924d-8fe30d2eb914 | -14.503 | -45.2215 | 2024-10-03 14:16:27 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 158.1 |
| 6ad9a16a-bffc-32ed-b04f-098f7cd13083 | -14.7935 | -48.05 | 2024-10-03 14:16:29 | GOES-16 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 787f3850-45da-3691-8fb8-23ae44993c27 | -18.7663 | -43.387 | 2024-10-03 14:16:50 | GOES-16 | ALVORADA DE MINAS | MINAS GERAIS | Brasil | 3102407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 128.8 |
| a5492fcc-a8cf-3bd5-b197-6afd847e3efd | -19.0141 | -43.1998 | 2024-10-03 14:16:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 131.9 |
| 80caadde-5a0b-35a6-80a8-0224b24e39b4 | -19.2962 | -42.5779 | 2024-10-03 14:16:52 | GOES-16 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 105.6 |
| 45fd6bc5-56c6-3a1a-a223-12ce411c2d20 | -19.744 | -40.6685 | 2024-10-03 14:16:54 | GOES-16 | SÃO ROQUE DO CANAÃ | ESPÍRITO SANTO | Brasil | 3204955 | 32 | 33 | nan | nan | nan | Mata Atlântica | 141.7 |
| be003262-4738-3001-b6d3-6ff9e54708f7 | -6.1325 | -44.9199 | 2024-10-03 14:25:41 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| e1a97401-b846-3226-a952-ee471002150b | -6.2565 | -41.8538 | 2024-10-03 14:25:41 | GOES-16 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 91.2 |
| d7584883-93b2-3bf5-9b0c-a145c4ede43c | -6.1138 | -44.9213 | 2024-10-03 14:25:41 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 136.8 |
| 565c3042-53be-3823-9200-5fde1656ce46 | -6.325 | -44.3791 | 2024-10-03 14:25:42 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 48.7 |
| e7eaa5c4-29c5-3ccd-baa2-61cfceb6d281 | -6.3008 | -43.0351 | 2024-10-03 14:25:42 | GOES-16 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 9060fcce-78cd-3d07-b265-a18d12851979 | -6.6208 | -42.9836 | 2024-10-03 14:25:43 | GOES-16 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 404b4eb6-6daa-3bfc-b6e2-aa79045b300c | -6.5618 | -45.0677 | 2024-10-03 14:25:43 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| b760931c-31c8-39d2-aabc-41eef25fe25d | -6.9075 | -44.2836 | 2024-10-03 14:25:45 | GOES-16 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 2077e665-adee-35ca-a42d-1cf3594c2536 | -6.9479 | -47.6668 | 2024-10-03 14:25:45 | GOES-16 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 7d611817-39db-31ac-9d0e-941e3c92dcfd | -6.9979 | -42.9016 | 2024-10-03 14:25:45 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 82.3 |
| c8581be2-63db-3d97-a0e5-9517918e40ac | -6.8885 | -44.3083 | 2024-10-03 14:25:45 | GOES-16 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 5ab0414c-20c7-38ee-a324-f950b02ae2ba | -6.9292 | -47.6682 | 2024-10-03 14:25:45 | GOES-16 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 2dcb9320-e993-3718-abcd-e71abbb23cc2 | -6.9666 | -47.6653 | 2024-10-03 14:25:46 | GOES-16 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 2053582a-2352-367f-ab42-73ec55699cae | -6.9685 | -49.4378 | 2024-10-03 14:25:46 | GOES-16 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 112.1 |
| a10edcb1-ed4e-3f17-974c-3339a9641693 | -7.1523 | -44.2385 | 2024-10-03 14:25:46 | GOES-16 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 93.6 |
| e26c53fa-2f9e-3c8c-b18f-35609bbd6ea8 | -7.0652 | -45.3429 | 2024-10-03 14:25:46 | GOES-16 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 2e1a43d3-f6bf-3476-8597-7fb3def0eff5 | -7.5945 | -45.0222 | 2024-10-03 14:25:49 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 80a830b0-9c7d-3f57-a9dd-9f589f34a86b | -7.844 | -43.0753 | 2024-10-03 14:25:50 | GOES-16 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 53.2 |
| a135a6e8-5b20-3632-ad25-78553fca06fa | -7.8149 | -45.4782 | 2024-10-03 14:25:50 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 8f8fdabf-64b0-3ade-929e-e6ace3b7f97b | -7.7687 | -43.0598 | 2024-10-03 14:25:50 | GOES-16 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 46.3 |
| ebe6956f-9357-341e-aef6-4a684359b8b8 | -8.1759 | -43.6957 | 2024-10-03 14:25:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 204478e2-5e58-3fe5-a6f2-dff1dcf1a364 | -8.1937 | -46.8324 | 2024-10-03 14:25:52 | GOES-16 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 227.2 |
| fd49f6b8-4275-37c6-9a66-1feb14a3d983 | -8.1859 | -44.3901 | 2024-10-03 14:25:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 16b42b35-c72e-3b31-a8ff-8e53bd1c133c | -8.2239 | -44.363 | 2024-10-03 14:25:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 69.1 |
| b57f67e7-6c8a-3f09-8696-f3a8fa37261e | -8.1762 | -43.6723 | 2024-10-03 14:25:52 | GOES-16 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 82.5 |
| e10255c3-b956-3398-9219-846205bf78fa | -8.194 | -46.8102 | 2024-10-03 14:25:52 | GOES-16 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 109.5 |
| ba932e38-9daf-3dbc-af79-779dc5a340fa | -8.1752 | -46.812 | 2024-10-03 14:25:52 | GOES-16 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 48.3 |
| 0086001e-41b9-38fb-b4fd-5802820556c5 | -8.4259 | -46.2968 | 2024-10-03 14:25:54 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 133.9 |
| 3915f83a-5bd8-34de-9d72-d5bfc4ab28a8 | -8.4256 | -46.3193 | 2024-10-03 14:25:54 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| eebc0379-6781-3835-ad83-5e5d3a37b63a | -8.6113 | -46.5243 | 2024-10-03 14:25:55 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 108.6 |
| f7017bfe-2b14-365a-823c-08fcb06de4a2 | -8.7414 | -45.202 | 2024-10-03 14:25:55 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 01ccd017-5b22-3f29-8666-14b9427f6ab1 | -8.7612 | -45.1314 | 2024-10-03 14:25:55 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 82.4 |
| a2785998-d492-38cd-b93d-a70b0c2b5d81 | -8.7033 | -45.2289 | 2024-10-03 14:25:55 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 86d055e9-0174-32f3-a209-3b34f5af2cdf | -8.817 | -45.1937 | 2024-10-03 14:25:56 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 081e9f36-de6b-33a8-aa1c-53e271804408 | -8.7896 | -68.8 | 2024-10-03 14:25:57 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 43.0 |
| b8734f14-e14c-3461-bfcc-ae79dc43b4c6 | -8.9674 | -45.2456 | 2024-10-03 14:25:57 | GOES-16 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 84.4 |
| be27d8aa-003b-3fdb-b255-a957c6758de9 | -9.0515 | -67.871 | 2024-10-03 14:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 9919a553-a289-3306-b6de-912017785056 | -9.2573 | -43.4771 | 2024-10-03 14:25:58 | GOES-16 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 58.0 |
| 4d1a68f8-ef74-3d75-a11e-e64685ade336 | -8.9792 | -67.3914 | 2024-10-03 14:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 7c3a68c4-aa17-3643-a3dd-c481e44aa1f7 | -8.9976 | -67.4094 | 2024-10-03 14:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 43.2 |
| e7503be9-1b20-32c6-80b9-714c2fdecc94 | -9.257 | -43.5006 | 2024-10-03 14:25:58 | GOES-16 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 63.9 |
| 94cd1b9c-84c3-359d-ac73-941fae47a6db | -8.9791 | -67.4099 | 2024-10-03 14:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |


[Clique aqui para ver as próximas entradas](README218.md)
