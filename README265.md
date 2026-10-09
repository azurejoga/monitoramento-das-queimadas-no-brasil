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

## Dados Diários - Página 265

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 61ed8571-cee7-31a6-8cee-72891b419104 | -12.2855 | -41.5663 | 2026-10-09 15:58:00 | NPP-375 | IRAQUARA | BAHIA | Brasil | 2914406 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 32161f61-138c-3fca-bcbb-fad75cecf43a | -11.48553 | -39.12046 | 2026-10-09 15:58:00 | NPP-375 | BARROCAS | BAHIA | Brasil | 2903276 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| b247a535-4570-3d70-952c-7a0ff8e7af80 | -11.97948 | -43.49634 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| a5ef854e-0dce-3b5a-9707-26a44d057b9f | -14.4403 | -40.7871 | 2026-10-09 15:58:00 | NPP-375 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 983af94c-c82a-3556-b389-7ab3753a8614 | -12.21494 | -44.74296 | 2026-10-09 15:58:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| f8ae5836-b108-33b5-ab4a-5076dfcf748d | -14.94482 | -41.0631 | 2026-10-09 15:58:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| ed74e172-54be-3fc7-8769-7bc7a5656895 | -17.5227 | -42.44522 | 2026-10-09 15:58:00 | NPP-375 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 7b381ff8-8bd3-3af2-821e-90973f621804 | -15.25195 | -42.38049 | 2026-10-09 15:58:00 | NPP-375 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 117.8 |
| fc7e5d5c-6160-321c-b93e-9b998eb11e7f | -13.25912 | -42.25764 | 2026-10-09 15:58:00 | NPP-375 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 590ecea8-635f-3bdc-a729-001f30b02143 | -11.60753 | -43.62753 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 72291a45-6229-328c-8d44-5906e02d6ba6 | -15.38124 | -41.89126 | 2026-10-09 15:58:00 | NPP-375 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 71.3 |
| 6a82ecb5-6247-3b31-a382-3aafcc4f518e | -11.99052 | -43.49165 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| f421b9bb-0081-39dc-8e77-f8418cce266b | -16.71309 | -41.88686 | 2026-10-09 15:58:00 | NPP-375 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| a123bbab-e707-38cb-a528-927ec7dba9f6 | -15.11123 | -43.63969 | 2026-10-09 15:58:00 | NPP-375 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 15.6 |
| 23ac3bbd-421a-392a-9c5a-2bdae726a270 | -14.05696 | -44.7984 | 2026-10-09 15:58:00 | NPP-375 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| d54ebf98-72eb-3d40-9af2-1879b7d89de9 | -15.38166 | -41.89497 | 2026-10-09 15:58:00 | NPP-375 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 94.2 |
| 6b0f0689-f647-3b57-8f92-7a56047cab3e | -15.37175 | -41.90374 | 2026-10-09 15:58:00 | NPP-375 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 59b1a1db-862e-3339-a048-1d4b476122bb | -14.74911 | -41.38382 | 2026-10-09 15:58:00 | NPP-375 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0a4b399b-9e79-3ae3-9a87-dc80d46a480e | -15.25665 | -42.37189 | 2026-10-09 15:58:00 | NPP-375 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 29.3 |
| 52a1532d-388d-3d24-9ae5-fe3ae684d340 | -14.41096 | -41.04279 | 2026-10-09 15:58:00 | NPP-375 | CAETANOS | BAHIA | Brasil | 2905156 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 91d03af8-7bb8-36e7-8d86-189f5fbecaaf | -16.15815 | -42.31182 | 2026-10-09 15:58:00 | NPP-375 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| f9029b22-e421-3358-97b1-60444cec0208 | -12.16645 | -44.70388 | 2026-10-09 15:58:00 | NPP-375 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| dd51ba50-40c1-34c3-9773-ad23f8c5e5a9 | -15.8045 | -41.33115 | 2026-10-09 15:58:00 | NPP-375 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| de183efc-2889-3232-b7c0-7208491fecf2 | -13.25329 | -42.25434 | 2026-10-09 15:58:00 | NPP-375 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| c5aaf295-bb36-3b42-aa4a-6e70e2ab2263 | -11.98408 | -43.47772 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| b1ddc491-5021-3d75-871c-5b8f5b0f845e | -14.76289 | -40.8954 | 2026-10-09 15:58:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.0 |
| 91111a6d-2c62-3f63-a63a-bbb27afc2afb | -14.06087 | -43.84126 | 2026-10-09 15:58:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 37.8 |
| c5e2968a-5267-3500-9966-90d0d354520c | -14.58582 | -41.20159 | 2026-10-09 15:58:00 | NPP-375 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 35.2 |
| c9e697b2-a04e-3312-8a76-ed2b56aab735 | -14.05222 | -44.81482 | 2026-10-09 15:58:00 | NPP-375 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 38c7bd87-dd1f-3a4b-a6e4-c45d008cb07b | -11.78501 | -46.81308 | 2026-10-09 15:58:00 | NPP-375 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 8673f79b-33f0-3776-8325-172d2805e142 | -14.33037 | -41.30532 | 2026-10-09 15:58:00 | NPP-375 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 126.7 |
| f71be6fb-89c6-358d-a76f-832836e541f8 | -14.46435 | -41.95472 | 2026-10-09 15:58:00 | NPP-375 | GUAJERU | BAHIA | Brasil | 2911659 | 29 | 33 | nan | nan | nan | Caatinga | 9.3 |
| c1535d60-4785-3a8e-934a-229169818827 | -18.78756 | -46.4734 | 2026-10-09 15:58:00 | NPP-375 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| f8b22c4e-1b2b-38cc-a07a-ba66806c35aa | -12.00882 | -43.44139 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 20.6 |
| c1acd17e-f85c-3004-b2ff-39b610f45641 | -13.08722 | -46.80632 | 2026-10-09 15:58:00 | NPP-375 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 15.4 |
| aca6ec92-8c95-3dfa-bb7b-70d8a0bab70b | -11.58734 | -43.65424 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 0c7de71d-165b-3741-aa96-2fc770f3ff64 | -12.22092 | -39.00448 | 2026-10-09 15:58:00 | NPP-375 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 06904a47-0720-30d0-81a8-676b0f9c3f10 | -11.5864 | -43.6462 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 263.3 |
| 66db2ca1-dc08-3327-87b1-edc2aceaec44 | -11.99351 | -43.46885 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 8cbe9744-c842-3ba4-b88c-bc5345a8c340 | -15.37789 | -41.90968 | 2026-10-09 15:58:00 | NPP-375 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 172.9 |
| 483539b1-d593-3720-a110-e9a6ea42e58f | -16.12493 | -43.74487 | 2026-10-09 15:58:00 | NPP-375 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f6aae4e0-174f-3594-b375-63dcacdeaadc | -14.08928 | -40.38956 | 2026-10-09 15:58:00 | NPP-375 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| a188c4e6-8520-35da-84ce-7ba7e0e5f279 | -14.49137 | -40.82913 | 2026-10-09 15:58:00 | NPP-375 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 19.2 |
| 63293c42-e249-3c3b-8c9a-6240a4c6dd18 | -15.1651 | -43.80076 | 2026-10-09 15:58:00 | NPP-375 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d9528e5e-e8ac-386e-87f3-050655cd6c88 | -11.70148 | -43.42653 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 62268b07-f5f9-38f6-82d8-b636ed7d6a1f | -15.39369 | -41.9046 | 2026-10-09 15:58:00 | NPP-375 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 42.4 |
| d07903fc-6080-3f63-99d3-19ed54a366e2 | -16.13558 | -41.68914 | 2026-10-09 15:58:00 | NPP-375 | MEDINA | MINAS GERAIS | Brasil | 3141405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.1 |
| bdbdb306-b769-3899-9167-0de32a07074b | -16.97352 | -41.15793 | 2026-10-09 15:58:00 | NPP-375 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.8 |
| 7192edab-a8bb-30b7-a216-19d9e8038ffe | -12.16084 | -45.35353 | 2026-10-09 15:58:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 2e5ed1f7-8347-33ef-b4dd-2917e1a12d4a | -15.74876 | -40.58029 | 2026-10-09 15:58:00 | NPP-375 | MACARANI | BAHIA | Brasil | 2919702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 0b5aad9f-ffe4-360f-9321-bfc6bd01a25b | -16.67513 | -43.74948 | 2026-10-09 15:58:00 | NPP-375 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a6db5e17-5731-3fa8-8840-453996635131 | -14.52077 | -41.24815 | 2026-10-09 15:58:00 | NPP-375 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 27.2 |
| 6fde2733-0911-3eac-af17-a14f3ff85eab | -14.65153 | -41.27674 | 2026-10-09 15:58:00 | NPP-375 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 16.1 |
| fd27092c-e916-3e98-a43f-8d0aa240268d | -11.61618 | -43.60227 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 2ad0a7d4-8c5c-3dae-b9ef-55b34d85bdcc | -14.04834 | -40.45124 | 2026-10-09 15:58:00 | NPP-375 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |
| be989cd1-099c-3a45-844b-ff3ea6aa80ca | -13.11394 | -46.33685 | 2026-10-09 15:58:00 | NPP-375 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 2145a774-b214-3368-8eb7-e0c8a7efbe3e | -12.19746 | -44.64636 | 2026-10-09 15:58:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 49d87407-f86a-37f0-9261-4e07d4e9b239 | -11.97201 | -43.48267 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 308475a0-fe68-352d-836a-9f53f0fc9751 | -15.42754 | -44.35302 | 2026-10-09 15:58:00 | NPP-375 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e84a35fc-7e23-3f2c-b58b-cffb0156cab8 | -13.25946 | -44.00061 | 2026-10-09 15:58:00 | NPP-375 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 17.0 |
| a2f13ebc-5f2b-36c3-b699-ae25ee6f8657 | -12.20144 | -44.62679 | 2026-10-09 15:58:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 1aecf2f7-f2f9-3b31-a1a2-18c84f05fad4 | -16.23819 | -44.06498 | 2026-10-09 15:58:00 | NPP-375 | MIRABELA | MINAS GERAIS | Brasil | 3142007 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 61995a06-d2e9-35d3-b856-7c93c1b17938 | -15.69035 | -40.72596 | 2026-10-09 15:58:00 | NPP-375 | MATA VERDE | MINAS GERAIS | Brasil | 3140555 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.0 |
| 4a65ffb8-cf67-3d0f-a350-158c6ea4d7e5 | -11.57504 | -41.40873 | 2026-10-09 15:58:00 | NPP-375 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 24.2 |
| 317d281b-04bb-3547-9224-997c98d876ed | -11.90638 | -47.39293 | 2026-10-09 15:58:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 124f124d-6c61-30b2-a614-90b78c2c3f35 | -13.26599 | -44.00446 | 2026-10-09 15:58:00 | NPP-375 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 98435fae-ecef-3d3f-b3ad-fbf260836e48 | -15.91613 | -38.96603 | 2026-10-09 15:58:00 | NPP-375 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| eefa975f-11c0-3601-815f-7484e4f4a473 | -12.90902 | -45.12059 | 2026-10-09 15:58:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 73e31ac5-6ef1-3aaf-8251-6ea54526e648 | -11.4804 | -43.39688 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| efad6d29-146a-33ff-a810-5a9748293b40 | -11.98843 | -43.46515 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 26.4 |
| f3e9dfc2-a54b-3f82-aa28-4a0eedb3308c | -11.57481 | -43.69811 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| b355ef19-e8a9-32d0-b8f7-f44057193da2 | -11.98727 | -43.46524 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 7fe8ec74-6c8f-3ead-bae2-cf9e16868020 | -15.691 | -40.73139 | 2026-10-09 15:58:00 | NPP-375 | MATA VERDE | MINAS GERAIS | Brasil | 3140555 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.3 |
| 5f659a65-8163-3582-9494-bce25a99c6c5 | -15.25759 | -42.36851 | 2026-10-09 15:58:00 | NPP-375 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 36.1 |
| a76f8609-50d0-33b9-b568-79bdbeb60bea | -14.05859 | -44.81395 | 2026-10-09 15:58:00 | NPP-375 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 1f9e53e1-a32b-37f2-bba1-6edacd27ca80 | -16.12434 | -43.39956 | 2026-10-09 15:58:00 | NPP-375 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 070083e8-19a4-351a-8d2d-89880b447b98 | -13.08648 | -46.79939 | 2026-10-09 15:58:00 | NPP-375 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 16.7 |
| d4b92209-0d8f-3dd5-8a8a-ff58af843e56 | -12.22219 | -43.95203 | 2026-10-09 15:58:00 | NPP-375 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 33.6 |
| f14546dd-e314-3c52-9c5b-612f7aae302d | -13.25375 | -42.25829 | 2026-10-09 15:58:00 | NPP-375 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 977ee25d-8ce8-3c64-90e5-287797ffd3cf | -11.89265 | -47.40147 | 2026-10-09 15:58:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| fa747d34-e70d-3b55-954e-3bd9e74da195 | -16.51079 | -43.14882 | 2026-10-09 15:58:00 | NPP-375 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 90ee6a25-4c0c-39a3-a45a-3a30030c96b0 | -13.58312 | -40.01073 | 2026-10-09 15:58:00 | NPP-375 | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 12.6 |
| 89ed43c7-b38b-3f16-973a-f8337f565cfe | -12.70436 | -43.07949 | 2026-10-09 15:58:00 | NPP-375 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 11.5 |
| a5bd752c-f3b3-3fb8-bbac-a9a91c8affc0 | -13.33143 | -40.38389 | 2026-10-09 15:58:00 | NPP-375 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.4 |
| c4ed8a64-27a4-3fd0-8069-7eca21df338e | -12.67556 | -39.1015 | 2026-10-09 15:58:00 | NPP-375 | CRUZ DAS ALMAS | BAHIA | Brasil | 2909802 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 57a94514-5c94-38eb-9243-cc78488cc85a | -11.58251 | -43.66292 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 15c2d85d-762c-311b-a708-3df2a854af12 | -11.58128 | -45.40351 | 2026-10-09 15:58:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 19.5 |
| f4ac5014-b52c-31be-b816-a6f51af39c71 | -16.85431 | -41.09055 | 2026-10-09 15:58:00 | NPP-375 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 63.5 |
| 05f54ed9-e243-3e8b-9962-0317613595c4 | -15.07847 | -40.44028 | 2026-10-09 15:58:00 | NPP-375 | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| ac4e2ee5-27b8-3f09-bcf2-4ee784d7e117 | -11.70716 | -43.42585 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| fe1995f1-a902-31e5-8993-4f3c6b86aede | -12.20199 | -44.63152 | 2026-10-09 15:58:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| d5d22e0f-e9ff-3ec6-80a0-1eb1d77e3b0b | -11.77649 | -46.79983 | 2026-10-09 15:58:00 | NPP-375 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 27af43b9-33da-3b70-b7d9-571ba45c4e37 | -13.24065 | -39.7639 | 2026-10-09 15:58:00 | NPP-375 | UBAÍRA | BAHIA | Brasil | 2932101 | 29 | 33 | nan | nan | nan | Mata Atlântica | 21.5 |
| f25488be-9870-396d-aa0f-c696d59e8594 | -16.13822 | -41.69114 | 2026-10-09 15:58:00 | NPP-375 | MEDINA | MINAS GERAIS | Brasil | 3141405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| 8a74bd0c-de9b-3cb6-be22-d0f75e137c7a | -11.57741 | -43.67162 | 2026-10-09 15:58:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| aee9df23-8850-326e-8481-02f5b97559c2 | -12.3461 | -47.31439 | 2026-10-09 15:58:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 79a24e6f-4334-37fa-a560-4ce4013f71ef | -15.37709 | -41.90269 | 2026-10-09 15:58:00 | NPP-375 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 61.2 |
| f799d83c-fecc-3a67-80af-97e0be936596 | -11.9746 | -43.45639 | 2026-10-09 15:58:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 0513bae0-7dd7-35b9-81b5-e0d5b279395f | -14.48517 | -42.15953 | 2026-10-09 15:58:00 | NPP-375 | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| fcc01418-e3c8-3008-aea9-d94564e08eb6 | -14.32529 | -41.30618 | 2026-10-09 15:58:00 | NPP-375 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 94.8 |


[Clique aqui para ver as próximas entradas](README266.md)
