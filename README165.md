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

## Dados Diários - Página 165

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b6afd341-2905-302e-ae64-03e6039dbe3a | -12.2876 | -49.2101 | 2025-10-05 14:20:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 1886d94a-e402-336e-8dcf-9cb16e29b7a3 | -12.5294 | -54.7531 | 2025-10-05 14:20:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 9aa8f968-62d6-3cb7-a9c8-3a8ef5c8e01e | -6.4076 | -43.6099 | 2025-10-05 14:20:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 149.3 |
| 34c22e4f-2129-3c03-886d-1fbe8cd6c74d | -10.1497 | -45.9709 | 2025-10-05 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 013c0088-e116-3047-8b21-ddfcd4c135bf | -6.3341 | -41.6309 | 2025-10-05 14:20:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 113.4 |
| 107a2532-25d0-3619-9ee4-6f96be8a80e4 | -16.077 | -51.0859 | 2025-10-05 14:20:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 261.5 |
| 533ac502-249a-3177-bb86-6f9e77a39233 | -13.8258 | -51.2138 | 2025-10-05 14:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 79bfc5f8-0519-3502-b348-dfc733637af4 | -5.9879 | -44.3598 | 2025-10-05 14:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| f743c9f0-9aba-3670-9b44-0689a1ff109d | -6.0618 | -42.5133 | 2025-10-05 14:20:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 80.6 |
| 86f6ba66-1d79-3156-a471-3b21e7030b65 | -8.6722 | -47.6924 | 2025-10-05 14:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 52.6 |
| d04d9825-8e9a-3499-8b66-8d240540d4b8 | -6.7866 | -41.5882 | 2025-10-05 14:20:00 | GOES-19 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 97.6 |
| bafada56-cf1e-34f2-b6a1-3c7f7a92191f | -7.7123 | -46.2307 | 2025-10-05 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 8f9aa8e5-09b4-3606-8ae3-40a2f69d2cef | -7.0367 | -42.8036 | 2025-10-05 14:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 151.2 |
| e247d23e-0efa-3d8c-8e0f-2a1b13c022a1 | -9.9212 | -50.1895 | 2025-10-05 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 102.8 |
| a862a17a-c0fe-3267-8c5d-e0b4de4e5881 | -5.989 | -44.2449 | 2025-10-05 14:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 0d21dd25-75a5-33a6-9245-d675cd2c1be0 | -11.8033 | -45.0856 | 2025-10-05 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 169.9 |
| 8dc57251-a2e4-3a0f-8e9e-027ec6642469 | -9.9207 | -50.2323 | 2025-10-05 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 144.6 |
| d4e12644-4091-3984-9383-f11deff67962 | -17.8808 | -57.6412 | 2025-10-05 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 47.2 |
| 3e3b5ca5-f858-3157-a3d8-669e9b18a3ac | -9.9021 | -50.2128 | 2025-10-05 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 3771a3f9-15e6-39ef-b2b6-2472e2bf8714 | -16.0966 | -51.0829 | 2025-10-05 14:20:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 353.1 |
| 0578fbb5-3d67-3082-bd8e-6bda132a5790 | -16.0212 | -50.9425 | 2025-10-05 14:20:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 27a8fbff-502c-3ea0-8618-dd97dae5eb5d | -6.1538 | -44.6446 | 2025-10-05 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 183.0 |
| 13056d28-2c66-3081-8a72-d1b91412eff1 | -11.8777 | -56.8769 | 2025-10-05 14:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 05aa6d47-8bcd-3113-a45b-f0ce176dfdaf | -8.1699 | -44.1608 | 2025-10-05 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 136.8 |
| ba1378db-560b-38ec-9170-b94d18b0af7e | -15.621 | -52.5075 | 2025-10-05 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 2773b3bb-82b3-34b9-8e3f-f8e69f43e7bf | -6.6069 | -44.3098 | 2025-10-05 14:20:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 7f2ee778-7ef3-3458-89b6-a17c6fab468a | -6.2515 | -44.2242 | 2025-10-05 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 77b82820-65c1-33c7-a741-36eaf5bf56c4 | -5.8576 | -44.2778 | 2025-10-05 14:20:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 76f7203e-3534-348f-84c1-5f8f8b5a66bc | -7.4276 | -46.5239 | 2025-10-05 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 86.0 |
| d16dc780-fa7b-3bbf-8872-365e50d56af7 | -6.7052 | -43.8859 | 2025-10-05 14:20:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 1f885d82-c228-31b4-8eef-b143e8d9e667 | -3.5496 | -39.811 | 2025-10-05 14:20:00 | GOES-19 | MIRAÍMA | CEARÁ | Brasil | 2308377 | 23 | 33 | nan | nan | nan | Caatinga | 108.8 |
| 4fc8306d-3436-3a9f-b0f1-17f98b09c60b | -11.823 | -45.0596 | 2025-10-05 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 171.1 |
| 5b2a6ff3-886f-3bf3-a828-c269327de9e6 | -18.2569 | -53.3329 | 2025-10-05 14:20:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 3276a439-9c11-3368-912a-6fd5aecde763 | -14.1611 | -53.0377 | 2025-10-05 14:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 103.3 |
| c1681b68-49db-3246-bf9c-78c390a31ef4 | -9.3894 | -47.5762 | 2025-10-05 14:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 62.1 |
| b73091ef-bd45-3e19-802c-5f2114a1b4aa | -9.2976 | -45.98 | 2025-10-05 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 845db872-a9b7-3239-aeb7-5d67a2c0ce19 | -9.2973 | -46.0026 | 2025-10-05 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 42bdbb62-5db4-3fde-82ef-9df5fa6d9197 | -17.9605 | -57.5904 | 2025-10-05 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 156.2 |
| c850b94c-7d9b-3e35-b36a-3e0c6598c466 | -15.6019 | -52.4888 | 2025-10-05 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 937969c6-f377-3eb3-a9c9-facae0035327 | -6.7048 | -42.1712 | 2025-10-05 14:20:00 | GOES-19 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 68.7 |
| 227ccc73-bf2f-37be-8979-ed6ec247d0ba | -16.0234 | -50.8334 | 2025-10-05 14:20:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 515fe9aa-a68c-3ad6-98f0-4cb279b89033 | -9.2627 | -51.8117 | 2025-10-05 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 94.0 |
| caea8a3b-53af-399d-8722-1b7f86ab7363 | -5.9226 | -43.3236 | 2025-10-05 14:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 83.5 |
| e5626f8c-9b7e-3ec1-9055-3ee97b8773fd | -6.2153 | -44.0889 | 2025-10-05 14:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 98.1 |
| ff718a38-c8d8-37d0-bd33-8fbc2f38eca4 | -11.5301 | -47.6798 | 2025-10-05 14:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 23627474-93b3-3837-a35a-a73baa003567 | -6.6416 | -42.7934 | 2025-10-05 14:20:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 83.3 |
| 973b32d3-dd0d-3d33-85da-1cc1626f2985 | -8.8618 | -46.0949 | 2025-10-05 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 797792b8-1b68-31cd-8b12-420d7c52f568 | -5.9772 | -43.5057 | 2025-10-05 14:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 90.9 |
| bd6f2977-abe7-3b8e-9d82-766babb69d38 | -11.4535 | -51.5177 | 2025-10-05 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 83.7 |
| badb7965-e921-3076-a9e6-f38440aa60e1 | -16.023 | -50.8553 | 2025-10-05 14:20:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 90686c62-0e99-3c42-bfec-0e64879703c0 | -8.1891 | -44.1357 | 2025-10-05 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 138.0 |
| 3d28d413-e485-32c6-8a16-ced58ef446c1 | -12.4105 | -51.0917 | 2025-10-05 14:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 90c740d4-8fc0-3660-bad4-257a11751380 | -12.4673 | -45.4925 | 2025-10-05 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 125.0 |
| b8e71a7b-b663-3834-a90b-61a6da12b023 | -10.4054 | -45.3931 | 2025-10-05 14:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 13ae4976-3154-30c6-9958-0d237df50195 | -7.7308 | -46.2513 | 2025-10-05 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 147.0 |
| 4c0395ab-bb6e-3b91-bf0d-0674fd354a47 | -21.6888 | -50.0559 | 2025-10-05 14:20:00 | GOES-19 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 135.1 |
| 93bbd9e4-b2dc-348f-9706-48d1fd5600a9 | -5.9229 | -43.3003 | 2025-10-05 14:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 88f9120d-f0f6-32fb-b63f-185edb4ead41 | -5.8925 | -42.551 | 2025-10-05 14:20:00 | GOES-19 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 89.7 |
| 5ee10991-5941-3992-92db-c87a1dfe8074 | -7.7749 | -42.5628 | 2025-10-05 14:20:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 107.6 |
| 3f27b48b-87ed-32b6-aa1b-dd4f18e0a13e | -12.3914 | -51.094 | 2025-10-05 14:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 30be92c7-e57a-31db-93ab-b0fed5b4b7b0 | -12.5297 | -54.7326 | 2025-10-05 14:20:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 89.7 |
| ad4de373-8d2a-31ce-a393-5114a0d6deac | -7.4464 | -46.5223 | 2025-10-05 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 03d71611-017a-376f-87a3-c28f65b95e5d | -8.6908 | -47.7126 | 2025-10-05 14:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 51.7 |
| f82511f2-608a-3021-8438-87262de09344 | -12.0895 | -45.1583 | 2025-10-05 14:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 142.0 |
| ab7840e0-4262-33f5-81a9-458ae4c6d363 | -7.4279 | -46.5016 | 2025-10-05 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| cc459125-9681-3c51-9cc3-bf681611770c | -5.9584 | -43.5072 | 2025-10-05 14:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 144.4 |
| 1295cec2-2ceb-3e39-bf14-e46badd3c93f | -11.8225 | -45.0827 | 2025-10-05 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 214.7 |
| ba99637f-6055-30a7-95fd-472c400e53c6 | -10.3907 | -50.3557 | 2025-10-05 14:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 141.7 |
| 47b5a4bb-7c37-3a51-8df6-ea0987b30dee | -11.6849 | -45.2872 | 2025-10-05 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 146.2 |
| 5c71f567-5dda-3dcb-903e-6e70c990b0c0 | -10.3864 | -45.3955 | 2025-10-05 14:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 73.0 |
| abfe6495-d9be-342a-8d4c-d2fdc84f6ad2 | -17.921 | -57.5952 | 2025-10-05 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.7 |
| cd8ad6f4-265a-3971-a04d-7ca50f982dae | -10.0315 | -50.4131 | 2025-10-05 14:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 6324d19e-8ac8-384d-ad2c-90fbc3d78e32 | -9.3276 | -54.5215 | 2025-10-05 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 8fb5b26e-836c-33cf-9278-249b0896d8ea | -16.0805 | -50.9116 | 2025-10-05 14:20:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 502dc75f-7360-3894-a786-ba3c3a4c1318 | -12.4669 | -45.5155 | 2025-10-05 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 141.7 |
| 64120b35-1449-3231-b720-7aa2012a61df | -8.6139 | -54.9558 | 2025-10-05 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 76e4a578-53d0-332b-a768-b31fead36434 | -9.425 | -49.2084 | 2025-10-05 14:20:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 45349b55-ccb1-3b1f-a880-d2024a844a2e | -9.5791 | -46.1286 | 2025-10-05 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 116.3 |
| a67d0893-8727-3ce0-b70a-5af78de20cbd | -7.7118 | -46.2754 | 2025-10-05 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 108.7 |
| ed4ecb42-dedd-3438-bc1d-29d2cfdea79c | -10.069 | -50.4307 | 2025-10-05 14:20:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 159.5 |
| ae0dfd4d-b083-3bc9-930a-5f39d24d22e1 | -8.8804 | -46.1155 | 2025-10-05 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 452b3455-60f4-39e6-855b-1fdc1c31c758 | -7.7933 | -44.1304 | 2025-10-05 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 107.8 |
| dfbea01a-ad3a-3500-89f9-be86bf51a973 | -8.6138 | -54.976 | 2025-10-05 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| d7175f07-649c-3da7-90a2-21b36789356b | -6.0616 | -42.537 | 2025-10-05 14:20:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 93.4 |
| 600dce09-1a46-39b7-9b5a-d8b07b613521 | -8.5407 | -47.6831 | 2025-10-05 14:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 33a96d2e-6a2a-3738-9a3d-518b5c7bae68 | -18.1769 | -53.3669 | 2025-10-05 14:20:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 1a8ee28c-4400-3eed-bb5e-49f6ee738f7b | -11.8779 | -56.8569 | 2025-10-05 14:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 476d4233-2325-3fe9-bcdb-57c70d3491b2 | -17.9661 | -51.1474 | 2025-10-05 14:20:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 133.1 |
| 099bd228-e523-3343-a6bd-294e87fd72d9 | -6.7167 | -42.8101 | 2025-10-05 14:20:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 82.8 |
| bed55915-53a2-314a-aa7c-24f5eea1fca2 | -11.0911 | -47.7573 | 2025-10-05 14:20:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 0135af82-7a09-3637-8341-143255d6a84c | -9.9313 | -50.8898 | 2025-10-05 14:20:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 109.2 |
| e148bb88-ec55-3dd4-9867-9a88d39bf587 | -7.6463 | -45.4262 | 2025-10-05 14:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 400dfcbb-5e8a-3858-9365-0af7c9f11431 | -15.9084 | -48.8254 | 2025-10-05 14:20:00 | GOES-19 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 015cfebb-28d6-3eb3-984d-b4f261c59c71 | -5.8764 | -44.2764 | 2025-10-05 14:20:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 452fb7b9-910c-346a-9697-198c82eba514 | -7.6993 | -42.5708 | 2025-10-05 14:20:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 100.5 |
| a213c1ec-0aa4-3f3e-9213-04df5f7e54b5 | -9.2439 | -51.8133 | 2025-10-05 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 88.9 |
| fb2cffac-c658-3987-839f-594ae4baf289 | -6.0428 | -42.5386 | 2025-10-05 14:20:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 82.9 |
| dc91ca5a-43e8-379f-b3aa-839b41d35c0a | -5.265 | -39.2697 | 2025-10-05 14:20:00 | GOES-19 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 118.7 |
| caf89a1e-5233-30ed-b467-e86960065b3a | -5.7917 | -43.2872 | 2025-10-05 14:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| ca6f360c-294c-3bed-b5e7-cfc36c2ac32a | -11.5094 | -54.4619 | 2025-10-05 14:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |


[Clique aqui para ver as próximas entradas](README166.md)
