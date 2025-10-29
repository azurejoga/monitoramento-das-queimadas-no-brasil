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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7274f7ce-7d5b-36a8-a387-938092b13510 | -9.29036 | -47.0255 | 2025-10-29 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| eb4dc829-427c-3e65-8e3a-37425d20ee6e | -7.99012 | -47.23653 | 2025-10-29 04:23:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 98f5674b-5283-3a96-b98d-7eecd15bb997 | -10.7785 | -44.76221 | 2025-10-29 04:23:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a2d1af35-4d3a-3e75-8172-7d63d8a7859f | -7.49398 | -47.04168 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 464508c4-371d-3266-9b26-bbcdeac71c2c | -8.54983 | -45.70641 | 2025-10-29 04:23:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bf864e3e-b729-33be-927f-e089f04e2aca | -7.32552 | -44.74408 | 2025-10-29 04:23:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fbe270dd-4b4d-3432-a74d-c1fc471bbd30 | -9.5716 | -46.97319 | 2025-10-29 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 64743e2e-016c-3f38-ac09-d213641a4fc4 | -5.59386 | -51.12614 | 2025-10-29 04:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 41f405f6-2260-3caa-86ed-6ac7f5cb26bc | -6.61706 | -44.62456 | 2025-10-29 04:23:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eb0456fd-9c7f-361a-b5df-b1c55327080b | -6.49006 | -42.24361 | 2025-10-29 04:23:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0caf84b9-87af-3d89-8e42-482b111f9af8 | -8.32873 | -45.37469 | 2025-10-29 04:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 65ae5097-440b-353b-bb7a-e5ce10c51f4d | -10.91529 | -48.00427 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8e505588-f6a6-3bca-b113-b9ca152bdd3e | -10.33776 | -47.78072 | 2025-10-29 04:23:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3c6af48c-44a0-3cb7-a656-7497ec80f2e8 | -9.50598 | -46.51722 | 2025-10-29 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 91e2673d-f091-3b0c-9dea-0884a1a0450a | -6.15451 | -41.67483 | 2025-10-29 04:23:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9ddfbfb6-d43e-3be6-a9c9-d3f036908e2b | -7.80838 | -46.42129 | 2025-10-29 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 62c46220-5f13-339f-9bd5-2da8e9011cda | -6.24182 | -42.57272 | 2025-10-29 04:23:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 77f36fdf-c075-30cd-bda8-7bd390b01723 | -10.64744 | -48.00363 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 159e77a9-fcd0-3028-b2b3-7af0fe8c2c9e | -7.347 | -43.91372 | 2025-10-29 04:23:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 82f4962a-e7ac-35c0-9afd-a96e0e808035 | -7.36526 | -47.63318 | 2025-10-29 04:23:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a54d1924-b743-3204-b205-4efc4a7cf1e9 | -10.22087 | -47.55121 | 2025-10-29 04:23:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c1056c4e-3f09-379e-906a-517f9f9b6632 | -10.53742 | -44.59946 | 2025-10-29 04:23:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 381694cc-2e1d-3464-a072-40f1543a3089 | -9.4971 | -46.93517 | 2025-10-29 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 21c69ebf-80e8-3ec0-a47d-86a81913a503 | -7.74467 | -44.72129 | 2025-10-29 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 06a25cec-f49c-34cc-91a0-1ac30941abf7 | -6.30432 | -41.88333 | 2025-10-29 04:23:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 49a54740-72c9-3766-9ec7-233d9eb31a51 | -8.18732 | -44.44707 | 2025-10-29 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8af3e608-9fab-34bb-af08-c4792ce351f6 | -7.34208 | -42.4657 | 2025-10-29 04:23:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2f703032-653e-3ad7-ab9b-edee93f14e57 | -8.02247 | -47.38735 | 2025-10-29 04:23:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5418bd8a-0935-3100-9edb-7f8067eca62c | -5.60611 | -42.78682 | 2025-10-29 04:23:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 069c07d9-96b0-3195-bf0e-9830b645995d | -10.95018 | -47.62315 | 2025-10-29 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1dcdc960-da5c-32de-8a41-bfa48b44989a | -4.93521 | -47.08701 | 2025-10-29 04:23:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c9731895-2517-3769-8db7-bcc5674cec27 | -5.59979 | -44.9612 | 2025-10-29 04:23:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5c01e0fc-5be5-3db5-929b-77ce8dae05a8 | -6.30494 | -41.8793 | 2025-10-29 04:23:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 5f90d338-5615-3838-8f62-dcf7826525c8 | -5.97354 | -46.3194 | 2025-10-29 04:23:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 583153ed-d87a-3938-8dc5-9c09814ddb1c | -7.41633 | -44.65844 | 2025-10-29 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ef86796f-1552-313b-979e-66a22b6ee30e | -6.08497 | -41.76206 | 2025-10-29 04:23:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 262dde0e-821f-3ad0-8344-7f805f99bef4 | -6.10648 | -42.43991 | 2025-10-29 04:23:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 5cb3c134-ed6b-3954-bb36-906a697a3632 | -9.90489 | -44.92599 | 2025-10-29 04:23:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7bc96692-f990-360e-a6c6-805f6ca4bc83 | -10.61813 | -42.30293 | 2025-10-29 04:23:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7ce6d747-d827-3b83-b98d-b40e458ec763 | -7.9301 | -45.51486 | 2025-10-29 04:23:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9186f0b5-142f-3520-a9a9-d9bc33167410 | -6.774 | -45.40513 | 2025-10-29 04:23:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a1472e35-7df0-3a64-9736-2c27235e19b7 | -10.57639 | -49.75872 | 2025-10-29 04:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d70ece77-7b35-3d06-a4a6-9ac9e50e6d66 | -6.98643 | -46.23365 | 2025-10-29 04:23:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d568465-42bd-3f2e-a6c2-033ab9382bc1 | -6.48844 | -42.20758 | 2025-10-29 04:23:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 83decd49-4b81-3ab9-ae97-bd76be817f91 | -7.79296 | -46.45219 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c995aa9-3603-372c-9d9d-81daab8e60f9 | -6.94096 | -47.00781 | 2025-10-29 04:23:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cf648943-2674-3a33-91f5-b444d3c46713 | -7.35819 | -47.63193 | 2025-10-29 04:23:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a7042206-0293-3aae-a010-62f639934223 | -10.6455 | -45.24974 | 2025-10-29 04:23:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d78eaa97-f9c1-381c-b2b0-8b52c5379229 | -9.57995 | -46.63606 | 2025-10-29 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 40040d22-49f0-37f9-802f-240b2dc2b03f | -6.14934 | -41.58272 | 2025-10-29 04:23:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 58d7a40e-0f36-302a-924a-5b7a1df596c7 | -7.78766 | -46.48479 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f42166c5-46e5-33de-9c59-6466db407417 | -7.39192 | -43.64607 | 2025-10-29 04:23:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b9b984de-e9a8-3f2d-b1c6-25302e19c5f5 | -10.63994 | -45.24163 | 2025-10-29 04:23:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1999f30b-d633-3d26-a321-72fbf523c80e | -9.68168 | -48.2312 | 2025-10-29 04:23:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 935f860c-eab9-3943-928a-d20bf65a478e | -7.92901 | -45.50035 | 2025-10-29 04:23:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 341db5c5-fdd9-3a44-82d2-74d582721ad1 | -11.27513 | -45.50547 | 2025-10-29 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d85b10d6-dd73-35a4-85eb-e20fd208dba5 | -6.64083 | -44.60339 | 2025-10-29 04:23:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 656f7d6f-2fee-3323-a5f5-7702ee46dc2d | -6.12304 | -41.70529 | 2025-10-29 04:23:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| fd1f9f93-a04b-337c-a91a-b6c6257d9d23 | -5.68157 | -47.82548 | 2025-10-29 04:23:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b938d7d-789b-3741-9086-836f834ac829 | -7.29819 | -44.98197 | 2025-10-29 04:23:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cad86511-91b3-3de1-ae41-f3b2c363dbcf | -8.51231 | -48.2781 | 2025-10-29 04:23:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a59c082d-ae08-378b-b8d5-4471168b7235 | -7.70278 | -46.90527 | 2025-10-29 04:23:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a4570e17-7f17-3b36-b216-fdcf9831c477 | -7.07763 | -44.94309 | 2025-10-29 04:23:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c10b86ef-e655-3f7d-a747-edf6a35b5b94 | -9.32012 | -46.25331 | 2025-10-29 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7b284856-93d3-3c57-8576-9b4cd69a2614 | -6.42438 | -47.31629 | 2025-10-29 04:23:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d921bdb4-e75b-37de-92df-4a2985df0f92 | -7.52821 | -47.69592 | 2025-10-29 04:23:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1f38c106-e296-3924-9be5-84f3e511d1f9 | -5.6084 | -47.11803 | 2025-10-29 04:23:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3156271f-0731-3836-bc8a-97949219c46a | -6.13317 | -41.71104 | 2025-10-29 04:23:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| a3746f1e-2f51-38e2-8f41-b3d728d322d6 | -7.85861 | -44.23328 | 2025-10-29 04:23:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 36214c21-c898-39db-a82f-bdf8995d9c1c | -5.81289 | -50.0636 | 2025-10-29 04:23:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b066eefb-34fa-38d4-8920-c0fd5c7c406f | -7.50211 | -44.91071 | 2025-10-29 04:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2ddb541a-2865-390b-b918-7a23d37ce376 | -5.16795 | -45.16031 | 2025-10-29 04:23:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e507ec03-b5f9-3f27-8526-21f5f0f4ef70 | -6.11037 | -41.71599 | 2025-10-29 04:23:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4518029c-af40-3b27-8edd-b0ef70867750 | -7.59786 | -43.60044 | 2025-10-29 04:23:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 05bc1b1d-6b7d-321e-9881-f0457b0628e9 | -10.51722 | -47.72704 | 2025-10-29 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4bab397d-41cc-3419-817c-57cbb9ec9dcd | -6.28226 | -42.88145 | 2025-10-29 04:23:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4ae0ded7-ecc1-3765-b1e4-c8104d9c5f03 | -10.57718 | -49.75404 | 2025-10-29 04:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3e1ce5be-303b-36aa-b484-4cbced1426ca | -7.76808 | -42.17697 | 2025-10-29 04:23:00 | NPP-375D | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a468433e-54db-3947-a75d-f41a4d55bcd4 | -9.19052 | -48.30511 | 2025-10-29 04:23:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7cef881d-0988-30ff-80c6-b8f581246649 | -6.2606 | -41.81045 | 2025-10-29 04:23:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8a1b3e8e-3f4a-38b2-96fb-a78d23cfac0c | -10.93972 | -47.62599 | 2025-10-29 04:23:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b4800c79-ec17-3e6d-8ac1-06024148df3e | -5.9627 | -46.32152 | 2025-10-29 04:23:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6579e6d6-2d04-3a1a-af7c-57696f4ce1dd | -6.99411 | -42.78809 | 2025-10-29 04:23:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fb805ffc-bc6c-31a4-84d5-69d01b26c090 | -7.8234 | -40.59133 | 2025-10-29 04:23:00 | NPP-375D | SIMÕES | PIAUÍ | Brasil | 2210706 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 699c835a-ec32-30da-a134-e7162f92557a | -11.18134 | -45.21921 | 2025-10-29 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 39ccb365-3fc6-3316-9f85-640371484a77 | -7.50413 | -46.2728 | 2025-10-29 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d5048da6-ae2d-3784-9f1e-ee4e1527ad8f | -9.44883 | -46.88969 | 2025-10-29 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 692adcdf-fa82-34cd-b841-bd9ee77faf2d | -9.44027 | -46.89949 | 2025-10-29 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c6b9f592-94c9-370a-b0e2-27214128c599 | -6.12039 | -42.44203 | 2025-10-29 04:23:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7c88a995-1780-35fb-bff4-0e7e1ef82159 | -6.2688 | -42.09027 | 2025-10-29 04:23:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5b4e28f4-d7c6-3293-bbd0-8795418ceb78 | -10.38681 | -45.30177 | 2025-10-29 04:23:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 692d8d2d-2678-381a-ab42-3a047246b7a2 | -10.64298 | -47.90033 | 2025-10-29 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2f93760c-14fd-308b-8f62-8f13eeeb7945 | -8.24712 | -46.90688 | 2025-10-29 04:23:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c72a1373-06ef-31ee-85e5-0ed06d9fcad4 | -10.82104 | -48.43821 | 2025-10-29 04:23:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7b156340-da8d-31ad-be6e-9a01a3bf9918 | -6.12387 | -42.44257 | 2025-10-29 04:23:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| bb6313e4-b26e-310f-8fad-83fcb97e54ba | -10.3669 | -47.55968 | 2025-10-29 04:23:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0a979ce6-5cde-30cb-b945-d62325c24f61 | -10.61187 | -49.61669 | 2025-10-29 04:23:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 42f7aa3a-23af-399b-a93e-3c00b1aef235 | -7.80267 | -46.43513 | 2025-10-29 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 124590ac-d0d9-3bc6-b520-99cc5851af3c | -5.19372 | -45.62307 | 2025-10-29 04:23:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d858be17-7642-3464-9007-69f4ca5da832 | -7.411 | -47.1725 | 2025-10-29 04:23:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README32.md)
