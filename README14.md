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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 649803af-165d-3933-9dd0-323441697cfa | -7.7464 | -44.62928 | 2026-06-25 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e67a6899-7e16-3272-a3bc-48b53e6d3778 | -6.99784 | -42.77858 | 2026-06-25 04:49:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9231c424-0f12-3936-a1ad-66e27435e871 | -10.29346 | -44.69351 | 2026-06-25 04:49:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 906e4113-3632-30aa-aa6f-19b79f0e6973 | -8.68392 | -47.86043 | 2026-06-25 04:49:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| e4366964-bcb5-3d93-bdf2-7120609997f7 | -11.53615 | -52.77704 | 2026-06-25 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f3ec3058-c9fd-3c2c-aa0a-cafd13af5dff | -9.18831 | -45.32082 | 2026-06-25 04:49:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 176840c9-2604-3d4d-821b-79cfa4991067 | -13.03371 | -49.93489 | 2026-06-25 04:49:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a262a1a-56ec-3bae-b5de-7d31b327e329 | -11.87345 | -51.75708 | 2026-06-25 04:49:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 652726d2-ab5d-3d5a-ad39-cb11afe91ea8 | -9.1605 | -45.39833 | 2026-06-25 04:49:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 768589af-bf98-3a1b-a2d8-373409c6acc2 | -11.31827 | -51.41693 | 2026-06-25 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 53ab0587-eca8-38bc-8621-c40569a03420 | -12.73601 | -44.46551 | 2026-06-25 04:49:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 43983a48-98a3-37cf-9ac4-21527c857a37 | -6.9944 | -42.89334 | 2026-06-25 04:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 00fb957d-4bcf-300a-bc02-5943a14617e8 | -7.74804 | -44.61807 | 2026-06-25 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 9258588b-3930-3659-8c5c-05bed6d39cdb | -10.39634 | -56.76778 | 2026-06-25 04:49:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ff6e4332-5a2f-3cbc-8f18-fc3e3c84219c | -9.2053 | -45.32307 | 2026-06-25 04:49:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b1bab66-d188-3940-976b-488d69d0e60f | -7.74859 | -44.61429 | 2026-06-25 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d0d948d0-379e-3743-a840-ad4d77050c32 | -11.50727 | -54.49854 | 2026-06-25 04:49:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d33c5e18-b684-3534-a9a2-568f681bc4d0 | -6.75704 | -46.31181 | 2026-06-25 04:49:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 78cf75f1-edaa-3576-9b61-9766d1fd043d | -10.39273 | -56.76283 | 2026-06-25 04:49:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 41d99585-219a-3a2b-a566-d8a64291b9dd | -8.67694 | -47.85937 | 2026-06-25 04:49:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b08bf72a-e42d-3f6e-be1b-42907f62c6b8 | -6.98979 | -42.89275 | 2026-06-25 04:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 099506b9-fa90-3f55-a69d-e42dc9ac4e30 | -8.85428 | -46.93195 | 2026-06-25 04:49:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 22f96830-fffe-353f-acf3-475559f8bc2b | -7.63292 | -50.21554 | 2026-06-25 04:49:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5614c2a4-f5f2-3245-a6e1-705c5e7cd8bd | -11.56082 | -47.61673 | 2026-06-25 04:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c0f0208-aa87-3d68-abd0-e36b5496ff55 | -9.62226 | -49.01484 | 2026-06-25 04:49:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 342f7065-bb10-30f5-b12f-492561dcf2e8 | -10.39818 | -56.76217 | 2026-06-25 04:49:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4eb56aa6-dc6c-35df-8db9-37b115c28768 | -11.91517 | -44.17115 | 2026-06-25 04:49:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1248289a-92a0-3eb8-a1da-9dc20e39da72 | -11.91961 | -46.63332 | 2026-06-25 04:49:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 77089155-28c8-3e73-aed4-7024e906acaf | -11.24782 | -43.32513 | 2026-06-25 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 50c8a1d8-9af2-3a94-95ac-802d228d848a | -11.58666 | -47.44643 | 2026-06-25 04:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35ed914a-5b2f-32aa-a605-0b399a32ff82 | -10.39781 | -56.75934 | 2026-06-25 04:49:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2910c1b9-481b-3882-82b4-f1a976cc0475 | -11.04362 | -47.03619 | 2026-06-25 04:49:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4aedaf00-661a-3519-a40a-9accd3c50ee8 | -12.74665 | -44.46924 | 2026-06-25 04:49:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f976c194-5c8c-390d-9194-921974c1bb9a | -6.99045 | -42.88803 | 2026-06-25 04:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 3b7763a4-a9d6-3fe0-9749-93c42aa8f2a2 | -7.74337 | -44.62113 | 2026-06-25 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a7674aaa-800a-3a7c-9f99-fde020c525d8 | -12.74216 | -44.46861 | 2026-06-25 04:49:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 43867d28-7f25-3d03-9c56-ca0d7380188c | -10.17331 | -51.66193 | 2026-06-25 04:49:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ee74488f-0e62-3d8f-877a-5e4840f472f0 | -11.3778 | -47.82341 | 2026-06-25 04:49:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 096fe208-2a01-3a71-98b5-02bcffb623fc | -8.32789 | -51.34784 | 2026-06-25 04:49:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5935b36c-09c2-3eb5-93ab-757e945c85dd | -9.10785 | -47.4591 | 2026-06-25 04:49:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a0a9affb-6ab1-3a23-9c20-6cc01ceec93b | -10.3923 | -56.76988 | 2026-06-25 04:49:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9cadfdab-3ab2-33be-b03e-76389737a1ea | -10.29828 | -44.69019 | 2026-06-25 04:49:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d15dac03-a281-3854-b2a0-d1cf8c6ea2c3 | -10.39382 | -56.76147 | 2026-06-25 04:49:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0a39399b-cf6e-3f93-885c-873593c9ac65 | -9.2802 | -47.65722 | 2026-06-25 04:49:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b80ec163-a932-3fe7-a0dc-e5b33466b3be | -8.57261 | -46.9028 | 2026-06-25 04:49:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 91b770a0-a571-3d85-bc8f-18d845e87a30 | -8.68043 | -47.85991 | 2026-06-25 04:49:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 082248bb-d498-31ae-9021-dc5a9d9843c7 | -6.98451 | -42.89685 | 2026-06-25 04:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 057fb9da-cf46-37f5-962c-3791860c3e2f | -12.74685 | -44.45315 | 2026-06-25 04:49:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 357ef80c-3fec-38c1-bb64-1e7c0d1aabc2 | -9.36468 | -50.54022 | 2026-06-25 04:49:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f4640dbc-5b69-3635-b467-ddd1435f8903 | -12.38219 | -54.16649 | 2026-06-25 04:49:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57e63748-87fc-3111-a4e0-2793025aee39 | -11.91254 | -46.62756 | 2026-06-25 04:49:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 644eb1ba-2f47-3520-94c5-0178c437c8c6 | -12.83446 | -44.36023 | 2026-06-25 04:49:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 612cc884-27b3-319d-8ee6-dd5d6d1aa20d | -11.56149 | -47.61438 | 2026-06-25 04:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e269574b-0f2d-3245-9fea-d5afe31216ae | -11.32218 | -51.41394 | 2026-06-25 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6a8df917-49ca-3d44-9490-5e1fd6c26315 | -9.98805 | -47.737 | 2026-06-25 04:49:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e6ef006d-376b-3c9e-9de8-d6a48d8da2e7 | -11.50652 | -54.50301 | 2026-06-25 04:49:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71eab079-bdef-3d1f-ae8f-95167cac53f9 | -7.64446 | -45.29558 | 2026-06-25 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0f741d5a-d169-3ac5-a19d-b58113f5da35 | -11.25253 | -43.3261 | 2026-06-25 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 1a1ed706-e7b5-3af4-b73e-d9efb4470c63 | -10.27612 | -47.60633 | 2026-06-25 04:49:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8dcccf12-e6ce-37be-ba4e-bfa8b72a7ffe | -11.58731 | -47.44205 | 2026-06-25 04:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 07d1571f-bc8e-3ed9-b168-be748d39f013 | -7.63347 | -50.21206 | 2026-06-25 04:49:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 59eecd7d-c750-38b7-a704-14672b442b0a | -10.28918 | -44.69291 | 2026-06-25 04:49:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9a02b7fc-3122-39c2-9778-6b1584535325 | -12.74333 | -44.45952 | 2026-06-25 04:49:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 94f8a1d1-e3e2-3b60-9574-f9fa22890ad4 | -12.74841 | -44.4556 | 2026-06-25 04:49:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e46cda59-672d-3c9b-a89a-f9f993e57471 | -7.75575 | -44.6231 | 2026-06-25 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| fc7e6a6e-c7f0-39ef-8cce-c4179f8c437a | -6.31175 | -44.65054 | 2026-06-25 04:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 07411d42-b5ca-3375-8e6f-552b6f38bdcb | -10.42379 | -46.7486 | 2026-06-25 04:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 93a9ca39-a776-3c4d-ad88-4be0e8a4aac0 | -11.87126 | -51.74935 | 2026-06-25 04:49:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c29ca20a-c325-3fdd-984c-45f2ef002713 | -10.39665 | -56.7706 | 2026-06-25 04:49:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9f3002d2-9036-3823-8eea-82c349fe76e6 | -6.98518 | -42.89213 | 2026-06-25 04:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 92ea784f-d524-3237-9627-8c7d7f4c1ac2 | -11.19658 | -48.1221 | 2026-06-25 04:49:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 265037b2-de2f-3881-931c-183bac70248e | -8.55141 | -46.89494 | 2026-06-25 04:49:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 04033c57-3045-3533-902a-ec08d5671443 | -11.78837 | -57.35437 | 2026-06-25 04:49:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aec9197d-02a3-3ce8-9e55-ea591f16d02a | -8.8573 | -46.93681 | 2026-06-25 04:49:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b72ac38a-ddd7-3cc1-95fd-9c4d9359ee1e | -9.27666 | -47.65667 | 2026-06-25 04:49:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7fa10735-7d07-3743-8cdc-ee471bc586f1 | -11.87403 | -51.75349 | 2026-06-25 04:49:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 107.0 |
| 01c667b4-7887-38cb-aaba-e64c29d0d4cd | -9.2048 | -45.32663 | 2026-06-25 04:49:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cda73fb1-036f-3cb5-ac5c-7114e6d1cecf | -12.8396 | -44.35629 | 2026-06-25 04:49:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 928e44b9-0247-3db2-9e4d-034d5def4161 | -8.32681 | -47.12893 | 2026-06-25 04:49:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 530fcdf8-ee09-30a9-bdb3-b643557b25e3 | -10.39894 | -56.75797 | 2026-06-25 04:49:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c112dd8e-d109-34e9-9403-0142a3c43e83 | -6.76505 | -46.30867 | 2026-06-25 04:49:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1434bb8a-d500-390e-9164-9fa12b768e09 | -10.39459 | -56.75727 | 2026-06-25 04:49:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 12a8d015-9fc7-3c92-a43e-4e08fc434494 | -11.8678 | -51.7473 | 2026-06-25 04:50:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 370.1 |
| 1898ae00-86aa-3e09-a6e0-398bbe1911a5 | -11.8675 | -51.7684 | 2026-06-25 04:50:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 170.3 |
| 82d0814e-4f9b-39a6-a649-31646f0976e3 | -11.8868 | -51.7452 | 2026-06-25 04:50:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 236.9 |
| 7027aeb6-1bb5-3de6-932a-3e50bf891f0a | -12.7373 | -44.4521 | 2026-06-25 04:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 4770ded0-6f5d-3e64-919a-e88a4f7cf889 | -11.8865 | -51.7663 | 2026-06-25 04:50:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 1042e880-d372-3a6b-bac3-5b186a835bb7 | -7.7498 | -44.6184 | 2026-06-25 04:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 63.6 |
| db015d0f-4deb-3ba3-8edd-ad085b555b5c | -13.87331 | -50.39857 | 2026-06-25 04:51:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ea6b8ad9-f5e5-3dc8-9d11-429b282cf85e | -11.94217 | -57.71019 | 2026-06-25 04:51:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2870db2-c9f8-3d9a-a6b2-1e357458a46f | -18.45755 | -47.25744 | 2026-06-25 04:51:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7e0d1fa7-0f8f-3b14-bfe5-cbe0ad4f1d03 | -12.22614 | -55.4991 | 2026-06-25 04:51:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 89232735-5feb-3b52-9a2a-f84c0ff4c54b | -13.06856 | -53.35706 | 2026-06-25 04:51:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c8af43ad-f1c7-31ff-9845-9fea9f050044 | -12.22917 | -55.5048 | 2026-06-25 04:51:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3a156415-39cd-319f-8510-4f0eb5f57abb | -13.83828 | -47.03572 | 2026-06-25 04:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 66e75307-45c8-3919-bbe2-90597802e988 | -15.75529 | -43.23346 | 2026-06-25 04:51:00 | NPP-375D | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3e51190c-c92b-3dce-83bb-b247a8eb1cdf | -11.9413 | -57.7075 | 2026-06-25 04:51:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 26c871e0-0a75-33a4-945d-8c9da75687d5 | -12.67006 | -54.57922 | 2026-06-25 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| de367f83-fb8f-3fd3-9936-01b4d9062f30 | -14.8521 | -42.79025 | 2026-06-25 04:51:00 | NPP-375D | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2553e13c-1111-3c27-a002-3b46bf5c0bba | -19.52935 | -42.58881 | 2026-06-25 04:51:00 | NPP-375D | CORONEL FABRICIANO | MINAS GERAIS | Brasil | 3119401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |


[Clique aqui para ver as próximas entradas](README15.md)
