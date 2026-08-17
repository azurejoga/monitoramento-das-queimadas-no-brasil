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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 90c1ff40-2846-3a50-a481-89a9a47169f6 | -6.77536 | -59.76417 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d5a20503-1685-3752-98b1-3fb11c39d208 | -6.85024 | -58.98555 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dc8796c2-1365-3f1c-84be-13f457ad4a13 | -8.96538 | -60.52443 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0abfd6f-7790-394c-a413-f1e18e93fe0a | -10.50724 | -50.02191 | 2026-08-17 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b34ecf59-7ab2-3970-9c3e-ddd60ef8757d | -11.22782 | -54.01621 | 2026-08-17 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cce12d91-5885-3ced-9cbd-333699434ffa | -14.86954 | -46.6473 | 2026-08-17 04:57:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 86571e72-e6f0-3eea-8914-e03d9c5f08ff | -6.89188 | -59.00416 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 21c518ff-d56e-354c-8d38-1f458e0d2a83 | -8.9694 | -60.53173 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a7694a13-9c88-346d-8160-f512ea067be8 | -7.36252 | -55.50741 | 2026-08-17 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 548fcf33-5926-320a-994d-7eba7a0512ef | -6.86894 | -56.41088 | 2026-08-17 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 34b68d52-5c53-35d2-9c8e-36d4a60d05b3 | -11.41297 | -46.40114 | 2026-08-17 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2e50a33a-02f4-3b26-ad83-10985ae16554 | -11.14122 | -49.04155 | 2026-08-17 04:57:00 | NPP-375D | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f9ef9181-0cad-3b91-a5e4-84ea2e079a43 | -11.31948 | -46.25229 | 2026-08-17 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 124fe98d-4926-393c-8609-b1f9609832f9 | -7.45506 | -60.00396 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b242859f-6ff0-34ad-bee7-aea16d77101c | -7.59488 | -61.23513 | 2026-08-17 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9ce058b2-952b-357d-aa44-4fb992e11b84 | -9.27219 | -45.65117 | 2026-08-17 04:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ef5e7827-610e-3a2f-93e2-2cea96d24d89 | -8.42405 | -62.68162 | 2026-08-17 04:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6083f177-4fd6-3ee3-a76b-5567d010a51b | -6.8724 | -56.41515 | 2026-08-17 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0227c1d9-eca6-3474-a718-b0bee0141f3f | -9.37001 | -62.36185 | 2026-08-17 04:57:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7df736b3-b6e6-35de-8ab1-c8f3ce26694d | -14.50928 | -53.02128 | 2026-08-17 04:57:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 89c4fd84-34ed-370c-986a-95288dccf818 | -6.71306 | -58.9364 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b4f9c44e-b8c8-3c31-bf67-70c3e21a0505 | -11.10867 | -47.24199 | 2026-08-17 04:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b1df810a-91a9-381c-b94a-350c2c97612a | -6.64276 | -58.96781 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 825fb305-ff70-3518-92c0-6e956f4644ae | -12.24113 | -47.03265 | 2026-08-17 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5837b382-4f4a-36a9-b76f-af99e8e0f809 | -8.96998 | -60.52856 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6cd795d4-b4d4-32a6-9a6d-fdadab015ff0 | -9.47604 | -51.66128 | 2026-08-17 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 32d83edb-cfba-3065-bda8-8a8d1d3c52aa | -9.18117 | -58.07189 | 2026-08-17 04:57:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bce1ec62-1419-3e03-92c5-99f8ef030f7d | -6.63981 | -58.95617 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fc01e804-bb4c-3181-9252-6670db0987b1 | -8.94928 | -60.52475 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 203f3c2e-fc3a-3dd3-95da-38b9f5dc572d | -13.42222 | -57.04484 | 2026-08-17 04:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3f89d9bc-727d-349e-9671-1380b52d448b | -6.87179 | -56.41872 | 2026-08-17 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3c28630f-3aab-328c-bda6-36d0c1caaad7 | -11.71933 | -54.61516 | 2026-08-17 04:57:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d23a375e-d797-3d89-aa62-6e229160209a | -11.49906 | -46.59374 | 2026-08-17 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d36a299b-ffa7-347a-b212-67a16caaf354 | -10.04994 | -62.45879 | 2026-08-17 04:57:00 | NPP-375D | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 664859f4-5c4a-3c64-b5c8-3088c1e10c23 | -14.87833 | -46.6489 | 2026-08-17 04:57:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| febe1d27-c399-3a52-89df-ebbaadb0de41 | -9.13167 | -46.01542 | 2026-08-17 04:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 114a6c92-e04f-32b0-9073-eabbc216a487 | -6.83183 | -58.97688 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 537f5570-0e8b-34a0-a01c-1680c9e3a21b | -10.97016 | -50.51062 | 2026-08-17 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 51cf8abd-5f08-3538-9d9e-4d1928da8ee5 | -11.90791 | -47.35122 | 2026-08-17 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| efed52ff-a07e-3beb-94ed-234074ce4360 | -11.13488 | -46.49533 | 2026-08-17 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2d0be123-a474-3224-96f7-bf0b7e89adc5 | -6.68812 | -59.06661 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7838c631-3452-37d7-a54b-efdcc41cd6b0 | -7.55394 | -61.18395 | 2026-08-17 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b714a164-d334-35f4-9903-a42f682d928d | -11.40808 | -46.41866 | 2026-08-17 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 62bf5405-3e29-3b3b-96de-3f690552d6d6 | -6.8243 | -56.45133 | 2026-08-17 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 35517fe2-077d-3819-b45f-3a2a8ad5f2c6 | -6.69886 | -58.96106 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0e557923-68f6-3803-bc60-16293a5c063b | -6.97024 | -59.03081 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dbd335dd-a880-37f4-a61d-356c0cdc6b15 | -9.12229 | -45.18038 | 2026-08-17 04:57:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4e798fef-f3c6-3223-bd45-ca48e06bd7b7 | -8.97862 | -60.53987 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| feb3e3ac-96cd-3ccb-9281-7c5c80bd6615 | -6.85716 | -56.43087 | 2026-08-17 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| edb646cd-ebe4-3f85-aa19-05bf2996f4b4 | -8.97688 | -60.52007 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1e16c38-cd1b-3ecf-b93e-64933fe754f0 | -9.27172 | -45.64867 | 2026-08-17 04:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 826c7f6c-1ae7-300f-b35f-eda389e43cd1 | -11.21698 | -54.01817 | 2026-08-17 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b774ca5-0d5d-317e-a60e-02b7bde4d476 | -14.30052 | -47.19725 | 2026-08-17 04:57:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| eb7ae102-999d-3633-a7af-9e606166900f | -9.06438 | -60.40039 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 29fe23e6-0a7d-3cae-a8bf-c0e556002f53 | -6.77722 | -59.45625 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 16681b49-435a-3b4c-ae00-d794e2f1a68b | -12.73522 | -48.46198 | 2026-08-17 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cdcb3be0-3342-3481-a764-2cae96dd1b5d | -6.83185 | -56.45623 | 2026-08-17 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d42c3ed1-2a37-335b-98db-4923a22a25d4 | -10.08018 | -60.49568 | 2026-08-17 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d9274853-c3d2-397c-aea6-4be9603939c9 | -14.47937 | -51.98289 | 2026-08-17 04:57:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c8002ee2-9e64-361d-b7c0-0816056ba0fc | -12.70447 | -48.52156 | 2026-08-17 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b76bf61b-ada9-32b3-8c0a-048356a17384 | -11.88068 | -50.22927 | 2026-08-17 04:57:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0d460380-9177-354d-bd5e-8014afd05408 | -6.98571 | -59.02797 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fe7c5147-2963-3de8-ad31-b42351cc78db | -7.4307 | -60.02167 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a614e519-124c-362a-af7d-3fe78566d0dc | -6.86834 | -56.41444 | 2026-08-17 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a2620b66-57cc-3136-af21-5c4eb4ba034a | -8.89312 | -60.59576 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 389498e2-631d-3151-8298-e1dba7c0323f | -6.54322 | -58.49815 | 2026-08-17 04:57:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 366b4757-43ec-369c-93ac-8a211ed4e3c8 | -8.896 | -60.5507 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84571af1-731a-3080-a892-8f6e7d63bcb9 | -15.03283 | -47.03644 | 2026-08-17 04:57:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 31a4a897-bd8c-3471-a211-3a47de45e8bf | -7.38518 | -59.9986 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1c6f95a4-faab-30b8-a064-5e928dade5af | -13.28263 | -48.69777 | 2026-08-17 04:57:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 972eb9e6-7f6e-34c6-a05d-10e8dde9824c | -10.51184 | -50.01482 | 2026-08-17 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 21487030-52b2-36a0-87b7-39b07b8f0287 | -8.97455 | -60.50359 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 99637aee-22b4-3759-91ff-db0a9bd28c10 | -9.4788 | -51.66529 | 2026-08-17 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9d9e9781-2fd5-359d-86fa-5b7173ec1bb0 | -14.05557 | -53.69644 | 2026-08-17 04:57:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3069c8ce-d408-336c-a8fb-a4814c9646f1 | -10.51597 | -50.78646 | 2026-08-17 04:57:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 46cdb744-e068-3c4a-8ce4-42cd4319255d | -8.95207 | -60.59708 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| acd285c9-9356-3d26-8a64-bc56932acf3d | -15.12873 | -50.05454 | 2026-08-17 04:57:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 26032137-6e56-31fa-a197-bb7a65a80424 | -8.03106 | -55.1444 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 449ee08e-b6a3-3c27-8b91-d2f0729013ba | -14.0492 | -53.65102 | 2026-08-17 04:57:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 708fcc98-0d28-3e77-860f-5045ff40b65f | -6.83411 | -58.97597 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4ea61a55-3966-33d1-b2c0-158c1c51e2e7 | -8.89371 | -60.56343 | 2026-08-17 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fcabe222-71b5-3688-9877-1231c84caa1f | -11.4996 | -46.58904 | 2026-08-17 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 80a20860-26be-3e37-8cb2-f77f8ce32e3e | -6.81772 | -56.4473 | 2026-08-17 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bbec061b-9a3e-36d3-88dd-41cb859baa4b | -7.55481 | -60.86709 | 2026-08-17 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9faf44a1-d0a6-39a9-9715-c98d33d9edad | -9.47379 | -51.61076 | 2026-08-17 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 25642af9-bb61-30ac-9b01-7aa0db5f88ad | -8.09296 | -61.36282 | 2026-08-17 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| fd913d9f-7312-30f5-af55-80a12743685d | -8.59518 | -54.67781 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 71bcdec1-0a52-3fba-822c-b52423ea5118 | -12.68097 | -48.44083 | 2026-08-17 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 08357b3c-d562-39c0-9b05-a05aaa429871 | -14.28977 | -53.06136 | 2026-08-17 04:57:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 55dfe7d7-c46b-3e0a-8600-399e73b41972 | -11.55301 | -46.85208 | 2026-08-17 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b8176417-ff25-3d5c-a0ee-f264edb7398b | -11.09738 | -47.29351 | 2026-08-17 04:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4c3b2ce0-cf32-30da-a432-c27b994984ec | -6.62048 | -58.96653 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 13e50a36-ce7f-3a81-b39b-6383d8b28172 | -12.20495 | -52.86656 | 2026-08-17 04:57:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0deb2dee-d3e8-3a8f-a8c4-67b015c0f3e9 | -6.78518 | -59.46958 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d68fe1cd-c48b-3705-9125-3691fa1301fb | -8.64481 | -54.71837 | 2026-08-17 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c82b3fe8-8dc5-336f-987d-3b2e094054cc | -11.51232 | -54.62079 | 2026-08-17 04:57:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d719fa1e-2566-34dc-a07d-02a9947ca3e0 | -9.36923 | -62.36592 | 2026-08-17 04:57:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 71240042-be24-357d-8198-e6c50487faca | -11.21759 | -54.01444 | 2026-08-17 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e697b389-5264-36ac-bdb8-aa7373ffc605 | -6.62076 | -59.0643 | 2026-08-17 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1a4306a5-2d3c-331d-b7b0-aea1e5320193 | -12.75826 | -48.43669 | 2026-08-17 04:57:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README33.md)
