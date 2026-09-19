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

## Dados Diários - Página 116

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7566fd32-e2bb-397e-9518-bb00363ac2f6 | -6.9224 | -55.0376 | 2026-09-19 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 20c4edb5-dfc1-3f45-94ef-47ce752a3f43 | -6.3319 | -45.6062 | 2026-09-19 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 123.2 |
| a766a776-d57c-34b8-8592-526904d1f31e | -13.2417 | -51.7146 | 2026-09-19 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 82.7 |
| bc63d78f-aa17-3de1-bfbc-ffc03966b015 | -10.8921 | -53.9857 | 2026-09-19 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 02987fa2-6f19-3cef-a5fb-fa15917f5c21 | -10.8367 | -50.9266 | 2026-09-19 14:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 98.0 |
| ec4c95b0-4092-3ebf-b30d-5469ef866e22 | -10.911 | -53.984 | 2026-09-19 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 93.7 |
| bf1fda84-7dcb-32c2-86cf-b9ef95080818 | -12.5952 | -49.1046 | 2026-09-19 14:30:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 134.5 |
| e26c22a0-41dc-3631-80cb-012ff055b76e | -13.3175 | -51.769 | 2026-09-19 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 2d229311-d853-33f5-a480-432e3cb7512c | -9.7137 | -45.9777 | 2026-09-19 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 283d96cd-a3d2-3712-9dd9-156e646bd40a | -10.9301 | -53.9618 | 2026-09-19 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| e02d3fc6-55d4-3feb-9210-ea13a09993cb | -13.2414 | -51.7359 | 2026-09-19 14:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 295.7 |
| 3b24115c-718f-3944-a038-b1b4ceeb57be | -5.6596 | -43.3906 | 2026-09-19 14:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 181.0 |
| 3abbcbab-1b9d-3d26-9641-deefa5b10146 | -11.234 | -48.3571 | 2026-09-19 14:30:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 9e7f42c8-74fd-3e11-8763-a791031cf95b | -2.6966 | -57.5889 | 2026-09-19 14:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| fbf42200-b488-3df6-8b64-6f5fbf8c9a44 | -11.1035 | -49.4623 | 2026-09-19 14:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 131.6 |
| 65f40ef7-39dc-3171-af26-c9469659debd | -6.3132 | -45.6076 | 2026-09-19 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 18e3fe0c-bf0a-3a97-bc4b-4cbd6a74bb96 | -10.567 | -51.3137 | 2026-09-19 14:30:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 6eb27c67-6598-36f8-a876-2cd68b2e39ef | -8.7731 | -48.6868 | 2026-09-19 14:30:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 178.7 |
| dd3c1e20-2052-3a2e-b0c1-632e4008f2b0 | -7.8025 | -44.9337 | 2026-09-19 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 167781c7-117d-3f3d-83f5-8100900e5a14 | -9.6668 | -54.3129 | 2026-09-19 14:30:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 92.3 |
| e0de8e47-c9d8-3f39-99d7-1081310b78f8 | -2.458 | -57.9033 | 2026-09-19 14:30:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| aeb629be-85e3-388b-9a0b-e0bf35d9f842 | -4.5585 | -42.9758 | 2026-09-19 14:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 920b296d-fc6d-30e1-ab6a-3151274de36d | -7.8843 | -47.6333 | 2026-09-19 14:30:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 98.6 |
| e28a85a9-4736-3e07-8fa2-5de44656ddb2 | -9.6013 | -45.9003 | 2026-09-19 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 213371f5-25cb-34ce-852c-0f3373aabe8d | -7.8595 | -44.8824 | 2026-09-19 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 147.2 |
| ad80c5f4-7eeb-3c88-bfe2-7151e02a6853 | -5.2335 | -47.5645 | 2026-09-19 14:40:00 | GOES-19 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 0e14766e-0487-3aab-adbc-3f3a3c18928c | -3.1514 | -58.644 | 2026-09-19 14:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |
| a1e3f7ce-85e8-3802-862a-c49094d7424c | -8.1688 | -54.7432 | 2026-09-19 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| f2f0ecc7-5b93-3ccd-a0a8-7824df82f924 | -8.4314 | -45.8467 | 2026-09-19 14:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 09f7c9f6-8ba2-39dd-8b08-86c90ee41d5b | -9.6205 | -45.8755 | 2026-09-19 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 3d307832-006b-3563-902e-b8492fa6b05e | -1.6396 | -55.1517 | 2026-09-19 14:40:00 | GOES-19 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| f734e81a-03d8-3587-95a3-e2dc9a364625 | -9.0358 | -48.727 | 2026-09-19 14:40:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 116.9 |
| ea533e7f-d811-3ee4-8202-f3670e96c047 | -11.8937 | -47.6099 | 2026-09-19 14:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 102.3 |
| e5331129-da22-39c3-b146-8b9c1ed6c0f6 | -9.0355 | -48.7487 | 2026-09-19 14:40:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 118.3 |
| d17cf619-c4d2-38e1-86fd-e9be640e307d | -3.4455 | -58.1941 | 2026-09-19 14:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| d4b6cdcc-f6b5-36be-bf04-f5db6b01c5ca | -10.0956 | -48.4226 | 2026-09-19 14:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 87.2 |
| f3d3e95d-deac-368e-ad41-b55950080aeb | -13.2414 | -51.7359 | 2026-09-19 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 123.4 |
| eb83d87e-9c3f-3faa-b690-c998743a14f5 | -10.7715 | -46.3001 | 2026-09-19 14:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 57647c3f-3262-38ea-9c57-20c484e422d4 | -12.4841 | -50.0532 | 2026-09-19 14:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 68567e3d-f7fd-3886-a40e-b0cb8761df94 | -4.5587 | -42.9523 | 2026-09-19 14:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 9723f837-9972-3ed0-836f-6a7136d9bc91 | -10.7133 | -50.258 | 2026-09-19 14:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 130.4 |
| 8b96b50b-5768-3705-a9fb-d82bbb26051c | -12.5952 | -49.1046 | 2026-09-19 14:40:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 145.9 |
| 7ba258f3-2f19-3731-8225-9f6ced4e7783 | -8.45 | -45.8674 | 2026-09-19 14:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 119.6 |
| f0ed66e2-7359-3071-816d-b46937e21289 | -11.8546 | -50.0653 | 2026-09-19 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| fe5ec271-e108-37e7-a2d6-eb35415e58b7 | -11.949 | -50.1186 | 2026-09-19 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 145.9 |
| 80bec6c0-d609-3c35-a302-a263e1cc33d7 | -12.5032 | -50.0508 | 2026-09-19 14:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 187.6 |
| 499acf92-14cd-37c3-85c5-cbe0d8206afc | -7.7844 | -44.8669 | 2026-09-19 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 132.0 |
| cdd811b0-496f-3b7f-9257-301e321c19f9 | -11.9303 | -50.0993 | 2026-09-19 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 131.6 |
| 1a3bc547-90b7-32c5-8112-f98445508d48 | -9.8066 | -46.1023 | 2026-09-19 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 9309cf3b-2a63-376b-894f-69cc44a1de74 | -2.8975 | -57.7793 | 2026-09-19 14:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 384bdad6-4082-32c3-9b47-c524d8d47008 | -13.3175 | -51.769 | 2026-09-19 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 75.1 |
| d247f331-a282-3509-84e1-ebf143a61949 | -13.2222 | -51.7382 | 2026-09-19 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 82aa3c01-4df0-3e0b-8212-bfe47c3909f9 | -6.2034 | -45.3453 | 2026-09-19 14:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 708da0f9-59e7-31ee-81a0-f9953ded960c | -7.8598 | -44.8595 | 2026-09-19 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 179.1 |
| 128a5b48-7a92-3e25-8bbc-f4b9fe4b936a | -10.7994 | -50.8881 | 2026-09-19 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 3a9cb72c-7f96-36b1-89c2-3f23e257879a | -13.884 | -47.9929 | 2026-09-19 14:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 0634df10-5627-3064-a53d-0dd45450b3e8 | -7.0029 | -49.7551 | 2026-09-19 14:40:00 | GOES-19 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 504f11d0-5e3f-35da-8ab5-c3cf2bb04840 | -8.4737 | -47.0053 | 2026-09-19 14:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 42915e0b-56f3-3317-9054-d76224912cda | -11.9356 | -49.7535 | 2026-09-19 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 127.0 |
| 3daa57e2-2378-3a59-a0fb-7330c82564d3 | -2.6966 | -57.6084 | 2026-09-19 14:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 886eae22-e2a6-3a16-b853-5e8b023a2adc | -6.2585 | -41.6617 | 2026-09-19 14:40:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 130.1 |
| 183b4d92-ae71-30cb-9bf3-3847bf7ecf6f | -9.6668 | -54.3129 | 2026-09-19 14:40:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 72d2b155-9b22-315c-a399-f43680c3404c | -11.0608 | -49.7909 | 2026-09-19 14:40:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 455b6939-49c8-313d-a247-92ba29dfedb6 | -11.0611 | -49.7693 | 2026-09-19 14:40:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 141.0 |
| eb8d5293-f6e3-3625-a980-e7eb6bb8a915 | -10.913 | -50.8762 | 2026-09-19 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 185.1 |
| 26979220-27cd-346d-b22e-4e902a51ed50 | -8.411 | -54.7274 | 2026-09-19 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 105.3 |
| 2757c7f3-db53-311f-975e-8b5fbd600ec8 | -6.2582 | -41.6858 | 2026-09-19 14:40:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 111.7 |
| 525e2ee9-d962-3463-b577-145b96d87286 | -2.6783 | -57.5893 | 2026-09-19 14:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 0b16fc77-d8e8-3f6c-93e7-9861cfab6577 | -8.4797 | -57.6282 | 2026-09-19 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 70363ad1-4da5-3ded-90a4-f28c7dc0b26b | -11.6798 | -54.446 | 2026-09-19 14:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 04137505-14f3-349c-8bf1-e68c29f73b5a | -2.8974 | -57.7987 | 2026-09-19 14:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 269.3 |
| e152beea-52fc-36c7-8524-706fbebad525 | -11.9487 | -50.1402 | 2026-09-19 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 148.5 |
| 474380e1-180c-3243-bc72-0da08acf6b2a | -7.8843 | -47.6333 | 2026-09-19 14:40:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 9cb226c8-cf6d-3585-913e-75b48b054cae | -3.4462 | -57.9812 | 2026-09-19 14:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| d69bc2cf-4014-3927-a239-e573df77da5e | -5.9465 | -44.7974 | 2026-09-19 14:40:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 1eac7cd2-2e6a-3e32-9a11-364f72ebf78e | -11.299 | -51.7238 | 2026-09-19 14:40:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 80.5 |
| a1584c5f-cb8e-35aa-a479-741190ad6bc6 | -11.8746 | -47.6125 | 2026-09-19 14:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 151.7 |
| 92ee2ff2-f4a1-39dc-b34e-262eefeaf852 | -10.8367 | -50.9266 | 2026-09-19 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 28549e69-d8f3-32c2-927c-9c7dcb10029b | -5.8064 | -43.728 | 2026-09-19 14:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 2da71e42-b694-38ea-87f3-e28c3542ae86 | -12.1723 | -46.968 | 2026-09-19 14:40:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 122fcaa8-f29e-32fb-b09b-585a5301fe1f | -11.874 | -50.0415 | 2026-09-19 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.9 |
| ad067672-3f8e-35e1-a4a3-d5408425a648 | -8.7919 | -48.6851 | 2026-09-19 14:40:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 266.4 |
| 678a9b85-84b5-3601-aa17-544c180a18c1 | -7.7629 | -46.7389 | 2026-09-19 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 142.3 |
| 359cc524-d6b9-3bbb-95b2-53a410a5ac7c | -11.9112 | -50.1016 | 2026-09-19 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 216.3 |
| fd107e60-fd9c-351e-98d6-10a6f9e724bb | -7.5704 | -57.6766 | 2026-09-19 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 105.9 |
| 5dbe8247-5c8a-3500-8d3f-1a1922a9ed3c | -9.0167 | -48.7505 | 2026-09-19 14:40:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 80.1 |
| c57cebc5-78b2-354b-8807-d112fcc82c00 | -9.6202 | -45.8981 | 2026-09-19 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 240.9 |
| aa29c557-e58c-31dc-aff8-192dfe06d0a6 | -11.1035 | -49.4623 | 2026-09-19 14:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 137.4 |
| b34e3902-12d1-3a8f-a9d0-80c31a72e63f | -8.6832 | -45.3221 | 2026-09-19 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 120.9 |
| cfdccc3f-8439-322f-ac54-d725df326452 | -9.2603 | -45.939 | 2026-09-19 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 40bd6d4f-1327-34a9-bb87-f2fdb8912112 | -9.0096 | -44.9209 | 2026-09-19 14:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 5405e72d-1baf-3737-bd8b-831613a754e2 | -8.6173 | -54.5924 | 2026-09-19 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 891342f2-5eb2-35f9-bf6c-14dab369cf1b | -7.7626 | -46.7612 | 2026-09-19 14:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 291.0 |
| 9437c3ea-9fc0-32ef-89e1-a12050e8a9d4 | -3.4272 | -58.1945 | 2026-09-19 14:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 4a00d26f-cba7-31e3-885d-f647f6066627 | -8.9412 | -44.3995 | 2026-09-19 14:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 239.2 |
| a960a4c5-6813-391a-8cd2-088ccc5b5e42 | -10.9133 | -50.8549 | 2026-09-19 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 246.0 |
| a4551d2e-f3e6-3264-991b-d6cf534d2f7e | -10.7466 | -50.5959 | 2026-09-19 14:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 52655cc9-350e-37d3-ac3d-612f2a501133 | -11.0827 | -48.3095 | 2026-09-19 14:40:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 6246efa0-bf0c-3971-a4cb-b50ad2eb771a | -11.6988 | -54.4443 | 2026-09-19 14:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 77.4 |
| ab1a4fc8-fafd-3a4e-9722-73a4d7ba0392 | -2.9795 | -54.7696 | 2026-09-19 14:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |


[Clique aqui para ver as próximas entradas](README117.md)
