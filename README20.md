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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a1307484-6742-3610-8966-3fce30566d43 | -12.6176 | -48.19324 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 7877bc13-3b11-3a9a-82fd-c2beb15c77bb | -13.51901 | -47.00768 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a5ddf65f-eaef-3396-af65-149abc8e1ef5 | -11.48239 | -46.79111 | 2025-09-02 03:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a7db9f72-3390-3d72-8805-a6d70a4e8d20 | -11.10368 | -44.63631 | 2025-09-02 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| efd0dab2-8950-31f0-83e5-11ea0dd089d1 | -10.0529 | -48.14255 | 2025-09-02 03:51:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a1c176aa-5193-3c1c-ad54-0c0a95f1f9c7 | -11.86177 | -46.72457 | 2025-09-02 03:51:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| acf8d90e-6fbd-342b-86ed-048dd96c1a7f | -11.9081 | -46.67672 | 2025-09-02 03:51:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e946fc38-a347-3f3e-962c-d5e62d1d0fff | -7.98272 | -46.4601 | 2025-09-02 03:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8ff29660-d49f-37bc-a79a-4ec24fb49fba | -11.54946 | -44.84549 | 2025-09-02 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7235d247-7ca5-3cb4-9712-eae2bd8905f1 | -10.83779 | -47.27703 | 2025-09-02 03:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5e8729b8-bd50-350a-813e-1244396708c2 | -14.73352 | -46.75288 | 2025-09-02 03:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3fcaa2ce-2398-39f7-9ac6-220734cd40f9 | -12.87529 | -48.05473 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ff28934b-928a-3090-9f12-a345d55c1c7c | -8.86128 | -45.79331 | 2025-09-02 03:51:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2ad3e10b-54fa-3b13-8616-21e12a8c5440 | -11.09259 | -44.61965 | 2025-09-02 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 46dfb8aa-1f26-303e-90c2-3a040cbe04e1 | -12.62882 | -48.18111 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 965b0558-bf4a-3c01-8618-6da04a9ce435 | -7.87099 | -47.96511 | 2025-09-02 03:51:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| caafc631-93dd-3a02-b7e0-a9e66f00b511 | -7.98244 | -46.46675 | 2025-09-02 03:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3a1e5c1b-24e2-302d-bfd8-c59565a48fae | -12.61608 | -48.18675 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 7f2f6768-cd40-3426-b58a-8c1b8bc7b577 | -11.00601 | -46.8314 | 2025-09-02 03:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 71214e62-d99b-30f1-996b-048e668ad8e3 | -12.97791 | -48.11098 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 65d5f419-1e13-3c67-8d61-d5379859b824 | -12.87133 | -48.04584 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fe193554-ce3e-3007-8f62-f828ffd12403 | -14.22129 | -48.05369 | 2025-09-02 03:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 09170cc8-ef87-35c8-8834-4760e312f6b4 | -11.35855 | -43.53347 | 2025-09-02 03:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 662fcf37-7fee-310e-8c59-0d793083810a | -9.13084 | -46.05273 | 2025-09-02 03:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9342b4b3-737e-377d-bc10-855ba2948fa6 | -9.12515 | -46.05184 | 2025-09-02 03:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6f6eb940-1a90-3ce5-bc5c-354dcaf1e55c | -10.05796 | -48.14763 | 2025-09-02 03:51:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bdaee4c6-e4d0-3997-a693-cde5befa76e5 | -11.6555 | -52.21337 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 31.6 |
| d17dcca0-a116-30d7-b7e8-fc22ab7f004e | -8.7036 | -50.43679 | 2025-09-02 03:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b736c6e-b469-3e63-bd13-da4cb1325955 | -12.98028 | -48.09904 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3789e7e8-ab11-3cd9-b211-dfc5107776e9 | -7.98078 | -46.47103 | 2025-09-02 03:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 169dd6bc-2522-374b-a403-af45a7ce0512 | -9.43968 | -48.86834 | 2025-09-02 03:51:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 278c2199-4fe1-37da-bbff-cd69ce016a04 | -11.09713 | -44.62048 | 2025-09-02 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 25.9 |
| ae47ebb1-9bd3-39be-8063-0c2b0ee135ec | -14.61861 | -48.03254 | 2025-09-02 03:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 57f92f5c-bd17-31d1-a56b-82a3fe9fec90 | -13.27597 | -46.88963 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ca774ca-c058-32c1-8cf1-e877e393e775 | -11.89802 | -46.67378 | 2025-09-02 03:51:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af25ca52-e2b6-3773-8efd-39de2494e9e8 | -14.05452 | -44.57225 | 2025-09-02 03:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d899142f-9667-328d-a066-d1e5fdb4cbda | -14.71385 | -46.74939 | 2025-09-02 03:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb3eb971-de2a-3ed8-a461-101c37ee65d0 | -13.53036 | -47.0037 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f732c4d-0de7-34d7-938e-054064955c02 | -7.60562 | -46.03795 | 2025-09-02 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 42418e01-2120-3224-8f7b-4e3ad2e77c13 | -8.71472 | -50.45326 | 2025-09-02 03:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c51684dd-2083-3268-8ebc-d0fcde04698c | -11.91756 | -50.62324 | 2025-09-02 03:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ae11b4e7-6430-3ce7-954c-e7482485d4d7 | -10.73089 | -44.80066 | 2025-09-02 03:51:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f67d20bc-6b50-3c9d-8f23-2e7aa784aa5a | -13.32501 | -46.83976 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 436c1f60-789e-3e7f-8a02-4e46cca7f8d4 | -7.98334 | -46.45659 | 2025-09-02 03:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| dc3e8f50-7c78-3b87-b5f9-f302ca40d425 | -13.32069 | -46.83503 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 576f0bd9-0ce3-301e-819b-938686c9fa4a | -11.65153 | -52.19704 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 749a31ff-405c-3bda-be43-94c6887ca7c2 | -13.69981 | -46.87799 | 2025-09-02 03:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d61aa3d0-388d-31ac-8bba-0ac107de73ac | -11.01834 | -46.9416 | 2025-09-02 03:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 22243073-6625-3980-a64c-86cc065bf1cd | -11.89922 | -44.88927 | 2025-09-02 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7c324bff-8d8e-31aa-86b7-a88faba2b946 | -10.06169 | -48.12835 | 2025-09-02 03:51:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9ee776f5-37ed-3640-846c-545da2a0aa17 | -11.88657 | -46.67811 | 2025-09-02 03:51:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59d6cee4-9dff-30e7-9370-5b3d4bb348e0 | -7.67099 | -44.74014 | 2025-09-02 03:51:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f69bbb01-7d14-3730-9ce0-a55aca89b86f | -14.26161 | -45.24664 | 2025-09-02 03:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 095c9f98-0117-3360-a9bf-bea058ef8eb0 | -12.4367 | -48.72322 | 2025-09-02 03:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b1bd5e91-5538-3811-bae5-5c94f5b68010 | -11.91641 | -50.62892 | 2025-09-02 03:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dc30b0d4-dc15-3790-b924-978c80b72eb4 | -11.97849 | -45.88147 | 2025-09-02 03:51:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7d3e510b-0ace-32d1-bdfe-577b7fcd9f66 | -10.79734 | -46.33969 | 2025-09-02 03:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 268823ab-7f54-3abb-a8a0-aa82e09f8a28 | -7.48273 | -45.36737 | 2025-09-02 03:51:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 39784193-d817-38dd-9dd9-49c7666f7ce1 | -7.98209 | -46.46367 | 2025-09-02 03:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 18a2ddf3-4c70-3eb2-aaed-0428868e3f3f | -11.67271 | -52.19387 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 19.5 |
| e1141b85-0116-3794-9695-194e71d050d7 | -12.81215 | -48.06294 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cad678da-1041-325f-8074-0d4c51bb445b | -10.05656 | -48.09944 | 2025-09-02 03:51:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 91d8cde0-9fde-30cf-90aa-0ab41e1de270 | -13.49873 | -47.00323 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8988385d-d43a-3154-9cfb-93dbf23b21ff | -13.31004 | -46.83582 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8f0e93f8-8fd1-3052-9ada-1a728a1ea017 | -14.21446 | -48.05995 | 2025-09-02 03:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3d8c1be1-d039-3353-9577-befe85e43d48 | -11.09496 | -44.65886 | 2025-09-02 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7ca54ccb-3b91-3dc9-b0a7-e3ded1f336dc | -11.85787 | -46.71706 | 2025-09-02 03:51:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 45bef287-5aeb-32be-b1fc-d0ecfb9f3be1 | -13.75738 | -43.77446 | 2025-09-02 03:51:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 472e6eb1-c873-3b29-b2f8-df10f3c35fe6 | -7.49759 | -45.34261 | 2025-09-02 03:51:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1942fb6c-45b5-3df8-909c-f8f69a842b8e | -7.71613 | -50.2589 | 2025-09-02 03:51:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4bc75f8b-9b1d-3da6-a720-50cdc88cdcac | -10.05004 | -48.09517 | 2025-09-02 03:51:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 767e60ce-13fa-326c-8c34-548aa44aa205 | -7.49706 | -45.34559 | 2025-09-02 03:51:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 69c9d3bd-728b-3f0e-adf7-b98446d2db97 | -13.52409 | -47.00875 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 992c5ca5-8856-320e-bb99-14a518205f69 | -7.63219 | -46.55529 | 2025-09-02 03:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 077d1be9-3c31-3717-bc5a-04c02b7ac002 | -9.12513 | -46.05468 | 2025-09-02 03:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7122a85a-a1b5-34a2-9223-30e7086c485e | -14.72858 | -46.75215 | 2025-09-02 03:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5ead9be4-4232-3b77-8aed-d71712385f77 | -14.59996 | -48.04246 | 2025-09-02 03:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ec7260a5-227d-3422-8a73-7b373f766edd | -11.87257 | -46.72397 | 2025-09-02 03:51:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| df844eaf-ef57-3bd6-97f2-c66f0a4a8eac | -8.83907 | -45.78569 | 2025-09-02 03:51:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2f27337a-f948-3a91-90c8-77b323d080e4 | -13.32827 | -46.95869 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 577ee545-d630-367d-8370-80401362b3d3 | -11.66595 | -52.19979 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 8b79c5d7-f67e-3f79-aec7-9911602d30d6 | -11.92065 | -50.62954 | 2025-09-02 03:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 06bd0f75-ed8d-3d15-b7db-07cab720ad14 | -14.6115 | -48.0403 | 2025-09-02 03:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 448f1558-7e01-32ab-83fe-ef465ac20f4f | -8.45842 | -47.36347 | 2025-09-02 03:51:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0695c318-1925-36ad-bd36-02eb0dcb9ca3 | -9.12462 | -46.05477 | 2025-09-02 03:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 62e6dff4-bd17-36f7-b605-cb100c8c3017 | -13.27538 | -46.89274 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7bd5bf8a-de37-3460-a92e-656ad8e465e5 | -7.37839 | -47.04749 | 2025-09-02 03:51:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| aac91be2-4a18-3cb9-bd6a-b09edae2ab7d | -11.09544 | -44.62989 | 2025-09-02 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 88.8 |
| a8356000-09fb-3e3c-bd87-fd7cb1a0825d | -7.93727 | -46.43287 | 2025-09-02 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6c5a01f8-f48d-38a2-9cea-566a0cda5134 | -13.28196 | -46.9136 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8a595560-1cfe-36e3-b944-ee71c68b777d | -7.49497 | -45.35741 | 2025-09-02 03:51:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 943b29c3-4e68-3da2-a93e-3121b8e6fe6e | -7.7038 | -45.01851 | 2025-09-02 03:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b942895b-8f38-3fd7-9e89-7a11aa48f69d | -8.85195 | -50.58578 | 2025-09-02 03:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 29b9eb52-b786-3391-b929-599ce789c255 | -8.18917 | -46.78735 | 2025-09-02 03:51:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6c8b6ad5-6e92-3508-ac3d-b036c64ec774 | -14.73208 | -46.75146 | 2025-09-02 03:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 47ca1204-4664-3fec-b635-3912aaafc5be | -11.6571 | -52.20596 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 50824eb4-4db6-3e5c-9084-1e069e3d4e70 | -13.32767 | -46.96184 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3da4ab95-c7e9-37f2-a050-dbbc32830ba9 | -7.49445 | -45.36037 | 2025-09-02 03:51:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 70dc1098-675a-3594-8a5f-cc3e0aaad83e | -14.76777 | -47.49993 | 2025-09-02 03:51:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9ce8f4fd-d098-32b6-b944-c124da84df43 | -7.70739 | -45.02205 | 2025-09-02 03:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README21.md)
