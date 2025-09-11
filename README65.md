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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 70a283ed-423e-3db0-95fb-048362536ed4 | -13.05444 | -47.15049 | 2025-09-11 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1a5d0e87-82fd-322c-a8e7-e177295a7266 | -13.26401 | -51.75116 | 2025-09-11 04:23:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ac9c91ac-f073-3122-8a0f-6956878c54b2 | -11.41435 | -43.61343 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2861faf0-db70-368d-b820-b4889c26914a | -9.88802 | -51.88203 | 2025-09-11 04:23:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 93af758d-7c17-3986-8997-be9f4a39675b | -15.22695 | -44.04475 | 2025-09-11 04:23:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cf9fcb06-445d-3247-bbf0-187d258dc42e | -9.13616 | -47.01136 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c0f3c568-cfda-34f7-ba80-66ce89dbdd85 | -12.07022 | -47.57355 | 2025-09-11 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 60bda3d1-472a-374d-8305-ac9f10252397 | -9.58712 | -48.06729 | 2025-09-11 04:23:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1b50ab65-ed6b-33b3-bf61-79d43be54860 | -9.06559 | -47.06103 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 34acae3d-e57d-352e-a2d1-2ed795a0e06c | -11.94448 | -46.64743 | 2025-09-11 04:23:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c8e026f4-b8e0-3469-904f-0b8893f38def | -14.13299 | -45.39799 | 2025-09-11 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f5313c8a-4678-311a-b268-af6759c71cfb | -9.79966 | -51.09768 | 2025-09-11 04:23:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8363c865-4f69-3601-91cc-a91199de0a84 | -11.63154 | -46.76448 | 2025-09-11 04:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9e2e5cdb-0e11-3f1b-a8ae-a588a7f4a505 | -9.59196 | -48.05992 | 2025-09-11 04:23:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1eb386f6-1801-3c41-b36e-b14bfeaa7cd8 | -10.39222 | -48.57932 | 2025-09-11 04:23:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 799317bb-5909-3354-8b42-daacf069bcaf | -10.32712 | -48.81145 | 2025-09-11 04:23:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dbe2bf33-e8c7-3e11-a766-2d600251a261 | -14.13868 | -45.39087 | 2025-09-11 04:23:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a4587bc0-7b6f-304e-a38d-a51b5e3ca3e2 | -9.04753 | -46.97788 | 2025-09-11 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6f0404c5-32db-3814-8bb4-e8940047128a | -9.08426 | -47.07605 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c71b1c08-2836-358d-b514-5665d826ed35 | -12.11374 | -51.0471 | 2025-09-11 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 580a0b3b-f119-3c10-8d6c-b7d4e669a55e | -12.06497 | -47.58415 | 2025-09-11 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6d8ccad2-099b-34f4-bfee-21db3e1da981 | -12.84549 | -47.96283 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 20040d9b-8877-3e4c-a3d0-65c42a13e737 | -9.77755 | -51.10029 | 2025-09-11 04:23:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 459d2f14-ebfe-30f8-9f54-1815ad0d0f51 | -11.40252 | -45.60593 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| cff2e4ec-2e19-339f-bdfb-13dd29082a66 | -11.68231 | -46.90934 | 2025-09-11 04:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f1bc5ac1-4053-3a3b-b2ab-b629102e3c60 | -11.09923 | -48.4369 | 2025-09-11 04:23:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 54acf0ab-19a0-35a8-804a-909452316e7b | -13.9257 | -48.23217 | 2025-09-11 04:23:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 56e40d8a-fd13-360a-bdbe-fbf078ad87fb | -10.02741 | -51.72969 | 2025-09-11 04:23:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f6ec0046-70fa-3b87-b8f9-604c16dcb767 | -14.57387 | -48.76532 | 2025-09-11 04:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 151ebad0-0b6a-3689-a5e4-0b028eb81571 | -13.64752 | -45.69738 | 2025-09-11 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| eaae69a0-44e9-358b-be0f-a8e955af4bd7 | -12.85899 | -47.96042 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0b3a5c17-dfd3-3706-be92-8a99306cf797 | -15.21459 | -44.05526 | 2025-09-11 04:23:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a4df77d9-357d-3da6-b895-86b480d792c8 | -9.31862 | -46.75019 | 2025-09-11 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a331999f-cc61-3293-8002-2ed22f4ff4bc | -13.90613 | -47.99338 | 2025-09-11 04:23:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2e2a697a-15f4-37b8-9498-3fd4f496552b | -9.0756 | -47.08607 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5b005b06-1db1-3b2e-8a0a-8cb7e0e92de1 | -11.34684 | -46.49451 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b9dc3cad-29ea-3954-b554-1302d1a28436 | -11.37851 | -43.51383 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 38157099-80e2-31ca-a35a-0806f3c0cf14 | -14.30457 | -44.86985 | 2025-09-11 04:23:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 461b1c35-eabb-3d6d-9740-d8686153f259 | -10.56963 | -52.02335 | 2025-09-11 04:23:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fbb3a5e9-4970-3f6e-82d5-93dc00527a1d | -9.01962 | -49.50236 | 2025-09-11 04:23:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 23cf6813-b904-3667-849c-6cdcc0aa25e4 | -11.72672 | -50.63972 | 2025-09-11 04:23:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 3b0dfb59-c296-3406-a743-af5d608aa7ef | -9.18957 | -45.59185 | 2025-09-11 04:23:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8fa6c580-3382-38da-9ecc-caa017d2d2ca | -9.07862 | -47.06744 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 476c5e14-b0e0-3188-bd8f-70f2482f3ef4 | -13.98475 | -48.21593 | 2025-09-11 04:23:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7a3b2f5d-e909-37d3-ba38-6de2305c5d4b | -9.75224 | -47.85314 | 2025-09-11 04:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 71f25abd-7a86-3035-b795-f50ca7c981ec | -10.02155 | -51.73746 | 2025-09-11 04:23:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f80958a1-44fa-3803-a7f6-45b9ea3c64b6 | -12.12687 | -44.86403 | 2025-09-11 04:23:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6273667e-1cce-3e5b-8ce2-68b1b4ae1dd7 | -12.85244 | -52.93738 | 2025-09-11 04:23:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b80a8391-8015-32c9-b21c-e2a7bf473030 | -9.45965 | -46.74015 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2fc598c0-0b7d-3100-9072-e6cc7f5e21fe | -11.05425 | -51.34466 | 2025-09-11 04:23:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 80464eac-938a-3694-91ae-381039b3f5fc | -11.48493 | -43.62732 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ab5a9e3e-2228-3ad4-be89-9e24c4f2558f | -11.10684 | -48.41316 | 2025-09-11 04:23:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f2a58a22-0daf-3342-9d0a-7a19826ef707 | -12.84656 | -52.94764 | 2025-09-11 04:23:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8d4ec5a8-48f5-3446-8b7b-37a020c9adec | -9.10006 | -46.9566 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b7fbd39e-fa5b-3d5e-92ba-b0ded78a4a5a | -10.70992 | -48.30412 | 2025-09-11 04:23:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 43dd3097-0b96-3dd6-bf09-058030430bab | -10.53758 | -49.8835 | 2025-09-11 04:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6cbb6e70-74e5-3768-84a6-9437a75bd141 | -12.12798 | -44.85681 | 2025-09-11 04:23:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7d50b7de-643a-3cf2-8bc5-81345e036140 | -9.81168 | -47.75457 | 2025-09-11 04:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1f6157d0-8a80-3b18-9749-0077e5a7d5e5 | -13.45143 | -43.48568 | 2025-09-11 04:23:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b40e6ab9-c5a6-36ba-9432-d7183063e7ba | -11.47695 | -43.68118 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ec622f0c-fb67-3b93-964a-d343bfc7c417 | -15.19513 | -44.04548 | 2025-09-11 04:23:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2251ee00-9737-3d20-a854-ee1e272ee974 | -11.68625 | -46.90631 | 2025-09-11 04:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e6a298f-0009-370b-a508-3dba8e429540 | -13.32791 | -46.37518 | 2025-09-11 04:23:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f9f1cb85-4345-37cf-bd5a-383f63ceb076 | -12.07298 | -50.9959 | 2025-09-11 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 7bfec42a-a72f-356a-a730-a9e735fb253c | -9.0191 | -49.78367 | 2025-09-11 04:23:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 932b132a-7496-394d-a03c-cc4dd7512506 | -9.68327 | -46.76102 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 868ee348-e0a1-3d32-97ad-75f22af8ac05 | -10.15302 | -46.16887 | 2025-09-11 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d3c2aa9-1b3e-3889-a9f6-27e267013336 | -11.77071 | -46.48723 | 2025-09-11 04:23:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 98cfc0aa-ff40-332c-8569-4cd315d44b6a | -11.44099 | -43.57804 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| eac0f9b0-22c8-3675-a267-b522b6496165 | -12.88638 | -47.9651 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff5921e5-282d-30f4-8e7d-12302d54cccf | -11.47046 | -43.64176 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a2c303db-9e51-32f8-9286-b5235da5afc7 | -12.56524 | -44.64461 | 2025-09-11 04:23:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 28121ad1-8bf7-3724-b1a9-0b6824f9dd4a | -11.50741 | -47.68054 | 2025-09-11 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3af5cc2b-9cf8-3c8d-bda8-b5a1e15b0e59 | -11.71881 | -50.63829 | 2025-09-11 04:23:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 4783ac18-5742-3fa5-b30d-9e7e37f9f90d | -9.05998 | -47.05228 | 2025-09-11 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9127a88c-b953-3387-b4e5-c846b8aa7f47 | -11.31096 | -50.75819 | 2025-09-11 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4dbb25a1-2ba1-3ff2-aa08-3a5c833075c5 | -9.05471 | -47.06307 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4bbb3225-4e21-3dde-aa1d-8673d25f649e | -11.4271 | -43.69392 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9811337e-b7f8-3d22-b43f-e0db1893c557 | -13.911 | -47.96369 | 2025-09-11 04:23:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 568f228d-2d52-3237-aea9-783520fe19cd | -8.52291 | -54.769 | 2025-09-11 04:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c3dc855c-5f02-3905-83a8-f03c6ab3e5f9 | -11.3679 | -46.54514 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 1f4f217c-9b51-32a4-b6dc-da9b6e902c3f | -11.38719 | -43.52709 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 03adc674-d27e-37fb-b16d-dc8b3ab1fbfc | -11.48041 | -43.68172 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a6b5c3e4-087b-3858-84a9-06c0a4bd2401 | -11.48274 | -43.68994 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e4e9bb4a-e3c2-3f19-a11d-589f9684c938 | -11.4572 | -43.58849 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7b24312a-fb42-3096-adb4-bc7f15bb2371 | -8.81065 | -48.09051 | 2025-09-11 04:23:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8f4d7925-faa0-3b1d-88b3-c79dc3074912 | -13.13474 | -54.91984 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f1175dc4-e738-365f-8204-ad37e78a05eb | -12.02927 | -47.54782 | 2025-09-11 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 354c97df-6ccb-3a1a-ab80-b751aa80a522 | -12.94514 | -54.82019 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6cd5d26c-d785-3482-8254-850b26ae8244 | -12.93651 | -54.79868 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 84fb1a1c-22fb-3eb3-a7a0-187f48d46073 | -11.74387 | -46.52653 | 2025-09-11 04:23:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cbda4efe-553b-39d5-b8ca-7c83bb2c7540 | -11.22174 | -54.99585 | 2025-09-11 04:23:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5bddf26c-4b0d-30af-9a4f-8e03c2cae4c2 | -15.02591 | -48.04836 | 2025-09-11 04:23:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b4cfe912-95a0-3637-82b8-93bf70d272f9 | -12.86007 | -52.95023 | 2025-09-11 04:23:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 925dc95e-d68f-34e6-b3d9-91d00e24476b | -11.43404 | -43.57696 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 630dea3c-e0af-3f10-bc7a-b1ad4e186f04 | -9.06593 | -47.08063 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6b026183-be29-309e-8380-00061669b2f3 | -10.78299 | -45.99991 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b54fe8f6-e400-35c8-a72e-03e71c306a32 | -13.65878 | -45.72454 | 2025-09-11 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f3b1aa2c-b7ea-3abe-8b70-a64b2f9177de | -9.00667 | -49.52274 | 2025-09-11 04:23:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f0bcffc6-dfdd-3be9-a18f-e6d8cd90a846 | -9.12419 | -46.19565 | 2025-09-11 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README66.md)
