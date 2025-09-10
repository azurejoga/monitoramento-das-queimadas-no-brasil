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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f0df1f19-6e24-32ab-90d0-b89933e5b83b | -7.86481 | -46.25119 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 849c8124-1ed8-30e7-b3a4-c420adebfc33 | -11.4672 | -49.24706 | 2025-09-10 04:42:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b652d9e2-b12e-3d06-8e24-0973b6462ddf | -11.46665 | -49.25068 | 2025-09-10 04:42:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2705502f-630b-3f14-b4a6-e7d3e072262f | -11.4591 | -50.32529 | 2025-09-10 04:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8496f57b-7ad3-3d5c-b997-1a9e03211c49 | -9.31401 | -46.726 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 860b0dc3-185c-36b1-937b-346feb3fdb93 | -7.84024 | -45.40813 | 2025-09-10 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5a123352-6c67-311e-9bda-40befca5c3d1 | -7.88853 | -46.25708 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7662fd9c-8d45-352f-a732-caf01654b37c | -12.1384 | -44.84095 | 2025-09-10 04:42:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f2c1f49b-a7c1-3668-b452-28b648585c55 | -9.69351 | -46.80463 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f9516756-fa75-381c-8d95-b329a0607576 | -11.1254 | -45.11565 | 2025-09-10 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 907dc51c-7fc8-3aae-81b3-f29b34f149ac | -9.05754 | -45.73177 | 2025-09-10 04:42:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 19e3e589-5736-305b-94f2-2b745c3ccbaa | -10.01165 | -48.09054 | 2025-09-10 04:42:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3d7b5c29-8a7f-3554-83c2-966ab7371646 | -9.09625 | -46.96817 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 43a882c0-ab84-3bc5-9b0f-48e0f10e684e | -7.10585 | -50.76429 | 2025-09-10 04:42:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bddd451d-78e6-365a-8e00-c9dd217d8f10 | -9.7621 | -51.12234 | 2025-09-10 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7be31b8c-5d48-3c9e-a708-cee399df7c0f | -7.55809 | -48.22478 | 2025-09-10 04:42:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 018549ce-3fc1-3d80-bd28-312e27d46d8d | -6.68638 | -51.4135 | 2025-09-10 04:42:00 | NPP-375D | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 75ceb5ad-493a-3ae2-af28-cd93f6c1c0e3 | -6.85564 | -47.89452 | 2025-09-10 04:42:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 697ae818-21b9-32b9-83e6-8757c299fb9d | -10.72879 | -48.3014 | 2025-09-10 04:42:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 46bf3eed-0e5e-3d16-9693-8763f3236ff2 | -6.42632 | -44.43801 | 2025-09-10 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| efa9cd80-4496-3637-ada2-61cfa33fbadd | -9.08051 | -46.97497 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| df092bce-3d9b-34af-9715-5dd43005f4b9 | -8.16206 | -46.06952 | 2025-09-10 04:42:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 12dca4bf-b718-3cf0-bcda-ddfa4805adc5 | -10.96869 | -46.79943 | 2025-09-10 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b88557db-55da-39c5-935a-a69bbed0248c | -9.68765 | -46.86922 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 45152e17-0a5f-30f8-bc98-9c5a37eea9dd | -7.07331 | -43.91575 | 2025-09-10 04:42:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a9aaf375-2169-3e01-8b19-0a5f43b00a89 | -8.47935 | -47.29515 | 2025-09-10 04:42:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0091e338-57f5-32a8-8de3-d49cdafe0963 | -7.74103 | -50.72665 | 2025-09-10 04:42:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee92c945-bde5-305a-8630-7ea1be55aa63 | -9.80889 | -47.76392 | 2025-09-10 04:42:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9a99cf61-ad8e-33c7-b472-b1d26737a1a3 | -11.46531 | -43.63356 | 2025-09-10 04:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d479fe66-2504-3223-87c4-b87b55fdd9e8 | -11.49492 | -50.41772 | 2025-09-10 04:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a1d9c623-2717-3f3a-ad2d-b563ea7817f9 | -9.2171 | -50.55504 | 2025-09-10 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef1abd59-c81d-3999-8cef-78e7254b3b71 | -7.08804 | -44.13707 | 2025-09-10 04:42:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| be6f4659-1a6e-3650-a22b-4fd7892ed251 | -10.00531 | -48.08555 | 2025-09-10 04:42:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 180fe8c2-59d6-3669-b8f8-d5b8657b01f4 | -10.57141 | -52.01364 | 2025-09-10 04:42:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef18719a-bd88-3e7e-92ba-0c02027f79f5 | -10.74663 | -48.1823 | 2025-09-10 04:42:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed67085f-b3d8-3463-9be8-063f5e9bb948 | -10.73178 | -48.46886 | 2025-09-10 04:42:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a08a5200-ecdb-3949-8d59-595ac8b249e2 | -10.01666 | -51.66645 | 2025-09-10 04:42:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f2b5dc9-4f2f-3d0d-b113-44e0c081ac6c | -9.06785 | -46.98588 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 850948a3-64e9-3232-b1ac-a14a08a5d48c | -10.01314 | -51.68815 | 2025-09-10 04:42:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9aac42e5-6390-376a-9821-526e047999f6 | -7.77853 | -46.05629 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7c1950c7-5c8a-3d46-924d-2699e44e52e1 | -9.77525 | -48.34137 | 2025-09-10 04:42:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e769d6e7-e56a-36e2-ace8-5c6bf256bd2a | -11.66512 | -46.9057 | 2025-09-10 04:42:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ea855dcd-c695-3c08-a19b-dce17cf1d548 | -9.10227 | -46.97734 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 522f9233-5de7-3d2c-b1b2-dc8fc651066a | -10.38889 | -50.54622 | 2025-09-10 04:42:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| a13d528c-122c-3ec8-99cc-cbfa55797e87 | -9.00536 | -49.79978 | 2025-09-10 04:42:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ff233347-f3c3-39af-8932-599e3b8c1753 | -6.44284 | -47.0261 | 2025-09-10 04:42:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6bd588d4-c8d9-3dd9-96ee-a238c2aff066 | -11.66529 | -46.89917 | 2025-09-10 04:42:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bcbf23d8-78fd-31d0-b2e1-04fce458bdb8 | -9.06969 | -46.97338 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ce6d7b83-c884-3e08-aba6-88ec45b51391 | -7.70336 | -44.84579 | 2025-09-10 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| cdecdff9-5250-36d3-9d2b-a0bbb43e940c | -9.03141 | -49.786 | 2025-09-10 04:42:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a48549ae-9b9c-3a9a-9bbc-6727b6f77224 | -9.55546 | -48.29648 | 2025-09-10 04:42:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0d45b1a0-2929-3e1f-90c5-d38c7b574906 | -10.88496 | -55.69342 | 2025-09-10 04:42:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6319789f-bab2-39f2-be7b-6f8cbac49273 | -6.85281 | -47.93507 | 2025-09-10 04:42:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 90d16460-3b21-3730-bd15-260f804d16a1 | -9.10165 | -46.98148 | 2025-09-10 04:42:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f7f8034a-b354-340e-ac11-feb536415506 | -11.24388 | -49.40555 | 2025-09-10 04:42:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c66b1e5c-3179-3942-b9e7-4cd30bd3f804 | -9.01161 | -49.54242 | 2025-09-10 04:42:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6ac27d84-3b2d-3685-b42e-01d3501ef631 | -12.41497 | -44.71801 | 2025-09-10 04:42:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e39165bb-d42f-3101-92b0-3fc8f6511e89 | -10.16037 | -48.8755 | 2025-09-10 04:42:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9693434e-4790-3d5b-b2c0-cb8a091b4797 | -9.06382 | -46.98258 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 90dd1c6d-fd14-3440-a55c-f7cb3ae05e45 | -8.05587 | -52.33313 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 38731f57-a785-3006-aed6-9234fab53d18 | -9.21324 | -50.53639 | 2025-09-10 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ca7a6fa-8891-34e5-9880-2ad8f1e527eb | -9.06445 | -46.97842 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9b045f60-ed5c-398f-9528-ea3e412b1c59 | -11.11351 | -48.41339 | 2025-09-10 04:42:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d5b1b5f2-4e3a-3017-b9dd-1a509925a7a0 | -11.44951 | -43.6123 | 2025-09-10 04:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6776b60f-f8ad-3c77-b637-c726037a8661 | -12.08386 | -45.47261 | 2025-09-10 04:42:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ae755e72-0b15-3c38-923f-f57074df79bc | -8.09944 | -44.85532 | 2025-09-10 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 51e46456-999f-39fa-bc2b-3c065c44acb4 | -7.56207 | -48.26612 | 2025-09-10 04:42:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 11464e7e-cab2-3e1f-b1e9-e63dcc87d3c3 | -7.66597 | -50.27032 | 2025-09-10 04:42:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 79bf567b-a9ec-3974-a49b-0b7bd9a86114 | -7.07141 | -44.86244 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d757731-d26a-3b3e-a549-d1534021a111 | -8.04125 | -48.66016 | 2025-09-10 04:42:00 | NPP-375D | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b625b4d8-9ac7-3dc4-8a3e-675b169daf2f | -10.5652 | -49.44309 | 2025-09-10 04:42:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f75fcd0b-eaca-3052-9c96-d80b6ce5ae94 | -10.47191 | -47.94822 | 2025-09-10 04:42:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| bf22df97-b328-3f1e-a77e-33200d4f444f | -6.44633 | -47.02665 | 2025-09-10 04:42:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 94d305b4-2706-378a-b711-da95d39fb036 | -11.65954 | -46.89129 | 2025-09-10 04:42:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e96d5890-45cd-3b11-b070-90ffb7a9ed8a | -8.74308 | -47.09479 | 2025-09-10 04:42:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bc8fbb86-7fdf-3ba2-9d98-d33df0249417 | -6.84757 | -44.91892 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0be011ee-e3e1-3047-a146-e528c9dbcdd1 | -9.084 | -50.45462 | 2025-09-10 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6103dc09-29ef-3187-82b2-3cd322eca708 | -11.46467 | -43.63825 | 2025-09-10 04:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a8a646a5-af44-375f-8772-7375611a6948 | -9.06353 | -49.83448 | 2025-09-10 04:42:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e03d7d6c-c8f8-3a25-b07a-1e99fe10725d | -8.06071 | -52.32574 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c57a9796-a6f9-363f-8bd2-be28cce8cf2d | -10.7178 | -48.28014 | 2025-09-10 04:42:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e349457-b6d8-3041-9936-f77bb76ad859 | -9.97898 | -50.31467 | 2025-09-10 04:42:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7e9748a3-da6f-3c24-a47f-0e77e9cb424e | -11.46488 | -43.63038 | 2025-09-10 04:42:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b9ad7a6e-dcdf-3a9c-b8c8-e293ce35dac6 | -10.65359 | -48.61448 | 2025-09-10 04:42:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| baaaa13c-8399-3d20-a70f-8c94f4ea333a | -8.85033 | -52.00446 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e315832-3b86-326d-9500-6525b650e65e | -10.95321 | -46.80135 | 2025-09-10 04:42:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a66f71d9-9f8f-3f93-8b88-4711ff3cf1e5 | -11.15882 | -45.28728 | 2025-09-10 04:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d6e77527-5ca2-32be-9aa6-3af585be5281 | -9.074 | -50.47454 | 2025-09-10 04:42:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1cc1b65f-045a-32fa-87b9-41483b19b182 | -8.40639 | -47.30056 | 2025-09-10 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b123add0-c2d4-3b72-8b07-b2dcddb353e2 | -7.18432 | -44.93773 | 2025-09-10 04:42:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 2a357827-74a7-34e9-9da7-4403841d7e19 | -7.88724 | -46.26584 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 97ae4697-afed-36f9-a9ec-cd218d103244 | -5.79098 | -50.16258 | 2025-09-10 04:42:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a696cc3-76d2-3d38-9a04-45e2c1aaadd5 | -11.43855 | -49.276 | 2025-09-10 04:42:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5bbd3d1d-ee41-3f96-a470-33b93a8b2642 | -7.78733 | -46.09871 | 2025-09-10 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2070f401-f78b-3253-bbb2-14340a7d3af9 | -9.01495 | -49.54295 | 2025-09-10 04:42:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 05d55434-bc3b-3994-a2f9-2335acb9fcf4 | -11.11781 | -48.42188 | 2025-09-10 04:42:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 35ff38f7-5459-3f5a-84ed-92394e4e2f69 | -11.95466 | -46.65371 | 2025-09-10 04:42:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3e779f2d-e978-3070-baf4-ca4c1abad801 | -8.04469 | -48.68233 | 2025-09-10 04:42:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 21.9 |
| c5529e71-5eb8-32a5-ba5f-0a30513f7ee9 | -10.73455 | -48.28664 | 2025-09-10 04:42:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 93c4d654-6881-32db-b476-049deb261af7 | -11.23996 | -49.40863 | 2025-09-10 04:42:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README63.md)
