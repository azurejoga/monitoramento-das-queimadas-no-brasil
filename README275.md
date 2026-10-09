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

## Dados Diários - Página 275

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 25623e50-4fd4-362f-8ba1-ecf219b062b9 | -9.18867 | -43.37985 | 2026-10-09 16:01:00 | NPP-375 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 18.5 |
| 94dae5fc-b82e-3b2d-be15-b1f48b413474 | -10.28923 | -46.6056 | 2026-10-09 16:01:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 4adbfdee-57f9-373f-9528-382568fb216d | -9.02695 | -44.36148 | 2026-10-09 16:01:00 | NPP-375 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 2562d733-4717-3c0b-99c8-59453f5e1ad9 | -10.53642 | -47.31369 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 0f6f61f5-30e6-3953-80cd-e71eebb91893 | -10.48298 | -47.31504 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3c2f52f9-5b59-3448-a05d-0e9137443ede | -4.99428 | -43.15992 | 2026-10-09 16:01:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| cb10731b-9faa-3677-b7c4-f3fdfb8c83a0 | -6.84132 | -41.74587 | 2026-10-09 16:01:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 53e30154-d2d6-3557-a0f7-aa90bb02d991 | -9.54929 | -46.84518 | 2026-10-09 16:01:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 6b719439-0187-3cad-97ba-ef898e8dde87 | -7.48839 | -42.8135 | 2026-10-09 16:01:00 | NPP-375 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 03dfbb3b-585d-3114-a3cc-d05718a5916a | -5.95872 | -40.92235 | 2026-10-09 16:01:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 21.1 |
| f0794067-8ea9-355b-acb2-5b46e87b2377 | -5.69984 | -41.74546 | 2026-10-09 16:01:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 1773d7af-9e14-3a0d-bda2-43bae1fff3ba | -11.04948 | -44.0238 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 89.2 |
| eb556f20-9e46-3aed-af2a-b978e8615ebd | -11.23374 | -46.31158 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 41.4 |
| dc8d5b1e-7af9-38ba-b722-e5b919174090 | -11.05585 | -44.02734 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 89.2 |
| a8e535c8-bfd6-3847-826c-29f3e20b9674 | -10.82585 | -47.3244 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 31.3 |
| beacab0f-a00b-3a6a-81b5-255888764238 | -6.88393 | -43.69275 | 2026-10-09 16:01:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7be2270d-5d52-3f2d-a95f-4a3bb19c32cf | -9.74566 | -45.68441 | 2026-10-09 16:01:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 38cab68b-28bc-30b5-b2bb-7ce5a8aa8d2b | -5.95114 | -40.93203 | 2026-10-09 16:01:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 75.3 |
| 7a12594e-705c-3b90-8b5a-73bb05aa49a8 | -9.74773 | -45.69141 | 2026-10-09 16:01:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 34.6 |
| 794a6e98-a993-3032-ac33-62faa55d06b6 | -5.87994 | -43.41542 | 2026-10-09 16:01:00 | NPP-375 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8b054569-1403-37ea-94f9-6c96af8ef184 | -7.48651 | -42.8383 | 2026-10-09 16:01:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 30aeda25-c036-3a54-9192-b1e81e366e1f | -11.04515 | -44.03714 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 277.1 |
| 0916764c-8597-316c-9cfe-f64a3bb7c18a | -10.31242 | -46.28273 | 2026-10-09 16:01:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 250ef89c-e8b9-3692-939d-ad9c552fdccd | -7.41184 | -44.75713 | 2026-10-09 16:01:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| b5bc16bd-31cd-3f08-85fe-bbdd6eabb046 | -6.94294 | -43.67012 | 2026-10-09 16:01:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| a5000409-678e-3bae-b539-f57726a2cf1c | -7.1599 | -44.49931 | 2026-10-09 16:01:00 | NPP-375 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d544a333-069c-32f2-b9b2-dca051363c1e | -8.89932 | -45.24441 | 2026-10-09 16:01:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 2e712d65-a93e-3a6f-959a-d893bebd1296 | -7.08111 | -43.4977 | 2026-10-09 16:01:00 | NPP-375 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d1c5c0d3-f194-308a-81ad-d660e295a1de | -5.66244 | -42.99373 | 2026-10-09 16:01:00 | NPP-375 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 60bbbaa3-ca7b-3ebd-a01d-8119a79acbd9 | -7.49229 | -42.80372 | 2026-10-09 16:01:00 | NPP-375 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| bede451f-03cc-349e-943f-37b8d6be5c51 | -8.18616 | -44.42008 | 2026-10-09 16:01:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 76934925-515f-3b0e-919f-64608165f2b6 | -11.11958 | -44.02048 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 95534f57-edcd-38fd-8a2d-de48f4b5c2b6 | -10.87368 | -45.52858 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 1ffd98df-a1af-3e10-917b-8b68c7812382 | -5.67797 | -46.36465 | 2026-10-09 16:01:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2e88d24d-5d8b-37f6-99fb-7a37c59cc3ec | -11.09305 | -44.03996 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 3e7783e4-4ee0-3eac-92e7-2dc41445014a | -10.87247 | -45.53196 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 7dfcb42b-5ebb-348b-b023-aa0c8d39ef14 | -11.23326 | -45.29874 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 0498519b-bf89-3dd3-a821-1b2837c6f944 | -7.60132 | -42.37212 | 2026-10-09 16:01:00 | NPP-375 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 4046a274-b2ea-364e-92d3-8a4ef7caa4fd | -5.46302 | -42.36403 | 2026-10-09 16:01:00 | NPP-375 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 0660e6fd-f497-3157-a1ba-a443616fb9b2 | -10.85233 | -45.56977 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| a3e21e28-fb0b-363e-8ac7-32864060cf17 | -6.91738 | -43.93666 | 2026-10-09 16:01:00 | NPP-375 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 71ea3374-73ec-3575-98b5-1805cf593b61 | -6.80708 | -45.20296 | 2026-10-09 16:01:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 298d4f8b-4f2c-3978-b245-7c9c24468f92 | -5.99088 | -41.37233 | 2026-10-09 16:01:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 30.3 |
| 4a6b9dd9-0343-35e0-8bfe-8c292594a889 | -5.50845 | -42.83659 | 2026-10-09 16:01:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 420666fe-67b4-3570-989f-a51403e9256e | -5.11342 | -42.85265 | 2026-10-09 16:01:00 | NPP-375 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b06f0fb9-c4a0-3b72-b831-01fa241c3864 | -10.97874 | -45.19872 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| aa26ef5e-4741-39b4-876b-0d74615ffe63 | -6.75308 | -43.71837 | 2026-10-09 16:01:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5c8a797e-2461-3b45-8b89-668fdefd3f04 | -9.93237 | -43.55922 | 2026-10-09 16:01:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 9c65e881-93f4-3689-a094-4332f81c602b | -7.02206 | -45.31329 | 2026-10-09 16:01:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a2a2d4cc-617e-3a67-b686-bc34d5739f0f | -11.25405 | -45.17609 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 19.5 |
| ffe60087-e845-3c7a-a5b8-915af1f56758 | -10.22474 | -46.82893 | 2026-10-09 16:01:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 97505dfb-e149-3a11-bbc7-2c9d1f7bc41e | -10.88791 | -45.53917 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 796c77a3-a3f2-3563-9e24-0eb1868de7f2 | -10.4318 | -47.30745 | 2026-10-09 16:01:00 | NPP-375 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 075aad45-ee1c-389b-aca5-ad20e8db480f | -10.85821 | -45.56416 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.1 |
| f9857285-8f2a-3242-8835-cf40d050d0d7 | -11.0735 | -44.12366 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 0f3f6c94-76b1-31e7-9893-5706b3a7030e | -6.22912 | -42.6781 | 2026-10-09 16:01:00 | NPP-375 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 16c3201a-84cd-306c-9eec-683048a0be6f | -9.18454 | -43.39075 | 2026-10-09 16:01:00 | NPP-375 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 26.5 |
| 705a98a4-5ec6-3b3c-813e-2f22b2f28a5f | -10.46864 | -47.25212 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 28.1 |
| de92a25b-3eb3-31b6-a00b-cbfa83911ee0 | -10.86163 | -45.54992 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| dfd2df2b-17e3-3b79-8286-a2129bebcdbf | -7.90495 | -44.16618 | 2026-10-09 16:01:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| f2332564-d765-39d4-91c5-b8d0fa6acf92 | -6.80083 | -39.33477 | 2026-10-09 16:01:00 | NPP-375 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 45a77ad7-5490-3277-bece-40c08d39ae38 | -8.29328 | -45.70913 | 2026-10-09 16:01:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 419ee6f1-b782-393e-b37a-6261e6b40350 | -7.10471 | -41.74897 | 2026-10-09 16:01:00 | NPP-375 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 27189d9f-415f-36a3-b880-c31c7c541d0b | -7.79371 | -44.56886 | 2026-10-09 16:01:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 78a17bdd-4db9-398d-b107-d49cd4d0e18a | -7.11672 | -42.54584 | 2026-10-09 16:01:00 | NPP-375 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 7efdd69e-c68b-3b96-b589-830c8ff25103 | -6.48795 | -41.82762 | 2026-10-09 16:01:00 | NPP-375 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 5c69211b-7e06-314c-9054-bcb90767318e | -7.5125 | -45.29339 | 2026-10-09 16:01:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 427b1751-cf37-3c48-b5c6-7e05c5c81327 | -8.93021 | -45.1418 | 2026-10-09 16:01:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 00a36e98-fa90-3eeb-94b5-fac688889259 | -6.35082 | -44.05609 | 2026-10-09 16:01:00 | NPP-375 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| aac54b6b-eaf6-3d7c-8652-27519fff4c44 | -10.91462 | -45.38019 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 0b5bc219-9275-3d4e-9da8-b94148266798 | -7.24362 | -39.25 | 2026-10-09 16:01:00 | NPP-375 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 53.3 |
| a5010020-080a-3fd2-8422-b7a96e432b0d | -9.87589 | -47.48777 | 2026-10-09 16:01:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 219f4d12-d71b-3f39-917e-3300e02e93e7 | -10.49555 | -47.23682 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 155.3 |
| 57d374a4-97e9-3556-a74a-4efa73b9105a | -10.46789 | -47.24548 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 23.9 |
| f49ec6c5-e610-395b-b4a3-a28aeb51fd5d | -8.25935 | -44.20415 | 2026-10-09 16:01:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 52a11af0-91cf-3371-88dc-ec9a7d7cdd37 | -8.90103 | -45.40626 | 2026-10-09 16:01:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4d52a6c7-b049-325f-a506-26f18a3370ad | -7.49066 | -42.79172 | 2026-10-09 16:01:00 | NPP-375 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 560e09b4-390a-3754-ba2a-35d8af062737 | -10.86465 | -45.5635 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9bf8592e-47be-3676-b56e-4665a5c97507 | -11.06453 | -44.09893 | 2026-10-09 16:01:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 26.0 |
| fd79a372-6c51-3af1-8aad-a199c8eb64ba | -6.06088 | -42.59986 | 2026-10-09 16:01:00 | NPP-375 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| c6803af5-cb4b-33de-8055-8bc8e92b125e | -11.25045 | -45.17448 | 2026-10-09 16:01:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 23a46c00-efa3-3e03-b708-e84fe5934d46 | -7.41769 | -44.75645 | 2026-10-09 16:01:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 8f107e1e-7ec5-3b60-9853-fcb750242208 | -6.05515 | -42.59495 | 2026-10-09 16:01:00 | NPP-375 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| b553e2c8-7f85-3e42-bce1-093f10b343c4 | -5.48555 | -43.03542 | 2026-10-09 16:01:00 | NPP-375 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9d1d0d89-18f4-321b-9677-1b8e1b86fbe4 | -9.04165 | -44.38448 | 2026-10-09 16:01:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 16fc4abb-e502-340f-8b6b-2b864cd0ea37 | -5.75727 | -42.09877 | 2026-10-09 16:01:00 | NPP-375 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| ead37c30-9dd7-3da9-9933-62dadf4af0fe | -10.84758 | -47.35651 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| d2d582b7-4880-3449-9d7a-16795d32566d | -5.99824 | -40.94696 | 2026-10-09 16:01:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| ec31165b-87cc-3d8b-a2f8-4e2fdc280558 | -9.15909 | -44.79152 | 2026-10-09 16:01:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 8e37405e-c0f6-3e1c-8d12-05d1873a961d | -7.41717 | -44.75249 | 2026-10-09 16:01:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 4340eb93-3a3d-3125-ad1f-02fedfdec52e | -6.92458 | -43.06399 | 2026-10-09 16:01:00 | NPP-375 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fd0f818c-1606-3fdd-9ba0-b2bde46a6ecf | -7.41822 | -44.76049 | 2026-10-09 16:01:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| df2afff4-3821-33e2-a019-34a2ee878892 | -10.46571 | -47.28957 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c5a96686-e8af-3ecb-aaba-fc79e03ab607 | -5.33849 | -42.92872 | 2026-10-09 16:01:00 | NPP-375 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 9e905be0-2594-3b22-951c-7f7ad56085ca | -7.74362 | -45.4421 | 2026-10-09 16:01:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 16.2 |
| c71fee48-1590-3e2a-b12f-e943156d2171 | -10.49063 | -47.25634 | 2026-10-09 16:01:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 33.9 |
| dbedfd3a-4a74-3010-88b5-334194e124f7 | -5.51917 | -43.05409 | 2026-10-09 16:01:00 | NPP-375 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| f282f8c6-a4db-35ed-9d35-ba3085776030 | -10.42843 | -47.31594 | 2026-10-09 16:01:00 | NPP-375 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 6f465f02-6319-36d3-a5fe-86dbbbce7b53 | -9.93664 | -44.79749 | 2026-10-09 16:01:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 5ba3a200-737f-303f-b2b6-4e8c5d154c4d | -5.67399 | -42.60517 | 2026-10-09 16:01:00 | NPP-375 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 26.4 |


[Clique aqui para ver as próximas entradas](README276.md)
