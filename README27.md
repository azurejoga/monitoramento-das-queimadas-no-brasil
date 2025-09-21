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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 07f18212-37e4-3afb-8f2d-6a55e2c3fd7b | -12.08011 | -44.80719 | 2025-09-21 04:36:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a061fb59-394e-3dbe-9fac-c123232a8582 | -6.69026 | -44.09454 | 2025-09-21 04:36:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b750c6f5-5ffa-3a15-a56e-b605942cf96c | -7.21826 | -43.75282 | 2025-09-21 04:36:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 44a333be-98af-357b-86a0-bfd580c26edf | -12.08476 | -44.85673 | 2025-09-21 04:36:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0fb0410b-b354-3d1f-9d19-e3d98abce46d | -6.39302 | -44.62767 | 2025-09-21 04:36:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e210bce6-9ddc-3a16-aea6-763c296d9310 | -7.93396 | -44.09496 | 2025-09-21 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8f2e02db-f2e5-305f-859f-50bcba0dea86 | -10.24326 | -48.07309 | 2025-09-21 04:36:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 92d2ef43-b4a5-3903-aef3-2686cb4b8a32 | -10.28219 | -46.06795 | 2025-09-21 04:36:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 21d039a5-3ab8-3fb7-a08e-7096987792bf | -11.30812 | -47.50191 | 2025-09-21 04:36:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 54323201-7e3d-396b-8170-c4a8616a0efd | -5.6967 | -51.75395 | 2025-09-21 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7595403a-c1b5-33af-90a8-404ebcbc3659 | -11.77455 | -43.76453 | 2025-09-21 04:36:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8d3bb854-79fb-3cfa-807d-965e6382c048 | -7.2144 | -43.75223 | 2025-09-21 04:36:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8bdfd085-be89-3f23-8b6e-b0dac8c25c81 | -10.26786 | -46.05012 | 2025-09-21 04:36:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| edb3bfd8-6254-3a54-8fe8-5e190c5199c9 | -10.57442 | -48.59137 | 2025-09-21 04:36:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0195a538-8214-3fdd-ae04-9dcc969ec653 | -7.61681 | -44.44529 | 2025-09-21 04:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fc677105-cbdd-3dde-9265-70287d24b7c0 | -11.31208 | -47.49874 | 2025-09-21 04:36:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e378b91f-9239-31d9-a226-75c91ce3ecc7 | -11.30756 | -47.50557 | 2025-09-21 04:36:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e6c40ea2-ab2a-3d32-8ff9-301cb8e978f9 | -12.08089 | -44.85619 | 2025-09-21 04:36:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 29f3497c-067b-3cec-9d8f-22328a0a896c | -11.2051 | -49.62984 | 2025-09-21 04:36:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 928ee91a-c0d9-3f0a-9df1-e43bd5b8dc8f | -5.64818 | -51.4646 | 2025-09-21 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5c6d6878-f373-3907-a2a7-f1fa0447d8c4 | -10.28611 | -46.07328 | 2025-09-21 04:36:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d62eb10e-ab7c-3512-95dc-e26d9cf8028d | -7.91589 | -44.11157 | 2025-09-21 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4d583ac0-9143-3724-a459-7cd462cf0d3d | -7.71898 | -44.45179 | 2025-09-21 04:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5dea4827-1656-3034-ac72-2a8eb1f5344a | -10.361 | -47.90207 | 2025-09-21 04:36:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c596d4fc-cdff-3eec-9031-852c4a93eff2 | -10.34495 | -45.23326 | 2025-09-21 04:36:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4d2e1fc4-c046-3cdb-be50-b797c8562188 | -8.94581 | -44.20596 | 2025-09-21 04:36:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce9b9f8e-46e4-3f7f-8539-82b9d8f1f81b | -11.78331 | -43.76201 | 2025-09-21 04:36:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 448f5963-da9d-36b1-b5ff-0bf91a7a3331 | -7.72603 | -44.45963 | 2025-09-21 04:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d5cc12f4-a861-3ad6-836d-feae55f89766 | -7.83143 | -45.61972 | 2025-09-21 04:36:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 09bb5c68-663e-3157-b397-6bb26d6aeaa6 | -10.29756 | -46.08655 | 2025-09-21 04:36:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 96ba09fb-1d7b-3c2c-9829-5f34532cd5b2 | -11.02248 | -44.64979 | 2025-09-21 04:36:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 14db612a-5393-34ed-b9f1-0b04407db028 | -9.08337 | -49.64346 | 2025-09-21 04:36:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 15463446-3736-3240-a0a4-9852b9847ab5 | -5.69394 | -51.75619 | 2025-09-21 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 40842a5d-45c7-32dd-a970-70c0caa6a1e1 | -12.08081 | -44.80237 | 2025-09-21 04:36:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 762af0f0-4eae-3204-a8b0-53eeb10746ea | -7.80808 | -46.17981 | 2025-09-21 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7b39df99-a0ab-3607-9a1c-f0fbb8e1dcb4 | -7.38114 | -47.04893 | 2025-09-21 04:36:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 52c079b2-c5ee-3142-8d66-62950284b71b | -11.29571 | -47.5149 | 2025-09-21 04:36:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5aef10f8-8ec7-393f-9363-4088852f8430 | -10.2637 | -46.0536 | 2025-09-21 04:36:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 74dc470b-7c1c-30d2-ae81-6fccbe991284 | -7.72136 | -44.46126 | 2025-09-21 04:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 717235d2-391e-32d0-a3c3-2f7259a7c941 | -6.03299 | -46.3651 | 2025-09-21 04:36:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d8bbd08f-173b-33c1-be86-729be13fb04a | -7.38953 | -47.0393 | 2025-09-21 04:36:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ca356d0-22e4-3836-a97e-552ba25dc88b | -7.5671 | -44.73306 | 2025-09-21 04:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b337b783-7e64-3bb7-ad41-a1b255c6d365 | -10.25551 | -48.06041 | 2025-09-21 04:36:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 715419c5-b766-377d-81fe-747bbc426dd7 | -11.43325 | -47.31935 | 2025-09-21 04:36:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7b8f10be-7a54-3285-9567-117f1491f534 | -12.07241 | -44.84202 | 2025-09-21 04:36:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3a46d641-d5a6-3bb0-8276-3eb41fca86f5 | -11.30305 | -47.51232 | 2025-09-21 04:36:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7478ad14-79a0-34dd-8deb-51302cebe5c4 | -10.29697 | -46.09056 | 2025-09-21 04:36:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 2a239b51-7844-3f7d-a5ca-c12bb564a53b | -7.93951 | -44.11031 | 2025-09-21 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4b2ce228-40b5-33e5-9e42-6ca3456e7c05 | -10.03767 | -46.26276 | 2025-09-21 04:36:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38e6b1a1-cfb1-388c-aac4-0eb25c6b8ccb | -11.29442 | -47.40902 | 2025-09-21 04:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fdad41bb-9b85-3c35-b343-d0380102ff2b | -8.59963 | -45.34464 | 2025-09-21 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 35702ef3-1ced-3ad9-a5b7-8c11d240be86 | -10.03824 | -46.25895 | 2025-09-21 04:36:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ceb61fc1-b142-3b37-85c7-0492fe29b506 | -11.20965 | -42.19554 | 2025-09-21 04:36:00 | NPP-375D | CENTRAL | BAHIA | Brasil | 2907608 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 5a5100ef-464f-3030-b3f8-598f1a359b3d | -12.33932 | -44.09558 | 2025-09-21 04:36:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b1f69bad-099d-3cc1-b050-4269b7797327 | -8.83205 | -43.03828 | 2025-09-21 04:36:00 | NPP-375D | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c59b292c-af4d-3a05-a6dc-7e695b95005b | -7.72509 | -44.46185 | 2025-09-21 04:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f4a80efb-8988-31b2-89a4-44d23f53c9c8 | -6.31728 | -45.91974 | 2025-09-21 04:36:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 17991beb-f7eb-3856-98c9-88bd11dabbf1 | -12.0952 | -44.79166 | 2025-09-21 04:36:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de2d1405-93fa-3976-ab08-237109695ad9 | -10.33888 | -45.22304 | 2025-09-21 04:36:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c23a3e8d-de07-3192-b5da-2b2e208852f8 | -10.25327 | -48.05278 | 2025-09-21 04:36:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 735bcc39-bcec-3c49-8623-249c0abc0c37 | -7.64645 | -46.77744 | 2025-09-21 04:36:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f202b5e3-78de-3b56-8079-a4028868b4fe | -7.71986 | -44.44955 | 2025-09-21 04:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 50b60327-4e73-3400-b967-378035ec7a6a | -8.35186 | -44.70476 | 2025-09-21 04:36:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86dce664-d9aa-3544-a0b7-879e020a9237 | -10.41679 | -47.85241 | 2025-09-21 04:36:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d5d80b50-4f07-37fa-8e7f-88cad10cd904 | -5.3854 | -50.53268 | 2025-09-21 04:36:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5b96790a-f73e-3f4b-b9e0-d9601d4897d6 | -7.7166 | -44.47189 | 2025-09-21 04:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1f1a64b2-5002-3327-b58b-665c65543d77 | -11.25501 | -49.84232 | 2025-09-21 04:36:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0f9c87e2-7531-3017-bbce-14a74f712478 | -11.49857 | -43.58897 | 2025-09-21 04:36:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 34c8dd61-ad9a-3caa-9097-e26d25a3ea80 | -9.43268 | -44.70718 | 2025-09-21 04:36:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 40a94749-fc1c-34c0-875a-bbb410877221 | -12.11559 | -44.84361 | 2025-09-21 04:36:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2217e6c7-d0cf-3037-bf27-6b320fe21379 | -12.07033 | -44.82019 | 2025-09-21 04:36:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 81fd4d63-ba9b-3c06-842e-19d0d17c87c5 | -10.34932 | -45.22921 | 2025-09-21 04:36:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 67b686a9-59f5-32a7-839c-7cb326cb68fe | -7.77102 | -44.17754 | 2025-09-21 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 98f6e20d-b7b0-3a74-bab8-a787541516d2 | -12.07626 | -44.84274 | 2025-09-21 04:36:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 36cdb13b-4374-3c96-89e2-477b619f6e83 | -7.61922 | -44.44713 | 2025-09-21 04:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e360bec0-050f-3b6d-83d7-f2616ef27a06 | -7.92422 | -44.10801 | 2025-09-21 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 32abe4e4-097a-3059-a63e-2c84b7cfd85c | -7.4475 | -42.61952 | 2025-09-21 04:36:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 442feb39-a155-3549-9879-31c8534539d7 | -10.3431 | -47.88459 | 2025-09-21 04:36:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1aad2069-c8ab-34cf-9cfa-ac97a5bc9569 | -15.24775 | -50.2236 | 2025-09-21 04:38:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a3c26289-64a2-3ec5-a94b-d21e9437000e | -15.47019 | -49.97022 | 2025-09-21 04:38:00 | NPP-375D | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c6f45b7d-beed-3dbb-9e90-18b25b2eec24 | -14.46297 | -46.50315 | 2025-09-21 04:38:00 | NPP-375D | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f20bf972-4c30-3b16-9c37-9b097a086e39 | -14.45933 | -46.50263 | 2025-09-21 04:38:00 | NPP-375D | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 116a8d8b-4c20-3494-bfa0-e5aaa562773c | -14.4557 | -46.50208 | 2025-09-21 04:38:00 | NPP-375D | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f63f0aba-2f8c-3361-a100-e1b4e8c61952 | -14.45024 | -46.51432 | 2025-09-21 04:38:00 | NPP-375D | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9405ff39-43e9-3870-852e-a0ba0548880b | -18.74624 | -53.32727 | 2025-09-21 04:38:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 398bb87f-aff5-3753-b084-bcc0b8826eb5 | -19.90608 | -44.719 | 2025-09-21 04:38:00 | NPP-375D | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 94358496-50aa-391e-826c-74cee727ec23 | -16.60372 | -45.09525 | 2025-09-21 04:38:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3bf34c11-410a-36af-b310-76376addc57d | -11.62059 | -50.60274 | 2025-09-21 04:38:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2dbc2a7e-e215-30de-9e90-957db88b7080 | -15.68912 | -46.99285 | 2025-09-21 04:38:00 | NPP-375D | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a424daf3-9026-3fe8-92da-032149468bfe | -13.3106 | -47.27894 | 2025-09-21 04:38:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 34d7938e-b124-3f11-8ed4-035905f306dc | -14.80556 | -51.38227 | 2025-09-21 04:38:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ef8c716a-936c-3eab-a276-d1635dc79af8 | -15.94361 | -59.42317 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a5416c15-c422-3bc4-8e6e-6e3139d66ee9 | -11.93539 | -48.7079 | 2025-09-21 04:38:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8a025d26-5767-3a40-86f9-30a70be919d0 | -11.58479 | -50.28832 | 2025-09-21 04:38:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| db63a3e3-b40f-3cfd-886e-0bd0b14a2abe | -14.61721 | -49.75935 | 2025-09-21 04:38:00 | NPP-375D | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d1ecbf4e-80ab-3179-9ea5-9dc7a524ec48 | -14.81175 | -51.3872 | 2025-09-21 04:38:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 60bb4407-f297-3bbc-b4e5-1a64d453c075 | -15.81604 | -59.51758 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f4c98c7b-f1e3-3881-a868-dd6b50b3cdc6 | -15.94829 | -59.45439 | 2025-09-21 04:38:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8230108b-e7a7-3162-ba99-3f61833ea36d | -18.8991 | -44.28449 | 2025-09-21 04:38:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7d813de5-8bf7-3713-bb77-077054a915de | -14.62374 | -48.27257 | 2025-09-21 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README28.md)
