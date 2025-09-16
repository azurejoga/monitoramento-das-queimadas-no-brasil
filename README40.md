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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ff7ca6a0-9241-34fd-af8c-538f9a94a25b | -8.60375 | -45.74125 | 2025-09-16 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6bf51c29-2f3c-3416-bac3-08915f196b8f | -7.72668 | -45.30568 | 2025-09-16 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 20ea9684-faad-31ff-81fd-8cdc143ca136 | -11.27711 | -50.80574 | 2025-09-16 04:29:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9e6f0592-7b76-3683-a85e-55b83f6adabb | -11.72631 | -46.48105 | 2025-09-16 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 080fc0f9-191a-31da-bbca-7dfba7900c4a | -8.91399 | -46.15258 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6863f65f-17cd-3e88-b08b-7020dd39b597 | -8.08846 | -50.16355 | 2025-09-16 04:29:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 16819013-2598-30af-8ae6-bff976adb2b2 | -7.19592 | -48.60679 | 2025-09-16 04:29:00 | NPP-375D | MURICILÂNDIA | TOCANTINS | Brasil | 1713957 | 17 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 80274ef5-23bf-3d7a-8962-db3897417a49 | -10.64746 | -46.22021 | 2025-09-16 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d592b70b-2003-3544-8083-5d92a2a0256d | -7.68952 | -44.66342 | 2025-09-16 04:29:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 22eeeec6-a300-37a2-bba5-edc30c4d8ebb | -11.4265 | -46.92973 | 2025-09-16 04:29:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0bcea051-220a-3672-a497-0bf0c13b954c | -10.6593 | -48.76226 | 2025-09-16 04:29:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1c6741f5-e32f-3bfd-a90d-4af3c62ed470 | -8.00535 | -45.67047 | 2025-09-16 04:29:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5431b9cb-7960-319c-a261-32c8bee05012 | -12.06007 | -46.55488 | 2025-09-16 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8770cb2c-9b15-3c49-995c-2ea39268ae1e | -11.1168 | -45.33958 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e5b24acd-13cb-3ef8-a554-f1e6f3788cb0 | -7.52275 | -47.65812 | 2025-09-16 04:29:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7472a647-58b7-30bb-b6a4-5ee11242a960 | -12.69361 | -47.73187 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| befc5819-a3e3-32c5-a283-db4188fa88c8 | -12.79211 | -47.25713 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7541e98f-24ff-3b70-9179-24a970357080 | -7.66371 | -45.14858 | 2025-09-16 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a0252485-02aa-3866-bfdc-2b41ef7c360f | -8.97402 | -45.03815 | 2025-09-16 04:29:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86b4e8a8-afe3-3bca-96a0-70622bf1f70f | -8.33706 | -47.56236 | 2025-09-16 04:29:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 87dbd298-63e9-3f3e-927b-811cf9a4b30a | -7.97615 | -45.6691 | 2025-09-16 04:29:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b7d89a1a-dd85-34cd-ade0-d3f05a8d8316 | -12.6705 | -47.94242 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 90b7ad05-2c5a-320b-a470-995aaea8a659 | -12.79268 | -47.18783 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 85440271-c178-3390-9591-cff53d8a6e51 | -8.12322 | -48.26633 | 2025-09-16 04:29:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 57783eca-cc60-3671-a41f-1948aff69b91 | -9.09563 | -44.85351 | 2025-09-16 04:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0f55dc40-cd21-36fa-b2fa-80af27cd786e | -11.70819 | -46.87661 | 2025-09-16 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 72209834-d55b-361b-b7f2-30fcbcf993bc | -11.04371 | -48.27107 | 2025-09-16 04:29:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f7d1847a-a5fe-38bd-8355-fe6a17860ea8 | -9.15321 | -46.98022 | 2025-09-16 04:29:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6efec7b1-61f8-36ae-a641-e75e50d1905b | -11.12141 | -45.35577 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2e8039e9-995a-3199-bc4a-c0478f8c122a | -12.82769 | -47.22641 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 803f7dfa-fdb0-31af-8e32-bae3ca39329b | -10.73043 | -44.74879 | 2025-09-16 04:29:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d07e5120-c3b2-327e-a3e5-2854a9a17ce2 | -12.67532 | -48.01962 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 492d7a21-818b-3c2e-b8d5-efdb3f00a613 | -7.95659 | -45.66234 | 2025-09-16 04:29:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c58183de-cb29-3a2f-9580-640b5e604bfc | -8.95351 | -45.8758 | 2025-09-16 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dbbd0b43-7784-3b9b-b04a-fa5b993b2924 | -13.00794 | -47.94672 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2136e4dd-e247-3158-b7cf-5cd855b38e15 | -7.4429 | -46.17913 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c7e04c1a-ba08-34ed-918a-fde4e808d086 | -10.71843 | -44.75565 | 2025-09-16 04:29:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d36faa60-1c47-3ece-885d-12ad738b82bd | -7.68905 | -44.50597 | 2025-09-16 04:29:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cfa0d714-807f-37b5-b472-9f55e08fe82b | -10.88306 | -47.78136 | 2025-09-16 04:29:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b58dd7a5-80db-3a66-81a5-80f037da6a66 | -12.85956 | -47.14363 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1091a450-6fbd-32b2-841c-074f0d7abfa8 | -8.95774 | -46.0256 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0486d1b6-8719-3fea-bfa9-6fd2a5681b32 | -11.11393 | -45.33524 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f125ff8-bf9f-3d60-b953-0f62985afbe2 | -12.10462 | -44.82309 | 2025-09-16 04:29:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 355fbb08-7957-3964-b6fe-ff66df10e0d2 | -7.52949 | -47.65921 | 2025-09-16 04:29:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c95eee3-7c76-3edd-8a48-157e019d6360 | -11.7401 | -43.37761 | 2025-09-16 04:29:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 65dd68da-04a4-3f37-8b81-d8d768875b0d | -7.82948 | -46.12562 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a7f9ff2e-ba36-399a-948f-a10f3c9e5f44 | -12.75966 | -47.97489 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 03108c24-db93-3216-8ba0-ea1cebf291c1 | -12.11241 | -44.83492 | 2025-09-16 04:29:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a281873f-18d2-3a75-b586-d44afccf82a3 | -13.05868 | -50.08299 | 2025-09-16 04:29:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 10530d0a-858b-3b82-b27a-dc428a5ab4e5 | -7.40656 | -49.98237 | 2025-09-16 04:29:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 51d7747d-e548-3d70-941b-837e54bed1bb | -11.43039 | -46.92671 | 2025-09-16 04:29:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5d8cb7d0-e90f-3a97-9a98-a9b04a3b5614 | -12.4436 | -49.70219 | 2025-09-16 04:29:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6e369a81-ac4f-3a4d-a4e1-d9200ef7e136 | -8.99812 | -47.0378 | 2025-09-16 04:29:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2c947bf8-bd15-3b4a-82b7-24b7653af360 | -7.69021 | -44.4984 | 2025-09-16 04:29:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 56ff33c4-ea16-31d8-953c-ec969f156b87 | -11.72296 | -46.48052 | 2025-09-16 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 881a1f33-ff7e-3a32-bc39-9e1b8ca1a6e2 | -11.35449 | -47.34478 | 2025-09-16 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 69e0d286-c853-39e3-aec6-e49fdbc81ee2 | -8.6124 | -46.40008 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 389783d7-6c44-3bad-ac9b-fb7d7ced7908 | -8.66945 | -46.37664 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| f7dca4ed-c372-32a2-8db9-74f272a77a5d | -9.05065 | -44.8355 | 2025-09-16 04:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a3eeff3c-cd39-3244-84d5-ddc8c1d3a333 | -9.09965 | -44.85027 | 2025-09-16 04:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c1093dd1-a196-3699-8a0b-b5a936e52c8d | -10.1422 | -46.14862 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fea9ab11-39ba-362b-b12d-c8eae1f26ed8 | -7.67631 | -46.28782 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 14500112-8691-3a1d-8009-474aa6e2d398 | -8.8811 | -46.19772 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0c67074a-6514-321a-9531-6708e5ae1bf9 | -9.46209 | -48.58331 | 2025-09-16 04:29:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| da75f100-58ec-317d-9540-0dc6920399a8 | -9.4649 | -48.58755 | 2025-09-16 04:29:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6d0db8ff-dea2-3060-8bb5-a9f691702e15 | -7.62849 | -46.54793 | 2025-09-16 04:29:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b5e03056-d972-30a0-b42d-ee6aeb294ca2 | -10.83862 | -42.80133 | 2025-09-16 04:29:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d1c81642-ee85-3986-8b47-f54ac148dd10 | -9.45171 | -48.60423 | 2025-09-16 04:29:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 91484e4b-0385-32d6-8edf-a5c64589afcf | -12.92817 | -47.96242 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 58883345-b362-3be4-b390-7739d1a9e8c3 | -11.1082 | -45.3498 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| cacd1808-c155-3eda-9179-bb152cdc57d0 | -7.14164 | -47.98565 | 2025-09-16 04:29:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 767957c4-07a6-334e-9938-4c5e94da49f2 | -12.64105 | -47.95576 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 568e8c2a-4306-38c7-818c-9c2929000186 | -8.58625 | -46.3493 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 52543090-829d-3f8a-b737-cfb237765de3 | -11.32252 | -50.87211 | 2025-09-16 04:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 756b0a2b-e5bb-306c-bbba-578c24f19fc9 | -10.74273 | -44.76288 | 2025-09-16 04:29:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3f2df13c-b66d-3be9-96be-4788b21e849a | -7.71587 | -44.78535 | 2025-09-16 04:29:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ea38ffbb-b120-36fd-92f3-bafaf67e369f | -11.3999 | -43.6829 | 2025-09-16 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 21c52871-9e8e-3450-9efe-b2cfca4ee80e | -12.12301 | -44.81199 | 2025-09-16 04:29:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b4a1453e-b1b6-383b-8032-8cd3ca486c0d | -7.39932 | -50.00351 | 2025-09-16 04:29:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8268f0b9-86bf-3039-800d-f6f8f80a0cf6 | -7.48607 | -46.12159 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7b07bd28-5540-3eda-aae1-50e7591d1a39 | -7.69295 | -44.66398 | 2025-09-16 04:29:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d2611172-013f-332f-ae4e-178ec5b0711b | -8.20069 | -45.55095 | 2025-09-16 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8cbff71b-d3e7-32ae-be5e-09a46439acd4 | -8.96667 | -46.0343 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 14c5a75e-8157-303a-9820-6408ecf32d5b | -10.65173 | -46.45828 | 2025-09-16 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3d5c368e-943a-3cd7-b059-c0e35a5a3dce | -11.70265 | -46.89016 | 2025-09-16 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 20b59b86-f044-39f0-a332-33d51c9d50bd | -13.20361 | -47.30505 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d72473a8-5b4f-3673-a1b0-a5d221167740 | -8.39481 | -47.25727 | 2025-09-16 04:29:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b58a134f-4e09-3a70-b243-b71e9ac90b49 | -8.61684 | -46.3936 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aa7185b8-bdd0-3cdb-9524-bdfda12a50f8 | -8.60177 | -46.33741 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4364e4f8-5f53-3ef1-b5a4-ca01e92e7517 | -12.54887 | -45.63432 | 2025-09-16 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6bf20e06-1da1-3bd8-a128-5d6366d01e29 | -13.00738 | -47.95026 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9bb00b89-9897-3446-aaba-cba88b7cd20b | -7.94822 | -45.67196 | 2025-09-16 04:29:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| effa609d-5b12-331d-afc0-487d7f9cabbd | -8.20461 | -45.54792 | 2025-09-16 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 097b1dc2-0424-32f4-8544-66af42dd14a2 | -10.47609 | -45.17451 | 2025-09-16 04:29:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 82b064de-4086-3478-a920-13218a47cc95 | -12.66421 | -47.72342 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d0ffcbcd-9f29-32cc-91fe-9eaeae48a63a | -12.544 | -45.87827 | 2025-09-16 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 282b881d-9e90-3f6c-b03a-6555dda00a5d | -9.09738 | -44.86527 | 2025-09-16 04:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 9f51e694-e85b-3947-b729-b5d6d24d4c7c | -8.41543 | -47.21383 | 2025-09-16 04:29:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| de18c6a7-7990-31fc-98c4-f52d68c8c95a | -7.4051 | -50.00227 | 2025-09-16 04:29:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f4eac0f7-b392-3866-8cfb-e2e76690618b | -13.19639 | -47.30747 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README41.md)
