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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1b35b7a9-6a38-379d-a83e-f110ca23a929 | -6.95565 | -44.30596 | 2025-08-31 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fc0ccb9d-ac83-3e60-aeda-56d49faa4422 | -9.58878 | -40.35349 | 2025-08-31 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9e3021ed-21cc-3edd-b3fe-c30b948691fc | -11.41293 | -44.68598 | 2025-08-31 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 994c99a3-3d7f-3bf3-9b04-87a2b168971f | -6.17869 | -44.13947 | 2025-08-31 04:02:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 82e7d867-4afc-38f8-917e-37b35e3c873f | -6.18783 | -44.13139 | 2025-08-31 04:02:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 47b06682-7b3c-3e18-ab36-443e44136021 | -6.15582 | -44.13766 | 2025-08-31 04:02:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 480db1e5-321a-3afc-ab25-6c40e4e906af | -6.86843 | -45.15073 | 2025-08-31 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 250468a3-a01e-3fc6-a3ef-55039898ba95 | -11.36628 | -43.57787 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 529de842-cd1e-3545-8b5c-3073320e5515 | -6.8209 | -43.34248 | 2025-08-31 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| bce1d9f7-1d85-3264-be68-4bbcdd723714 | -10.60956 | -44.32775 | 2025-08-31 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3b427772-efc1-329b-b48a-41593fbfc14d | -7.37905 | -43.40538 | 2025-08-31 04:02:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 583f4260-e1d7-3090-a84f-ab158d70b2fe | -9.59594 | -40.35105 | 2025-08-31 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 28.1 |
| 50fc041c-0980-3e0f-959b-60794e9834bc | -6.28151 | -43.54489 | 2025-08-31 04:02:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 25d2bb1e-3ed8-3f9f-9b0b-9338c85acd3a | -8.88883 | -45.0879 | 2025-08-31 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c97fdbb-2608-31e7-9135-f2d6bfcd0c37 | -6.33683 | -53.43093 | 2025-08-31 04:02:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4b9de298-afec-3541-a3e2-6ecadd9b0092 | -7.32812 | -44.09809 | 2025-08-31 04:02:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 67f46c31-71ca-31a3-aaa0-b03b926948b0 | -7.9523 | -46.42302 | 2025-08-31 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 98f7ed5e-751b-3b9c-bb70-20a80d1c580b | -8.54465 | -45.80724 | 2025-08-31 04:02:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| cb2d9486-018f-3cc4-8b0d-95266fe8b0bd | -11.31928 | -43.69045 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d25e09b1-5314-3093-a7da-76f7c242325d | -6.57995 | -43.69223 | 2025-08-31 04:02:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| bcea0dfc-d8a5-3a32-b361-8b531c74ada3 | -7.00999 | -42.03402 | 2025-08-31 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| fa7880d2-e2b2-3ccc-b6db-e71d76584ed5 | -7.21895 | -44.21678 | 2025-08-31 04:02:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 457829ce-a4d0-3e6b-ba7f-fbf27d18a3a7 | -6.01862 | -42.71508 | 2025-08-31 04:02:00 | NOAA-21 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| acddc96f-0158-3b8b-b18a-392a88f1bde2 | -8.33063 | -47.41927 | 2025-08-31 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 00c7b312-348b-35e8-aa9e-266cf983c81b | -6.19379 | -42.75468 | 2025-08-31 04:02:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2d38d2e8-4039-360a-ba92-0dafb67eb1a9 | -6.48876 | -43.56337 | 2025-08-31 04:02:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 819b13ea-7775-3876-8ca0-f62bbe07eb40 | -8.30917 | -44.91106 | 2025-08-31 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 74026150-7289-35f1-bc8b-bfa3192d9ac9 | -5.55136 | -44.29436 | 2025-08-31 04:02:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1a1c931-02f5-34c3-830c-5f38158aa1b4 | -7.58926 | -42.71595 | 2025-08-31 04:02:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 555b3ab3-00fd-3bb4-96e2-3052251eeb3f | -6.58067 | -43.68788 | 2025-08-31 04:02:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 121fb7d8-3262-3706-a244-e50c82bc7392 | -5.59098 | -46.32273 | 2025-08-31 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| acf10a91-ee14-3041-b840-07839e902bb7 | -10.47485 | -51.63451 | 2025-08-31 04:02:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a1f31e85-c92a-34e2-8119-78915fc2ae66 | -6.51038 | -45.4207 | 2025-08-31 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ee8d08b5-1f45-3ce0-a190-5a144633b010 | -8.91903 | -40.43972 | 2025-08-31 04:02:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 197abe0f-70c2-3fa9-bc95-aff434678423 | -6.53799 | -44.43853 | 2025-08-31 04:02:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6fb93dc7-f892-34a0-abb7-46b34c3b60ec | -6.22635 | -42.41126 | 2025-08-31 04:02:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5232a045-31be-36b0-accf-defd750f1925 | -7.36678 | -43.3998 | 2025-08-31 04:02:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e65321e9-cbba-3856-9007-9dbc83991751 | -5.76849 | -42.60308 | 2025-08-31 04:02:00 | NOAA-21 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5770e40b-6c14-311e-be44-72e73ce19267 | -7.73854 | -50.26207 | 2025-08-31 04:02:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7d456c2e-47a4-3ca0-a83b-14f13f918ec1 | -5.82287 | -41.26242 | 2025-08-31 04:02:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| cdbe203f-888f-3869-8756-65fa3b8b4dc1 | -5.76765 | -42.60383 | 2025-08-31 04:02:00 | NOAA-21 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a6f6d07b-ba6b-3745-80b0-4f4a68697d85 | -10.10088 | -49.28291 | 2025-08-31 04:02:00 | NOAA-21 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 361ec1ac-51b9-3fa2-a346-eb6e8032182f | -11.29685 | -43.67454 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aaa583e9-a648-3145-a348-64cee5834285 | -6.50557 | -43.55256 | 2025-08-31 04:02:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cd5969d6-fd59-3c2a-b246-7b54b30be318 | -11.35649 | -43.61606 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3a8cff53-e539-32e7-9cf7-2ee014f8475d | -9.69519 | -48.291 | 2025-08-31 04:02:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fe3a9fe2-359d-344a-9143-fe5556614997 | -5.7322 | -44.11665 | 2025-08-31 04:02:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 43e0f914-88e8-36f5-ad94-dd86d7f8e9d4 | -10.93677 | -46.83976 | 2025-08-31 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fe06d39b-2cb7-3788-b115-7ef5de528cd3 | -9.6825 | -47.05378 | 2025-08-31 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0b02a6ac-dc19-3fef-9edf-d4351d494d3e | -7.73302 | -50.26507 | 2025-08-31 04:02:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a3686c88-aedc-3035-aba3-8f33d8c8bae8 | -9.58956 | -46.01001 | 2025-08-31 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| adb46568-c1b6-3b33-b396-1524863462ec | -10.48245 | -51.62403 | 2025-08-31 04:02:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b7672fbd-b3ad-3aff-b53c-b6e22971ec4c | -10.02003 | -48.36697 | 2025-08-31 04:02:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1a822ca1-a370-3e4a-ad7e-6ae0b0528438 | -5.46107 | -42.57289 | 2025-08-31 04:02:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ce8a7b9f-21a2-3ecf-ac97-8f09e7bee47c | -11.29225 | -43.63757 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c2056efb-4e83-327a-ad9b-d27885d4e042 | -6.86001 | -44.44024 | 2025-08-31 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5793f3f8-afca-3901-981e-398a50e01dd8 | -7.32704 | -44.36341 | 2025-08-31 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5ca5ca43-ba6b-3691-930a-f46132bbba8c | -6.31258 | -43.6077 | 2025-08-31 04:02:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8b4dd0ed-2a17-3dfb-a44f-c447cf9d44a2 | -6.53078 | -42.95837 | 2025-08-31 04:02:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f9159047-2648-35e3-b910-235c08b94d58 | -11.06327 | -44.6434 | 2025-08-31 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d7d83d0b-8233-350f-b175-78caedfa5780 | -8.96727 | -44.44019 | 2025-08-31 04:02:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ae0b9594-5803-3f91-8023-2b2c7d6aad6f | -6.64543 | -44.25563 | 2025-08-31 04:02:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1a38d9eb-897c-3acc-9f62-225ece51d16c | -7.58579 | -42.7154 | 2025-08-31 04:02:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ac6abf0a-2e55-3a92-b2dd-e183661a608d | -6.44825 | -42.40694 | 2025-08-31 04:02:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a8b33847-eb3b-3150-a459-5bc712e2a43e | -11.00941 | -46.94913 | 2025-08-31 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6e788824-874d-3e59-a027-97340964a6bd | -11.32664 | -43.66742 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 49fa7e79-5582-3b1e-9d98-99d29cff640f | -10.03009 | -48.09196 | 2025-08-31 04:02:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| cc8f690e-7a37-310b-8bf0-a913c36056b7 | -11.29677 | -43.61029 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 211f0057-b247-3b58-aae7-b72bb14d70bb | -11.02454 | -46.88667 | 2025-08-31 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b613030d-bf3f-37fe-b55a-8e9d8f73d7e6 | -9.59101 | -40.36099 | 2025-08-31 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 28.1 |
| 32336bbf-9708-3aaa-8b8a-576fce796df8 | -7.64395 | -42.72031 | 2025-08-31 04:02:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5c38829e-78a0-341f-88a3-61021e43a073 | -11.06545 | -44.63033 | 2025-08-31 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 84d9e116-528b-3be2-8789-e5b7d1556428 | -11.0764 | -44.63219 | 2025-08-31 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a6cade54-46a6-3e13-b91c-3734d91643f4 | -10.42047 | -50.86314 | 2025-08-31 04:02:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 406a8846-493f-3a1d-b0da-c744d0555c41 | -6.21939 | -42.77518 | 2025-08-31 04:02:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 44d6a866-62e4-3e84-aab5-a2681b930f2f | -11.29726 | -43.65047 | 2025-08-31 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d19b0437-aed5-36f1-ac11-e8603040420d | -6.17827 | -43.34799 | 2025-08-31 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b1bc8fcd-3eec-388e-9c33-d383e40853f0 | -11.01883 | -46.86992 | 2025-08-31 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 9833bec4-d08a-3116-a989-27a2ca1d4b17 | -7.76725 | -45.45645 | 2025-08-31 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 03a3e929-7e1b-349c-a156-adff7a5079e1 | -4.91798 | -42.09072 | 2025-08-31 04:02:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6bb4b39e-a210-3168-8613-6ba7cdc0c0b8 | -6.16872 | -44.1301 | 2025-08-31 04:02:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b73384eb-579d-36b6-a37b-ec7e5d764ec2 | -4.14781 | -46.45175 | 2025-08-31 04:02:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e476549b-0ece-32f7-aa6f-6fad49801a06 | -6.95457 | -42.0099 | 2025-08-31 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 358dc87a-acdc-350e-bc5e-fde8c781b693 | -7.78092 | -43.90044 | 2025-08-31 04:02:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b235c8e3-c00b-3402-a270-6ee0fe90311e | -5.53391 | -36.85304 | 2025-08-31 04:02:00 | NOAA-21 | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 80cf85a2-0cef-3b62-aec2-cd99e7783066 | -6.49022 | -43.55463 | 2025-08-31 04:02:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 09e97a97-c6f7-3e7b-9428-4ed08348099f | -6.80691 | -44.31181 | 2025-08-31 04:02:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 786f718f-0bbd-37cd-934d-d113ac2db791 | -9.26006 | -47.06208 | 2025-08-31 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 37d19a1e-ec5a-3090-b7b2-92a36b8aea2d | -6.98604 | -44.12218 | 2025-08-31 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a853992f-fd27-3202-9d06-3d5edf7db3ea | -6.12654 | -42.94596 | 2025-08-31 04:02:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| aa60a1d2-9a8e-3910-a7f5-7e193b15b694 | -6.515 | -43.54086 | 2025-08-31 04:02:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5cb10b2d-eba2-3d3a-9565-e1ac9ae0a92c | -8.03838 | -45.4174 | 2025-08-31 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| df86e437-80c1-343b-b233-9bfa4c37b37f | -11.05958 | -44.62051 | 2025-08-31 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b8315bc2-971e-3f1a-9a5f-5064e0f3ccbb | -10.04243 | -46.02884 | 2025-08-31 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7736964c-a4db-3c07-bb06-731f6bd6af92 | -7.08776 | -44.33018 | 2025-08-31 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0bb2c39c-901c-3993-99de-bf3e52a1d8ab | -7.9599 | -46.42353 | 2025-08-31 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a441e847-2381-3721-809f-cff78e2ee229 | -7.44765 | -44.81112 | 2025-08-31 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d8785bf6-5978-3005-a243-4e5ef1a08f5b | -5.88341 | -44.33082 | 2025-08-31 04:02:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3a4e8308-9da8-3d94-9a27-1975a3df8689 | -7.70751 | -50.27489 | 2025-08-31 04:02:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8cafbca7-706f-3d2a-81be-aca920b60a1c | -6.83598 | -44.25449 | 2025-08-31 04:02:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README23.md)
