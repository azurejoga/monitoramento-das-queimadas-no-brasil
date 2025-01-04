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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 71ce94db-a090-35e5-b0aa-0f3a27c57ac7 | -8.07761 | -35.13556 | 2025-01-04 03:44:00 | NOAA-21 | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| dce092c1-1485-3e5c-9283-4c73346eeb62 | -7.21599 | -38.64038 | 2025-01-04 03:44:00 | NOAA-21 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 9ba0b11c-77b7-3e35-83d6-a732407878f2 | -13.901 | -39.18345 | 2025-01-04 03:44:00 | NOAA-21 | IGRAPIÚNA | BAHIA | Brasil | 2913457 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 6e661244-701a-33b2-9aff-896fccaac789 | -9.85438 | -37.12582 | 2025-01-04 03:44:00 | NOAA-21 | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 1970d463-3f9a-3649-9110-511479ee41db | -12.09003 | -40.27276 | 2025-01-04 03:44:00 | NOAA-21 | MACAJUBA | BAHIA | Brasil | 2919603 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| fa75ad61-655d-3f04-ae65-89862ff185a3 | -9.55644 | -35.75461 | 2025-01-04 03:44:00 | NOAA-21 | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5b9d6a74-640d-373c-8256-56932f495e8e | -7.69644 | -41.66559 | 2025-01-04 03:44:00 | NOAA-21 | ISAÍAS COELHO | PIAUÍ | Brasil | 2204907 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 004730a2-042d-33ab-9ce1-c4ec509695ef | -6.98489 | -40.0118 | 2025-01-04 03:44:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| eeb12c60-9cca-32ac-b174-e1839bd512c5 | -9.98462 | -36.38643 | 2025-01-04 03:44:00 | NOAA-21 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| ea980104-d0e3-3e4e-adbd-db41b09c9e12 | -8.07376 | -35.13852 | 2025-01-04 03:44:00 | NOAA-21 | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0843a25d-c8a3-3ce4-9e1a-c8b001b40939 | -8.31038 | -38.76253 | 2025-01-04 03:44:00 | NOAA-21 | CARNAUBEIRA DA PENHA | PERNAMBUCO | Brasil | 2603926 | 26 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 32c7291d-351a-3356-b3f8-22e884707b1d | -10.61526 | -44.34494 | 2025-01-04 03:44:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 51434b19-41de-3e68-b12b-7b202eaaf4d0 | -13.9873 | -40.00473 | 2025-01-04 03:44:00 | NOAA-21 | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 7f99706d-3e78-39de-afb4-1f9cb4f6c3f6 | -12.47276 | -46.93491 | 2025-01-04 03:44:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 877da111-b1ef-35ec-acc2-aad035fc0e7f | -10.63486 | -37.11858 | 2025-01-04 03:44:00 | NOAA-21 | SIRIRI | SERGIPE | Brasil | 2807204 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 69bdc762-ea8a-3d83-9829-aabf21173efe | -9.48491 | -35.99279 | 2025-01-04 03:44:00 | NOAA-21 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 6fb6f378-5376-3b08-a0fd-5b917dfc62ae | -13.98899 | -39.99036 | 2025-01-04 03:44:00 | NOAA-21 | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 86d7a908-d22d-3f88-a345-9ef197024976 | -12.27065 | -44.98786 | 2025-01-04 03:44:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 96313ca7-8565-3793-a3a1-392393fbd765 | -11.79924 | -49.32725 | 2025-01-04 03:44:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6990fb7a-b367-369e-8a89-26c6c969200c | -6.98015 | -40.01627 | 2025-01-04 03:44:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 16.4 |
| dc1461ff-6495-3287-b2d7-f92a816b2813 | -8.20586 | -35.29451 | 2025-01-04 03:44:00 | NOAA-21 | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| f2f63ba8-c516-3a06-bb1e-9fa561a8d180 | -9.19593 | -43.15711 | 2025-01-04 03:44:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c1abf826-477f-3429-994f-73024c782794 | -6.70239 | -39.14835 | 2025-01-04 03:44:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f0975fe1-7b0f-3654-9fae-ab9d07f2cf4f | -11.23903 | -39.4082 | 2025-01-04 03:44:00 | NOAA-21 | SANTALUZ | BAHIA | Brasil | 2928000 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 14d49d2b-292c-371c-94ce-8011278d2671 | -12.86074 | -38.36674 | 2025-01-04 03:44:00 | NOAA-21 | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| de7d8ece-65f1-32cb-b383-aa09cdce4247 | -6.97706 | -40.01065 | 2025-01-04 03:44:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 58fff29b-66ab-3aec-ad72-e6f84cd9dafb | -7.97836 | -35.22689 | 2025-01-04 03:44:00 | NOAA-21 | CHÃ DE ALEGRIA | PERNAMBUCO | Brasil | 2604403 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ec152018-1007-31ac-869a-e676ca3b2572 | -10.6139 | -44.3363 | 2025-01-04 03:44:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 125.5 |
| c5cc9228-473d-35ac-b323-8972cc451876 | -6.7061 | -39.149 | 2025-01-04 03:44:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a95d1af6-750b-3081-b7e6-ce5c1a6b9681 | -9.98186 | -36.38242 | 2025-01-04 03:44:00 | NOAA-21 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| c26c1f07-4418-3ede-bb7d-f9c33367c9c3 | -7.21668 | -38.63612 | 2025-01-04 03:44:00 | NOAA-21 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 52d6b8fa-aed7-3afe-aea5-446544f3b231 | -10.53993 | -44.67903 | 2025-01-04 03:44:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c97ed459-b498-353e-98f7-5b7fcdc87887 | -10.56245 | -37.03796 | 2025-01-04 03:44:00 | NOAA-21 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| a29a43c5-7161-33d0-a7a2-89639cdd561b | -9.31819 | -43.16085 | 2025-01-04 03:44:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| fd566a06-ac43-3a1c-a37f-9d15b4d7c8c1 | -10.61627 | -44.33927 | 2025-01-04 03:44:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| d6cd94d1-0c75-3f12-a39d-46850f6c7685 | -7.24466 | -38.41743 | 2025-01-04 03:44:00 | NOAA-21 | BONITO DE SANTA FÉ | PARAÍBA | Brasil | 2502409 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4f306259-e947-3262-83b0-83579e97eb84 | -13.90373 | -39.18395 | 2025-01-04 03:44:00 | NOAA-21 | IGRAPIÚNA | BAHIA | Brasil | 2913457 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 04e801b8-4569-385d-9211-14958520c787 | -7.22028 | -38.63669 | 2025-01-04 03:44:00 | NOAA-21 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 9.6 |
| ada737cd-bf00-3ec2-81bd-94230466ac36 | -10.21943 | -44.7603 | 2025-01-04 03:44:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2732b4d7-5703-3c6b-9751-9e1977c141d0 | -8.43389 | -40.66607 | 2025-01-04 03:44:00 | NOAA-21 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f9de5f67-064e-34e8-aa89-690493f5571d | -10.61494 | -44.33072 | 2025-01-04 03:44:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 68893aa8-3460-35e9-b601-70d3895b9f52 | -11.80045 | -49.32146 | 2025-01-04 03:44:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 32a865d7-978c-3f62-93cb-00d7f2fc1aae | -9.86166 | -37.10154 | 2025-01-04 03:44:00 | NOAA-21 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e2fc25e7-c1ad-35e0-b397-73523a9c6273 | -8.0743 | -35.13504 | 2025-01-04 03:44:00 | NOAA-21 | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| cfd184f7-17c4-3432-82d8-54f9cead48c2 | -11.22132 | -40.1277 | 2025-01-04 03:44:00 | NOAA-21 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c4e2a0d8-eb3b-34fa-99d3-afa732c778ed | -12.2183 | -42.45006 | 2025-01-04 03:44:00 | NOAA-21 | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6ae8a6b2-e9ab-3605-9139-ee6f7e4418ba | -9.98407 | -36.38992 | 2025-01-04 03:44:00 | NOAA-21 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| c864f8c7-518e-3f14-af88-d2b046d24af7 | -10.54384 | -44.68283 | 2025-01-04 03:44:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dd07ab8e-c766-3b6d-9718-ed7ae4b9ca9e | -13.64284 | -41.35844 | 2025-01-04 03:44:00 | NOAA-21 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9172d446-e317-38ba-bc31-d7e4a924eaf1 | -10.41903 | -39.868 | 2025-01-04 03:44:00 | NOAA-21 | ANDORINHA | BAHIA | Brasil | 2901353 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5dd7baa1-0817-32f4-b40d-821a07bc0369 | -7.76691 | -35.51625 | 2025-01-04 03:44:00 | NOAA-21 | BOM JARDIM | PERNAMBUCO | Brasil | 2602209 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 78f3e51f-ea2e-329a-814a-ef1cc49a6b2c | -7.23241 | -39.78118 | 2025-01-04 03:44:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| fcb6536d-8a92-3bd9-99ce-0cb91ca068bb | -6.98178 | -40.00637 | 2025-01-04 03:44:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d470a849-9f01-3995-bb2e-eab36eb4ae44 | -13.46248 | -41.33722 | 2025-01-04 03:44:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f7f1d9b7-1e34-3469-b8b9-a9a1db06b4fc | -7.02308 | -39.65952 | 2025-01-04 03:44:00 | NOAA-21 | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d461e232-fdde-37d1-8efa-ed431ec433ee | -11.80121 | -49.32594 | 2025-01-04 03:44:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 406ce42b-f6bb-367a-8473-4d71d00c98e4 | -13.98673 | -40.0035 | 2025-01-04 03:44:00 | NOAA-21 | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| dd0cf9c7-b62d-398f-8868-a7524c1eeba9 | -6.95015 | -38.10597 | 2025-01-04 03:44:00 | NOAA-21 | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6127deba-10ea-39db-ba41-f891dd58fdf2 | -6.95079 | -38.102 | 2025-01-04 03:44:00 | NOAA-21 | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b2f08478-1bd0-3db7-9a45-b581ee1a3a45 | -9.85105 | -37.12528 | 2025-01-04 03:44:00 | NOAA-21 | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 6b114a65-2247-35f9-b0e0-0069c73546c2 | -12.56056 | -39.62672 | 2025-01-04 03:44:00 | NOAA-21 | RAFAEL JAMBEIRO | BAHIA | Brasil | 2925956 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 41ed6105-7db4-3818-a284-7526c248e0bc | -7.69215 | -41.66481 | 2025-01-04 03:44:00 | NOAA-21 | ISAÍAS COELHO | PIAUÍ | Brasil | 2204907 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7591d92a-f15d-347d-950c-dbf5521749a1 | -6.98406 | -40.01684 | 2025-01-04 03:44:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 9352b25e-a292-3d35-8a9a-b8343cd6cda6 | -10.54494 | -44.67996 | 2025-01-04 03:44:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4182610e-9448-347d-8855-529f1c190273 | -9.90467 | -38.10722 | 2025-01-04 03:44:00 | NOAA-21 | PEDRO ALEXANDRE | BAHIA | Brasil | 2924207 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 79c06fd7-b88d-3918-81f2-7015890fd981 | -10.60795 | -44.34103 | 2025-01-04 03:44:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 892f0f5c-692e-31ed-bef7-602c0477ad7d | -7.64749 | -35.18909 | 2025-01-04 03:44:00 | NOAA-21 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9f289545-5f2f-373d-ac26-606e399aad31 | -8.98243 | -35.61692 | 2025-01-04 03:44:00 | NOAA-21 | NOVO LINO | ALAGOAS | Brasil | 2705606 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 0fb7018e-2283-3e75-b5f9-df93b645bdec | -10.61239 | -44.33272 | 2025-01-04 03:44:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| fb22cc42-fe79-325f-9293-98f3accebaec | -12.10729 | -44.75476 | 2025-01-04 03:44:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 40036034-9791-317b-a451-cc259790d8cf | -10.13634 | -36.39698 | 2025-01-04 03:44:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a3c45874-fe6e-3f99-bbe5-a055f9d6b4aa | -9.86222 | -37.09797 | 2025-01-04 03:44:00 | NOAA-21 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1b18e3aa-d345-368f-9fbe-e03331b9ce1b | -11.72312 | -37.94889 | 2025-01-04 03:44:00 | NOAA-21 | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2756f406-bbb5-3e28-a246-27ff44026c06 | -15.64747 | -39.18952 | 2025-01-04 03:46:00 | NOAA-21 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fbbd3023-f290-3974-adc2-2c272049ff0d | -15.64668 | -39.18982 | 2025-01-04 03:46:00 | NOAA-21 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0f4e0ab1-5cab-3b39-b6b2-1968645e669a | -14.93253 | -40.34211 | 2025-01-04 03:46:00 | NOAA-21 | CAATIBA | BAHIA | Brasil | 2904803 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| abff255e-a3d9-3477-bfd9-a64dc7e615e0 | -25.19657 | -49.3239 | 2025-01-04 03:49:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 206a2f6d-7893-3335-b093-3b7904a6e42e | -22.78719 | -43.75683 | 2025-01-04 03:49:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 87397241-0a17-3195-8c24-ca2f93ee1259 | -22.67521 | -42.85724 | 2025-01-04 03:49:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 7762f880-356a-3b52-8989-42e9a318477e | -25.19078 | -49.32588 | 2025-01-04 03:49:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f2b78ba2-2761-3145-90a4-d0459c23406b | -22.67605 | -42.85263 | 2025-01-04 03:49:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 047211c9-8e70-394d-a380-8bbae87966e8 | -23.40759 | -46.55759 | 2025-01-04 03:49:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| add6bf9f-71d7-3afb-8a27-e3285ae53478 | -10.6124 | -44.3517 | 2025-01-04 03:50:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 4a647831-3afc-3865-8222-7751ddfac051 | -10.6128 | -44.3284 | 2025-01-04 03:50:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 8ee5677f-55ed-34a3-b5cc-23925c0091fd | -27.62846 | -50.20997 | 2025-01-04 03:51:00 | NOAA-21 | CORREIA PINTO | SANTA CATARINA | Brasil | 4204558 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5fe1e8fb-8e9c-3bfe-b271-2130cd7c313f | -27.6257 | -50.20945 | 2025-01-04 03:51:00 | NOAA-21 | CORREIA PINTO | SANTA CATARINA | Brasil | 4204558 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 404cb92f-d33b-3b0e-a278-4a9705888d46 | -27.62724 | -50.20285 | 2025-01-04 03:51:00 | NOAA-21 | CORREIA PINTO | SANTA CATARINA | Brasil | 4204558 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7947e134-a05d-3f97-8dc9-d74322db8cfa | -30.72785 | -53.33572 | 2025-01-04 03:51:00 | NOAA-21 | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| d67a3f6d-b48a-3780-88f4-72389cdc4b72 | -30.72919 | -53.33663 | 2025-01-04 03:51:00 | NOAA-21 | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 154e61ce-3691-3d43-a66b-bf80224a9168 | -10.6128 | -44.3284 | 2025-01-04 04:00:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 159.3 |
| 9f07fb94-b942-3843-abc5-1b48a34965c8 | -10.6124 | -44.3517 | 2025-01-04 04:00:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 105.1 |
| be8e47d4-ddb5-3b32-a0c5-3b66b595d2ff | -2.88976 | -41.63744 | 2025-01-04 04:06:00 | NPP-375D | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 62f11ef0-0237-394f-b858-0db088fe9e6e | -3.54151 | -41.96939 | 2025-01-04 04:06:00 | NPP-375D | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8ed8f431-2475-32af-8fcb-65b6dbeaadb0 | -3.27409 | -43.51794 | 2025-01-04 04:06:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| edcd04d1-6f27-363f-9ea7-033820eada1f | -3.27056 | -43.51739 | 2025-01-04 04:06:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ab4c00c-e6bd-3755-9503-642605a98b29 | -2.96205 | -40.21792 | 2025-01-04 04:06:00 | NPP-375D | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 559e622d-021f-3ae0-b3b8-d6e432abb01f | -2.44718 | -49.02518 | 2025-01-04 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3023e103-33eb-33e1-89eb-98ac31ee73ea | -2.45174 | -49.02889 | 2025-01-04 04:06:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9cc4d3a4-fc7b-3057-94cc-1a9874ae9d41 | -3.13711 | -40.0449 | 2025-01-04 04:06:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| bf48e88b-a804-3c40-8284-f515b0789445 | -3.00329 | -39.93391 | 2025-01-04 04:06:00 | NPP-375D | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |


[Clique aqui para ver as próximas entradas](README5.md)
