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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0a5bb028-a9c8-39e9-863e-0288dfc7b220 | -12.43702 | -58.40084 | 2026-06-04 04:44:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 032ff434-6ade-3d1c-a073-4cd99fd83f29 | -13.1772 | -46.85133 | 2026-06-04 04:44:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3cdb0e4b-15cb-38c6-ac58-e46eff4eb6cb | -15.96292 | -52.20975 | 2026-06-04 04:44:00 | NPP-375D | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d429177d-e783-30ce-a70a-bd363c919b0e | -10.39101 | -49.44477 | 2026-06-04 04:44:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| a58bab55-a30e-30b2-94f5-42fcccda7a8e | -15.23502 | -48.5663 | 2026-06-04 04:44:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e9b41ba5-84b2-3502-a2df-550af495c5ee | -14.08906 | -59.38488 | 2026-06-04 04:44:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 78efdc33-501e-3541-999b-dcf9ee998608 | -14.09511 | -59.38262 | 2026-06-04 04:44:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a0276447-0f82-3a7b-973e-2b2d0111fec3 | -13.9568 | -46.18618 | 2026-06-04 04:44:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3c53596b-67c7-3696-a654-2dbe533f5753 | -12.22072 | -57.2855 | 2026-06-04 04:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| ccc3bff8-50ba-3973-a75b-745e4a2100c0 | -12.54624 | -57.18171 | 2026-06-04 04:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d9bfabd6-97b6-3487-a112-055d0de0b5f2 | -11.78486 | -52.51409 | 2026-06-04 04:44:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed52f3e8-e528-3861-a995-8e7a0a3a53c6 | -12.55962 | -48.35196 | 2026-06-04 04:44:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 434a1ac9-e34a-364e-9949-add6728a8260 | -12.45115 | -58.46938 | 2026-06-04 04:44:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a004026b-ecce-32e0-97e5-5ca6ba2d6acb | -11.2599 | -53.96498 | 2026-06-04 04:44:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c57cf71b-9814-3613-8151-f535c57b85cf | -14.05894 | -53.39772 | 2026-06-04 04:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| dc918d8c-f7a1-35e0-90d8-e189e6266b88 | -10.57408 | -57.31737 | 2026-06-04 04:44:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cb124623-4729-37f8-ae38-5d6710ad19c5 | -13.53796 | -49.90202 | 2026-06-04 04:44:00 | NPP-375D | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6d84cb4e-ad2f-305b-9827-2e68aa38e3b2 | -12.45055 | -58.47249 | 2026-06-04 04:44:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d7e1fa15-efb2-33b9-9d70-49867173975c | -12.73497 | -54.19878 | 2026-06-04 04:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 496cb67a-e33d-3775-a33a-2c21518892e8 | -9.51894 | -50.26093 | 2026-06-04 04:44:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 60bbc82f-bb37-33d9-b8fb-de7214381351 | -11.62226 | -55.1857 | 2026-06-04 04:44:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2169366-4c79-39e7-8fe1-af37a14f1af2 | -12.21105 | -57.28355 | 2026-06-04 04:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f87c6b08-2e55-3d51-b078-d2d2f0d7448f | -9.93162 | -48.003 | 2026-06-04 04:44:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ff387b94-6685-3462-93d8-69c798c1d18b | -12.46099 | -58.47449 | 2026-06-04 04:44:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d8bea9c3-e235-3c2a-84ad-884510db4b1f | -12.17158 | -54.54057 | 2026-06-04 04:44:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f1dcbed4-26ee-3737-a8bd-3025398d5d4d | -11.6327 | -55.19019 | 2026-06-04 04:44:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0a9d0af9-33b0-3d4e-8e5c-b775c8f404cc | -11.78559 | -52.50987 | 2026-06-04 04:44:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6ec96cd-b233-3cc4-af95-e023c3f1d27d | -12.22597 | -57.26816 | 2026-06-04 04:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fed57731-3da4-3627-8ef4-d4227495957b | -12.55004 | -57.18797 | 2026-06-04 04:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d880cf25-d693-3cec-846f-33e29d155a5d | -11.60243 | -55.33181 | 2026-06-04 04:44:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5ecf88d4-2bcf-3411-b1f4-7df77005baf2 | -11.25807 | -48.35773 | 2026-06-04 04:44:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b6436dc8-0d55-360f-a4ca-903e0fccc699 | -12.2238 | -57.26936 | 2026-06-04 04:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| cc02c05c-a098-3d7f-9eb3-1263777b01a6 | -10.98438 | -47.07548 | 2026-06-04 04:44:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b7a2461-b959-3aff-91f1-0b5dcd6d355c | -9.89688 | -47.86182 | 2026-06-04 04:44:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a9b88b54-8883-3383-8290-1fcdd4a7f38d | -12.73408 | -54.2039 | 2026-06-04 04:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e1990e1-c694-3a61-80fa-46d41af16b9a | -12.17908 | -54.54229 | 2026-06-04 04:44:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ab1ece5-c087-3c78-b963-dfab34d9b83a | -11.62722 | -55.18246 | 2026-06-04 04:44:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab745114-3164-3007-8971-5624d3b73453 | -11.5965 | -55.33253 | 2026-06-04 04:44:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 36aaf8a2-7d43-3acc-a6e0-fa190d871f96 | -10.56264 | -46.63071 | 2026-06-04 04:44:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a75cbff1-64ce-30da-88e6-d53b9e80e13e | -12.30396 | -47.90432 | 2026-06-04 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c9ff15d3-2d3e-3b80-8b7b-692fb7640ab6 | -12.20896 | -57.29447 | 2026-06-04 04:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 3642d960-90ed-3821-8427-73424ccc11bf | -12.32097 | -47.90695 | 2026-06-04 04:44:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 17211028-30ea-33e4-9391-ba9f2cf54a67 | -9.37609 | -50.54086 | 2026-06-04 04:44:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 02783a71-c1c5-355d-a0bb-f29d32efc377 | -11.54684 | -52.7919 | 2026-06-04 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| fcd65dc7-8da3-3ae4-a5be-92e5c40705ab | -12.21433 | -57.27696 | 2026-06-04 04:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 4d3e614b-5095-3d93-a28f-3840831ff235 | -10.57195 | -57.32348 | 2026-06-04 04:44:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 42862bae-2851-37f1-afca-6a41ef51535c | -14.08701 | -53.3891 | 2026-06-04 04:44:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 296099e8-5988-3541-aaf1-fec94053d27a | -9.46749 | -46.06301 | 2026-06-04 04:44:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| def426ad-aebd-325e-a6b9-8896a054a373 | -12.44615 | -58.41185 | 2026-06-04 04:44:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c7d6999-a5ef-33c6-b9c1-f8b29a1175c5 | -10.67171 | -49.69723 | 2026-06-04 04:44:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 009c07fe-3052-31a8-9fe1-f85da2b56eb6 | -11.88844 | -57.83575 | 2026-06-04 04:44:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b41e9d0-5804-3271-8e9a-9e859d1b4fd3 | -9.36531 | -47.0852 | 2026-06-04 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 41943431-037e-3e77-a295-19495375fe5c | -14.04944 | -46.34743 | 2026-06-04 04:44:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2a454c0d-f0f4-392d-926c-56cabe85d3c7 | -10.57084 | -57.32928 | 2026-06-04 04:44:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b3a3ba97-e19a-3704-b85e-1a7fbe86389f | -12.54492 | -57.1823 | 2026-06-04 04:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7c42f40-3043-3e32-9e12-a92204164203 | -10.55386 | -46.6175 | 2026-06-04 04:44:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3032b609-fa74-3df6-963c-4c8de94de566 | -11.1671 | -49.24218 | 2026-06-04 04:44:00 | NPP-375D | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 96035476-ada3-3c06-b4f0-56c1a6c80c88 | -11.6242 | -55.1886 | 2026-06-04 04:44:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2d451efb-82d6-3971-b649-bdd5e313ab84 | -10.38768 | -49.44423 | 2026-06-04 04:44:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| f4667066-9cdf-3bcb-bbd7-6695fb2bde9a | -12.43581 | -58.40726 | 2026-06-04 04:44:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e5711694-2f79-3ece-9033-269af35a8c47 | -14.78602 | -50.63851 | 2026-06-04 04:44:00 | NPP-375D | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5b070b1d-a4fe-3ba9-b74c-949289a6a776 | -12.0088 | -45.34595 | 2026-06-04 04:44:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e3ff33a9-f8b0-34c0-a72e-2999969cfbd3 | -10.86287 | -53.73299 | 2026-06-04 04:44:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ebe32057-d30d-3824-a227-a4ab0cdaadca | -9.37206 | -50.54401 | 2026-06-04 04:44:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ecf727a-174c-3a78-ac11-50c569058f75 | -10.38712 | -49.44775 | 2026-06-04 04:44:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 03d051c3-e51a-3c9f-80c5-857cc9ee75cc | -9.92492 | -48.00193 | 2026-06-04 04:44:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 165cd3d7-500e-3cd1-ab93-39d4da877f25 | -12.43763 | -58.39758 | 2026-06-04 04:44:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| da75792c-1e4b-35ca-ae89-871eff04f2ef | -11.62581 | -55.19053 | 2026-06-04 04:44:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ddbd337-d86e-36b1-bde8-480a572032d1 | -12.21133 | -57.29333 | 2026-06-04 04:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 15.0 |
| f22e18a7-6e7e-3acf-9f94-4e15233c089d | -10.38434 | -49.44369 | 2026-06-04 04:44:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 1bb7bccc-27e4-3286-96d2-aaf9244c22f5 | -14.05069 | -46.3386 | 2026-06-04 04:44:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f893242d-a776-3d5f-a5e2-4ae4309da841 | -10.84673 | -53.75594 | 2026-06-04 04:44:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 195e0b47-e57e-3ce3-baed-0faa7ae70529 | -14.76794 | -52.67528 | 2026-06-04 04:44:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3fb6c624-6e26-3f88-867c-ed926f10be38 | -10.89784 | -54.13297 | 2026-06-04 04:44:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fc9d01b1-b3e4-3b0c-b39f-ccd6c5bd427b | -14.44462 | -48.90276 | 2026-06-04 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 454e225d-91ac-3e49-aafc-e9fcc54376f8 | -11.95434 | -49.54336 | 2026-06-04 04:44:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 97ce39e1-d273-3f9f-8dd6-ed692df35f9a | -12.46159 | -58.47136 | 2026-06-04 04:44:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3bb2a43d-9156-3a77-ad4d-b8a7b3385ae6 | -12.22762 | -57.27561 | 2026-06-04 04:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| bcc8888e-4dbe-385f-8a56-75265e92be29 | -12.56354 | -48.34886 | 2026-06-04 04:44:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f3482bd-7d0d-33ba-bb81-e71864d98ff7 | -11.75847 | -47.0721 | 2026-06-04 04:44:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f99d2e63-c04c-3587-ba64-61a0965ef925 | -11.59813 | -55.33102 | 2026-06-04 04:44:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 811b454b-9f2e-358e-ab2d-233a50a4d174 | -11.25863 | -48.35416 | 2026-06-04 04:44:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 185a7c5a-e0f8-3b55-8a4d-652ff183352a | -11.61994 | -55.1878 | 2026-06-04 04:44:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48c68ef7-6c80-3e96-a217-5e6a2b261d40 | -11.89158 | -57.8294 | 2026-06-04 04:44:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e28a26d-0dc4-3963-98d2-011a7f5f11ad | -11.54315 | -52.79128 | 2026-06-04 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 0222ace4-18dc-3e8b-b005-0fce9dfef0d2 | -9.88862 | -52.44111 | 2026-06-04 04:44:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b5a5a26-1d76-3688-b6ab-8000ab7c01e0 | -12.23246 | -57.27654 | 2026-06-04 04:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 4f9d994e-0e1f-3d96-8d07-8d48f68d8ace | -12.22864 | -57.27025 | 2026-06-04 04:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 6f3ca690-79d1-3799-8db1-af0aa801dab0 | -10.57693 | -57.32451 | 2026-06-04 04:44:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6bd5e70f-1e67-3bac-bef0-ba2ce0dd7f48 | -10.39158 | -49.44125 | 2026-06-04 04:44:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bf5355d3-cc9e-3ba3-b5b5-8c5e192ce1b6 | -15.31673 | -55.73823 | 2026-06-04 04:44:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 10510e8c-39a0-3e0f-9225-d8fc6ea07f76 | -9.18261 | -58.05647 | 2026-06-04 04:44:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3d8b2221-32e4-380b-86a3-77f0eb66fb3d | -9.47104 | -46.06356 | 2026-06-04 04:44:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c9187c3e-7ecf-31ca-acab-ef415a063229 | -14.44406 | -48.9064 | 2026-06-04 04:44:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8c29cbb6-0afc-3a98-8510-9b662681f437 | -11.60597 | -55.33674 | 2026-06-04 04:44:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f6894e94-962b-39e4-aa3d-955c86bb0aef | -11.55128 | -52.78814 | 2026-06-04 04:44:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 9d0c8017-fb6c-32e1-81b8-a3a19cdb328d | -12.09468 | -51.98925 | 2026-06-04 04:44:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31b3710a-7ef7-32dc-b2f1-9dba74ffabf8 | -10.61449 | -46.69061 | 2026-06-04 04:44:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e8586bfc-544d-3e5f-b3a2-5e43b120f0b3 | -12.54868 | -57.18853 | 2026-06-04 04:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c757cf0e-04d9-306c-8c2d-53907a1f8956 | -12.21589 | -57.28453 | 2026-06-04 04:44:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |


[Clique aqui para ver as próximas entradas](README10.md)
